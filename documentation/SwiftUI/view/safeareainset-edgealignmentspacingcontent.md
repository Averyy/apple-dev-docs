# safeAreaInset(edge:alignment:spacing:content:)

**Framework**: SwiftUI  
**Kind**: method

Shows the specified content beside the modified view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func safeAreaInset<V>(edge: HorizontalEdge, alignment: VerticalAlignment = .center, spacing: CGFloat? = nil, @ViewBuilder content: () -> V) -> some View where V : View
```

#### Return Value

A new view that displays `content` beside the modified view, making space for the `content` view by horizontally insetting the modified view.

#### Discussion

The `content` view is anchored to the specified horizontal edge in the parent view, aligning its vertical axis to the specified alignment guide. The modified view is inset by the width of `content`, from `edge`, with its safe area increased by the same amount.

```swift
struct ScrollableViewWithSideBar: View {
    var body: some View {
        ScrollView {
            ScrolledContent()
        }
        .safeAreaInset(edge: .leading, spacing: 0) {
            SideBarContent()
        }
    }
}
```

## Parameters

- `edge`: The horizontal edge of the view to inset by the width of   , to make space for  .
- `alignment`: The alignment guide used to position    vertically.
- `spacing`: Extra distance placed between the two views, or   nil to use the default amount of spacing.
- `content`: A view builder function providing the view to   display in the inset space of the modified view.

## See Also

- [func ignoresSafeArea(SafeAreaRegions, edges: Edge.Set) -> some View](view/ignoressafearea(_:edges:).md)
  Expands the safe area of a view.
- [func safeAreaPadding(_:)](view/safeareapadding(_:).md)
  Adds the provided insets into the safe area of this view.
- [func safeAreaPadding(Edge.Set, CGFloat?) -> some View](view/safeareapadding(_:_:).md)
  Adds the provided insets into the safe area of this view.
- [struct SafeAreaRegions](safearearegions.md)
  A set of symbolic safe area regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/safeareainset(edge:alignment:spacing:content:))*