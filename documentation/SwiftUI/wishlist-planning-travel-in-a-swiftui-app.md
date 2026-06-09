# Wishlist: Planning travel in a SwiftUI app

**Framework**: SwiftUI

Build a travel planning app that organizes trips into collections and tracks activity completion.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

The Wishlist sample app helps people organize travel plans by grouping trips into seasonal collections. Within each trip, people can create activities and mark them complete as they explore. The app rewards progress with achievement badges, tracking milestones like completing a first trip or reaching an activity milestone across all adventures.

The sample project demonstrates how to:

- Compose custom views.
- Manage state with the [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) macro.
- Customize navigation title appearance.
- Animate view changes.
- Create zoom transitions to navigation destinations and between buttons and sheets.

##### Compose Custom Views

SwiftUI views conform to the [`View`](view.md) protocol and define their content through a computed `body` property. Each view returns a description of what appears on screen, and SwiftUI handles the rendering.

Wishlist builds custom views by combining built-in components like [`VStack`](vstack.md), [`HStack`](hstack.md), [`Text`](text.md), [`Image`](image.md), and [`Button`](button.md):

```swift
struct TripCard: View {
    var trip: Trip
    var size: Size

    var body: some View {
        VStack(alignment: .leading, spacing: 5) {
            TripImageView(url: trip.photoURL)
                .scaledToFill()
                .frame(width: size.width, height: size.height)
                .clipShape(.rect(cornerRadius: 16))

            VStack(alignment: .leading, spacing: 0) {
                Text(trip.name)
                    .font(.body)

                if let subtitle = trip.subtitle {
                    Text(subtitle)
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                }
            }
        }
    }
}
```

The outer `VStack` stacks the image and text vertically, aligning content to the leading edge. Apply transformations sequentially by stacking modifiers, with each modifier wrapping the previous view in a new view with modified behavior.

##### Manage State with an Observable Macro

SwiftUI updates views automatically when their dependencies change. Mark model classes with [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) to opt into automatic change tracking. In Wishlist, the `@Observable` macro synthesizes the necessary code to publish changes made to any stored property:

```swift
@Observable
class DataSource {
    var trips: [Trip.ID: Trip] {
        didSet {
            updateGoalAchievements()
        }
    }
    var searchText = ""
}
```

The `DataSource` class stores trips in a [`Dictionary`](https://developer.apple.com/documentation/Swift/Dictionary) keyed by trip ID for efficient lookup. The `didSet` property observer calls `updateGoalAchievements()` whenever the `trips` dictionary changes, keeping goal progress synchronized with trip completion. Any views that read from the `trips` dictionary, like `RecentTripsPageView`, automatically update when the dictionary changes, such as when adding or removing a trip.

To share this data across the sample app, Wishlist creates a state with the [`State`](state.md) property wrapper inside the [`App`](app.md) struct, then injects the data into the view hierarchy with the [`environment(_:)`](view/environment(_:).md) modifier:

```swift
@main
struct WishlistApp: App {
    @State private var dataSource = DataSource()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(dataSource)
        }
    }
}
```

Inside a view, Wishlist gets the observable object using its type, then creates a property and provides the object’s type to the [`Environment`](environment.md) property wrapper:

```swift
struct WishlistView: View {
    @Environment(DataSource.self) private var dataSource

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading, spacing: 10) {
                    RecentTripsPageView()
                    ForEach(TripCollection.allCases) { tripCollection in
                        TripCollectionView(
                            tripCollection: tripCollection,
                            cardSize: tripCollection.cardSize,
                            namespace: namespace
                        )
                    }
                }
            }
        }
    }
}
```

The `@Environment` property wrapper retrieves the data source from the environment and establishes a dependency relationship between the view and the observable model. By default, reading an object from the environment returns a non-optional object when using the object type as the key. This default behavior assumes that a view in the current hierarchy previously stored a non-optional instance of the type using the `environment(_:)` modifier. If a view attempts to retrieve an object using its type and that object isn’t in the environment, SwiftUI throws an exception.

SwiftUI automatically tracks property access within the view’s body. When any observed property changes, SwiftUI updates any parts of the view that depend on the value.

Some built-in views and modifiers in SwiftUI, like [`Toggle`](toggle.md) and [`searchable(text:placement:prompt:)`](view/searchable(text:placement:prompt:).md), take a [`Binding`](binding.md) to a property. This lets these views and modifiers write back changes to the property. Use the [`Bindable`](bindable.md) property wrapper to create bindings to properties of an `Observable` object. This includes global variables, properties that exist outside of SwiftUI types, or even local variables. For example, the sample app creates a `@Bindable` variable within a view’s body:

```swift
struct SearchView: View {
    @Environment(DataSource.self) private var dataSource

    var body: some View {
        @Bindable var dataSource = dataSource

        NavigationStack {
            SearchResultsListView()
                .searchable(text: $dataSource.searchText)
        }
    }
}
```

The `@Bindable` property wrapper exposes a binding projection prefix `$` to produce a `Binding` value. In the above example, `$dataSource.searchText` creates a `Binding<String>` that connects the search field to the data source. When someone types in the search field, SwiftUI writes the new value through the binding, updating the observable property and invalidating dependent views.

##### Customize Navigation Title Appearance

SwiftUI separates visual presentation from semantic meaning when displaying navigation titles.

In the sample app, the `WishlistView` view uses a [`ToolbarItem`](toolbaritem.md) and [`title`](toolbaritemplacement/title.md) `toolbarItem` placement to customize the title’s visual appearance.

```swift
NavigationStack {
    ScrollView {
        // Content
    }
    .toolbar {
        ToolbarItem(placement: .title) {
            ExpandedNavigationTitle(title: "Wishlist")
        }
    }
    .navigationTitle("Wishlist")
    .toolbarTitleDisplayMode(.inline)
}
```

The `ExpandedNavigationTitle` view renders the title with a custom font. Always add a navigation title using [`navigationTitle(_:)`](view/navigationtitle(_:).md), which the system uses for the accessibility label when someone navigates back from a detail view. The [`toolbarTitleDisplayMode(_:)`](view/toolbartitledisplaymode(_:).md) modifier that specifies [`inline`](toolbartitledisplaymode/inline.md) tells SwiftUI to display the title in the navigation bar’s inline position rather than as a large title.

For content that extends into the safe area, use [`largeTitle`](toolbaritemplacement/largetitle.md) placement instead.

##### Animate View Changes

To direct people’s attention to state changes, add animation in one of the following ways:

- Animate all of the visual changes for a state change by changing the state inside a call to the [`withAnimation(_:_:)`](withanimation(_:_:).md) global function.
- Add animation to a particular view when a specific value changes by applying the [`animation(_:value:)`](view/animation(_:value:).md) view modifier to the view.

SwiftUI animates the effects that many built-in view modifiers produce, like those that set a scale or opacity value. You can animate other values by making your custom views conform to the [`Animatable`](animatable.md) protocol. Use the [`Animatable()`](animatable().md) macro to do this.

Choose the right approach based on whether you’re animating a discrete action or responding to specific property changes.

In Wishlist, when a person deletes an activity, `withAnimation` ensures the removal animates smoothly:

```swift
Button("Delete", role: .destructive) {
    withAnimation {
        model.removeActivity(activity)
    }
}
```

The `withAnimation` block establishes an animation transaction. Any view changes that `removeActivity(_:)` triggers animate automatically, sharing the same animation curve and timing.

For finer control, apply animations to specific views using the `animation(_:value:)` modifier. This value-based approach creates a targeted animation that only triggers when the specified value changes, affecting only the view hierarchy where the modifier appears. In the activity completion button in Wishlist, the checkmark icon animates its appearance only when `isComplete` toggles, leaving other view changes unanimated:

```swift
Image(systemName: activity.isComplete ? "checkmark.circle.fill" : "circle")
    .foregroundStyle(activity.isComplete ? Color.accentColor : .gray)
    .contentTransition(.symbolEffect)
    .animation(.snappy, value: activity.isComplete)
```

The `animation(.snappy, value: activity.isComplete)` modifier tells SwiftUI to animate this image when `activity.isComplete` changes, using a snappy spring curve. If other properties change, like the view’s position or opacity, those changes won’t animate unless they also depend on `isComplete`.

To learn more about animations, check out WWDC23 session [`10156: Explore SwiftUI animation`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10156/).

##### Create Zoom Transitions Between Navigation Destinations

To customize animated transitions between views, apply [`matchedTransitionSource(id:in:)`](view/matchedtransitionsource(id:in:).md) to the source view and [`navigationTransition(_:)`](view/navigationtransition(_:).md) with the transition  [`zoom(sourceID:in:)`](navigationtransition/zoom(sourceid:in:).md) to the destination view using matching identifiers. Use the [`Namespace`](namespace.md) property wrapper to create a unique value that associates the source and destination.

In Wishlist, when someone taps a trip card, it smoothly zooms and expands into the trip detail screen, maintaining visual continuity throughout the navigation. Dismissing the detail view reverses the animation, zooming back down into the original card position.

```swift
struct WishlistView: View {
    @Namespace private var namespace

    var body: some View {
        NavigationStack {
            ...
            ForEach(TripCollection.allCases) { tripCollection in
                TripCollectionView(
                    tripCollection: tripCollection,
                    namespace: namespace
                )
            }
        }
    }
}

struct TripCollectionView: View {
    var tripCollection: TripCollection
    var namespace: Namespace.ID

    var body: some View {
        ...
        ForEach(dataSource.trips(in: tripCollection)) { trip in
            NavigationLink {
                TripDetailView(trip: trip)
                    .navigationTransition(.zoom(sourceID: trip.id, in: namespace))
            } label: {
                TripCard(trip: trip, size: cardSize)
                    .matchedTransitionSource(id: trip.id, in: namespace)
            }
        }
        ...
    }
}
```

The `@Namespace` property wrapper creates a unique identifier space that SwiftUI uses to coordinate the transition. Pass the same namespace to both the source and destination views to establish their relationship.

Each `TripCard` in the trip collection receives `matchedTransitionSource(id:in:)` with the trip’s ID as the identifier. When someone taps a card, SwiftUI captures its position, size, and corner radius as the transition’s starting point. The trip detail view applies `navigationTransition(.zoom(sourceID:in:))` with the matching identifier, declaring itself as the zoom target. SwiftUI interpolates between the two geometries, seamlessly morphing one into the other.

Check out WWDC24 session [`10145: Enhance your UI animations and transitions`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2024/10145/) to explore how to adopt the zoom transition in navigation and presentations in your app.

## See Also

- [Declaring a custom view](declaring-a-custom-view.md)
  Define views and assemble them into a view hierarchy.
- [protocol View](view.md)
  A type that represents part of your app’s user interface and provides modifiers that you use to configure views.
- [typealias ContentBuilder](contentbuilder.md)
  A custom parameter attribute that constructs views and other content types from closures.
- [struct ViewBuilder](viewbuilder.md)
  A custom parameter attribute that constructs views from closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wishlist-planning-travel-in-a-swiftui-app)*