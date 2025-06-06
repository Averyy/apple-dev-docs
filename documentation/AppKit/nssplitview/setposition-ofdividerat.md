# setPosition(_:ofDividerAt:)

**Framework**: AppKit  
**Kind**: method

Updates the location of a divider you specify by index.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setPosition(_ position: CGFloat, ofDividerAt dividerIndex: Int)
```

#### Discussion

One of the views adjacent to the divider may collapse because the method’s default implementation assumes a person is dragging the divider to the new location. The Auto Layout system collapses the view if it can’t satisfy the view’s constraints — typically imposed by its delegate — with the divider’s new location.

[`NSSplitView`](nssplitview.md) doesn’t invoke this method.

## Parameters

- `position`: The position of the divider.
- `dividerIndex`: The index of the divider.

## See Also

- [func minPossiblePositionOfDivider(at: Int) -> CGFloat](nssplitview/minpossiblepositionofdivider(at:).md)
  Returns the minimum possible position of the divider at the specified index.
- [func maxPossiblePositionOfDivider(at: Int) -> CGFloat](nssplitview/maxpossiblepositionofdivider(at:).md)
  Returns the maximum possible position of the divider at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/setposition(_:ofdividerat:))*