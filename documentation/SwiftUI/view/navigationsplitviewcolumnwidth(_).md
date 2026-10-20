# navigationSplitViewColumnWidth(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets a fixed, preferred width for the column containing this view.

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
func navigationSplitViewColumnWidth(_ width: CGFloat) -> some View
```

#### Discussion

Apply this modifier to the content of a column in a [`NavigationSplitView`](../navigationsplitview.md) to specify a fixed preferred width for the column. Use [`navigationSplitViewColumnWidth(min:ideal:max:)`](./navigationsplitviewcolumnwidth%28min,ideal,max%29.md) if you need to specify a flexible width.

The following example shows a three-column navigation split view where the first column has a preferred width of 150 points, and the second column has a flexible, preferred width between 150 and 400 points:

```swift
NavigationSplitView {
    MySidebar()
        .navigationSplitViewColumnWidth(150)
} contents: {
    MyContents()
        .navigationSplitViewColumnWidth(
            min: 150, ideal: 200, max: 400)
} detail: {
    MyDetail()
}
```

Only some platforms enable resizing columns. If you specify a width that the current presentation environment doesn’t support, SwiftUI may use a different width for your column.

## See Also

### Presenting views in columns
- [Bringing robust navigation structure to your SwiftUI app](../bringing-robust-navigation-structure-to-your-swiftui-app.md)
  Use navigation links, stacks, destinations, and paths to provide a streamlined experience for all platforms, as well as behaviors such as deep linking and state restoration.
- [Migrating to new navigation types](../migrating-to-new-navigation-types.md)
  Improve navigation behavior in your app by replacing navigation views with navigation stacks and navigation split views.
- [struct NavigationSplitView](../navigationsplitview.md)
  A view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns.
- [func navigationSplitViewStyle<S>(S) -> some View](./navigationsplitviewstyle%28_%29.md)
  Sets the style for navigation split views within this view.
- [func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](./navigationsplitviewcolumnwidth%28min,ideal,max%29.md)
  Sets a flexible, preferred width for the column containing this view.
- [struct NavigationSplitViewVisibility](../navigationsplitviewvisibility.md)
  The visibility of the leading columns in a navigation split view.
- [struct NavigationLink](../navigationlink.md)
  A view that controls a navigation presentation.
- [struct NavigationView](../navigationview.md)
  A view for presenting a stack of views that represents a visible path in a navigation hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationsplitviewcolumnwidth(_:))*