# minPossiblePositionOfDivider(at:)

**Framework**: AppKit  
**Kind**: method

Returns the minimum possible position of the divider at the specified index.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func minPossiblePositionOfDivider(at dividerIndex: Int) -> CGFloat
```

#### Return Value

A [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct) that specifies the minimum possible position of the divider.

#### Discussion

The position is  because the bounds of the split view and the current position of other dividers dictate it.  positions result from letting the delegate apply constraints to the possible positions.

You can invoke this method to determine the range of values that you can pass to [`setPosition(_:ofDividerAt:)`](nssplitview/setposition(_:ofdividerat:).md). You can also invoke it from delegate methods like [`splitView(_:constrainSplitPosition:ofSubviewAt:)`](nssplitviewdelegate/splitview(_:constrainsplitposition:ofsubviewat:).md) to implement relatively complex behaviors that depend on the current state of the split view.

The result of invoking this method when you haven’t invoked [`adjustSubviews()`](nssplitview/adjustsubviews().md), and the subview frames are invalid, is undefined.

## Parameters

- `dividerIndex`: The index of the divider.

## See Also

- [func maxPossiblePositionOfDivider(at: Int) -> CGFloat](nssplitview/maxpossiblepositionofdivider(at:).md)
  Returns the maximum possible position of the divider at the specified index.
- [func setPosition(CGFloat, ofDividerAt: Int)](nssplitview/setposition(_:ofdividerat:).md)
  Updates the location of a divider you specify by index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/minpossiblepositionofdivider(at:))*