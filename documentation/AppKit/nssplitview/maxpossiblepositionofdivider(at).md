# maxPossiblePositionOfDivider(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the maximum possible position of the divider at the specified index.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func maxPossiblePositionOfDivider(at dividerIndex: Int) -> CGFloat
```

```objc
- (CGFloat) maxPossiblePositionOfDividerAtIndex:(NSInteger) dividerIndex;
```

## Return Value

A [`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md) that specifies the maximum possible position of the divider.

## Discussion

The position is *possible* because the bounds of the split view and the current position of other dividers dictate it. *Allowable* positions result from letting the delegate apply constraints to the possible positions.

You can invoke this method to determine the range of values that you can pass to [`setPosition(_:ofDividerAt:)`](./setposition%28_,ofdividerat%29.md). You can also invoke it from delegate methods like [`splitView(_:constrainSplitPosition:ofSubviewAt:)`](../nssplitviewdelegate/splitview%28_,constrainsplitposition,ofsubviewat%29.md) to implement relatively complex behaviors that depend on the current state of the split view.

The result of invoking this method when you haven’t invoked [`adjustSubviews()`](./adjustsubviews%28%29.md), and the subview frames are invalid, is undefined.

## Parameters

- `dividerIndex`: The index of the divider.

## See Also

### Constraining Split Position
- [func minPossiblePositionOfDivider(at: Int) -> CGFloat](./minpossiblepositionofdivider%28at%29.md)
  Returns the minimum possible position of the divider at the specified index.
- [func setPosition(CGFloat, ofDividerAt: Int)](./setposition%28_,ofdividerat%29.md)
  Updates the location of a divider you specify by index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitview/maxpossiblepositionofdivider(at:))*