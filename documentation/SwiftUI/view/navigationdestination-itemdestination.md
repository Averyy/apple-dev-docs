# navigationDestination(item:destination:)

**Framework**: SwiftUI  
**Kind**: method

Associates a destination view with a bound value for use within a navigation stack or navigation split view

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func navigationDestination<D, C>(item: Binding<Optional<D>>, @ViewBuilder destination: @escaping (D) -> C) -> some View where D : Hashable, C : View
```

## Mentions

- [Understanding the navigation stack](understanding-the-composition-of-navigation-stack.md)

#### Discussion

Add this view modifier to a view inside a [`NavigationStack`](navigationstack.md) or [`NavigationSplitView`](navigationsplitview.md) to describe the view that the stack displays when presenting a particular kind of data. Programmatically update the binding to display or remove the view. For example, you can replace the view showing in the detail column of a navigation split view:

```swift
@State private var colorShown: Color?

NavigationSplitView {
    List {
        Button("Mint") { colorShown = .mint }
        Button("Pink") { colorShown = .pink }
        Button("Teal") { colorShown = .teal }
    }
    .navigationDestination(item: $colorShown) { color in
        ColorDetail(color: color)
    }
} detail: {
    Text("Select a color")
}
```

When the person using the app taps on the Mint button, the mint color shows in the detail and `colorShown` gets the value `Color.mint`. You can reset the navigation split view to show the message “Select a color” by setting `colorShown` back to `nil`.

You can add more than one navigation destination modifier to the stack if it needs to present more than one kind of data.

Do not put a navigation destination modifier inside a “lazy” container, like [`List`](list.md) or [`LazyVStack`](lazyvstack.md). These containers create child views only when needed to render on screen. Add the navigation destination modifier outside these containers so that the navigation split view can always see the destination.

## Parameters

- `item`: A binding to the data presented, or   if nothing is   currently presented.
- `destination`: A view builder that defines a view to display   when   is not  .

## See Also

- [struct NavigationStack](navigationstack.md)
  A view that displays a root view and enables you to present additional views over the root view.
- [struct NavigationPath](navigationpath.md)
  A type-erased list of data representing the content of a navigation stack.
- [func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some View](view/navigationdestination(for:destination:).md)
  Associates a destination view with a presented data type for use within a navigation stack.
- [func navigationDestination<V>(isPresented: Binding<Bool>, destination: () -> V) -> some View](view/navigationdestination(ispresented:destination:).md)
  Associates a destination view with a binding that can be used to push the view onto a [`NavigationStack`](navigationstack.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationdestination(item:destination:))*