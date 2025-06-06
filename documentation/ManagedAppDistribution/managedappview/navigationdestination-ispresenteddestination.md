# navigationDestination(isPresented:destination:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Associates a destination view with a binding that can be used to push the view onto a `NavigationStack`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func navigationDestination<V>(isPresented: Binding<Bool>, @ViewBuilder destination: () -> V) -> some View where V : View
```

#### Discussion

In general, favor binding a path to a navigation stack for programmatic navigation. Add this view modifier to a view inside a `NavigationStack` to programmatically push a single view onto the stack. This is useful for building components that can push an associated view. For example, you can present a `ColorDetail` view for a particular color:

```None
@State private var showDetails = false
var favoriteColor: Color

NavigationStack {
    VStack {
        Circle()
            .fill(favoriteColor)
        Button("Show details") {
            showDetails = true
        }
    }
    .navigationDestination(isPresented: $showDetails) {
        ColorDetail(color: favoriteColor)
    }
    .navigationTitle("My Favorite Color")
}
```

Do not put a navigation destination modifier inside a “lazy” container, like `List` or `LazyVStack`. These containers create child views only when needed to render on screen. Add the navigation destination modifier outside these containers so that the navigation stack can always see the destination.

## Parameters

- `isPresented`: A binding to a Boolean value that indicates whether    is currently presented.
- `destination`: A view to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/navigationdestination(ispresented:destination:))*