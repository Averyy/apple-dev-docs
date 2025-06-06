# safeAreaInset(edge:alignment:spacing:content:)

**Framework**: FamilyControls  
**Kind**: method

Shows the specified content above or below the modified view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func safeAreaInset<V>(edge: VerticalEdge, alignment: HorizontalAlignment = .center, spacing: CGFloat? = nil, @ViewBuilder content: () -> V) -> some View where V : View
```

#### Return Value

A new view that displays both `content` above or below the modified view, making space for the `content` view by vertically insetting the modified view, adjusting the safe area of the result to match.

#### Discussion

The `content` view is anchored to the specified vertical edge in the parent view, aligning its horizontal axis to the specified alignment guide. The modified view is inset by the height of `content`, from `edge`, with its safe area increased by the same amount.

```swift
struct ScrollableViewWithBottomBar: View {
    var body: some View {
        ScrollView {
            ScrolledContent()
        }
        .safeAreaInset(edge: .bottom, spacing: 0) {
            BottomBarContent()
        }
    }
}
```

## Parameters

- `edge`: The vertical edge of the view to inset by the height of   , to make space for  .
- `spacing`: Extra distance placed between the two views, or   nil to use the default amount of spacing.
- `alignment`: The alignment guide used to position    horizontally.
- `content`: A view builder function providing the view to   display in the inset space of the modified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/safeareainset(edge:alignment:spacing:content:)-1ee0d)*