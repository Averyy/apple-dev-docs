# navigationLinkIndicatorVisibility(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures whether navigation links show a disclosure indicator.

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
@MainActor
@preconcurrency func navigationLinkIndicatorVisibility(_ visibility: Visibility) -> some View
```

#### Discussion

If you need to detect whether the navigation disclosure indicator should be shown for the current view, read the [`navigationLinkIndicatorVisibility`](environmentvalues/navigationlinkindicatorvisibility.md) environment value.

The following example hides the indicator for all links in the list. The indicator can be hidden for a specific link by placing the modifier on the `NavigationLink` itself.

```swift
struct NoIndicatorLink: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("See detail") {
                    Text("Detail view")
                }
            }
            .navigationLinkIndicatorVisibility(.hidden)
        }
    }
}
```

> ❗ **Important**: Setting the link indicator visibility to `.visible` is only supported for navigation links contained in a `List` built with the Xcode 16 SDKs and earlier. Current releases support setting the indicator visibility to `.visible` regardless of whether the link is within a list.

## See Also

- [func navigationDestination<D, C>(for: D.Type, destination: (D) -> C) -> some View](view/navigationdestination(for:destination:).md)
  Associates a destination view with a presented data type for use within a navigation stack.
- [func navigationDestination<V>(isPresented: Binding<Bool>, destination: () -> V) -> some View](view/navigationdestination(ispresented:destination:).md)
  Associates a destination view with a binding that can be used to push the view onto a [`NavigationStack`](navigationstack.md).
- [func navigationDestination<D, C>(item: Binding<Optional<D>>, destination: (D) -> C) -> some View](view/navigationdestination(item:destination:).md)
  Associates a destination view with a bound value for use within a navigation stack or navigation split view
- [func navigationSplitViewColumnWidth(CGFloat) -> some View](view/navigationsplitviewcolumnwidth(_:).md)
  Sets a fixed, preferred width for the column containing this view.
- [func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](view/navigationsplitviewcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the column containing this view.
- [func navigationTransition(some NavigationTransition) -> some View](view/navigationtransition(_:).md)
  Sets the navigation transition style for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationlinkindicatorvisibility(_:))*