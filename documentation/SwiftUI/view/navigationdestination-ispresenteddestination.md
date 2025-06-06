# navigationDestination(isPresented:destination:)

**Framework**: SwiftUI  
**Kind**: method

Associates a destination view with a binding that can be used to push the view onto a [`NavigationStack`](navigationstack.md).

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func navigationDestination<V>(isPresented: Binding<Bool>, @ViewBuilder destination: () -> V) -> some View where V : View
```

## Mentions

- [Understanding the navigation stack](understanding-the-composition-of-navigation-stack.md)

#### Discussion

In general, favor binding a path to a navigation stack for programmatic navigation. Add this view modifier to a view inside a [`NavigationStack`](navigationstack.md) to programmatically push a single view onto the stack. This is useful for building components that can push an associated view. For example, you can present a `ColorDetail` view for a particular color:

```swift
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

Do not put a navigation destination modifier inside a “lazy” container, like [`List`](list.md) or [`LazyVStack`](lazyvstack.md). These containers create child views only when needed to render on screen. Add the navigation destination modifier outside these containers so that the navigation stack can always see the destination.

## Parameters

- `isPresented`: A binding to a Boolean value that indicates whether    is currently presented.
- `destination`: A view to present.

## See Also

- [struct NavigationStack](navigationstack.md)
  A view that displays a root view and enables you to present additional views over the root view.
- [struct NavigationPath](navigationpath.md)
  A type-erased list of data representing the content of a navigation stack.
- [func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some View](view/navigationdestination(for:destination:).md)
  Associates a destination view with a presented data type for use within a navigation stack.
- [func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D) -> C) -> some View](view/navigationdestination(item:destination:).md)
  Associates a destination view with a bound value for use within a navigation stack or navigation split view


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationdestination(ispresented:destination:))*