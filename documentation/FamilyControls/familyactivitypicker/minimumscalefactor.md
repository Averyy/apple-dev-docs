# minimumScaleFactor(_:)

**Framework**: FamilyControls  
**Kind**: method

Sets the minimum amount that text in this view scales down to fit in the available space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func minimumScaleFactor(_ factor: CGFloat) -> some View
```

#### Return Value

A view that limits the amount of text downscaling.

#### Discussion

Use the `minimumScaleFactor(_:)` modifier if the text you place in a view doesn’t fit and it’s okay if the text shrinks to accommodate. For example, a label with a minimum scale factor of `0.5` draws its text in a font size as small as half of the actual font if needed.

In the example below, the `HStack` contains a `Text` label with a line limit of `1`, that is next to a `TextField`. To allow the label to fit into the available space, the `minimumScaleFactor(_:)` modifier shrinks the text as needed to fit into the available space.

```swift
HStack {
    Text("This is a long label that will be scaled to fit:")
        .lineLimit(1)
        .minimumScaleFactor(0.5)
    TextField("My Long Text Field", text: $myTextField)
}
```

## Parameters

- `factor`: A fraction between 0 and 1 (inclusive) you use to   specify the minimum amount of text scaling that this view permits.

## See Also

- [func allowsTightening(Bool) -> some View](familyactivitypicker/allowstightening(_:).md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func truncationMode(Text.TruncationMode) -> some View](familyactivitypicker/truncationmode(_:).md)
  Sets the truncation mode for lines of text that are too long to fit in the available space.
- [func flipsForRightToLeftLayoutDirection(Bool) -> some View](familyactivitypicker/flipsforrighttoleftlayoutdirection(_:).md)
  Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/minimumscalefactor(_:))*