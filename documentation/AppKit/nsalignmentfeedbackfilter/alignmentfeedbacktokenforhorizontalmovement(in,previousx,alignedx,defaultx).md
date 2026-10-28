# alignmentFeedbackTokenForHorizontalMovement(in:previousX:alignedX:defaultX:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Requests a feedback token for the alignment of an object requiring horizontal movement only.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func alignmentFeedbackTokenForHorizontalMovement(in view: NSView?, previousX: CGFloat, alignedX: CGFloat, defaultX: CGFloat) -> (any NSAlignmentFeedbackToken)?
```

```objc
- (id<NSAlignmentFeedbackToken>) alignmentFeedbackTokenForHorizontalMovementInView:(NSView *) view previousX:(CGFloat) previousX alignedX:(CGFloat) alignedX defaultX:(CGFloat) defaultX;
```

## Return Value

If the system determines that the alignment should not occur, a null value is returned. Otherwise, a feedback token of type `NSAlignmentFeedbackToken` is returned.

## Discussion

This method requests a feedback token for the alignment of an object requiring horizontal movement only.

If a feedback token is returned, call [`performFeedback(_:performanceTime:)`](./performfeedback%28_,performancetime%29.md) to initiate haptic feedback. Then, move the object to its aligned location.

If no feedback token is returned, don’t perform the horizontal alignment or request haptic feedback. Even if this horizontal alignment fails, be sure to check other alignments. For example, a vertical alignment may still be allowed. If no alignments will occur, move the object to its default location.

## Parameters

- `view`: The view ([`NSView`](../nsview.md)) in which the object was moved.
- `previousX`: The horizontal location ([`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md)) of the object prior to its move.
- `alignedX`: The new horizontal location ([`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md)) of the object if alignment occurs.
- `defaultX`: The current horizontal location ([`CGFloat`](../../CoreFoundation/cgfloat-swift.struct.md)) of the object. This is where the user actually moved the object. This location may be offset from the location of the cursor.

## See Also

### Related Documentation
- [func performFeedback([any NSAlignmentFeedbackToken], performanceTime: NSHapticFeedbackManager.PerformanceTime)](./performfeedback%28_,performancetime%29.md)
  Performs the haptic feedback described by one or more alignment feedback tokens.
### Preparing Haptic Feedback for Alignment
- [func alignmentFeedbackTokenForMovement(in: NSView?, previousPoint: NSPoint, alignedPoint: NSPoint, defaultPoint: NSPoint) -> (any NSAlignmentFeedbackToken)?](./alignmentfeedbacktokenformovement%28in,previouspoint,alignedpoint,defaultpoint%29.md)
  Requests a feedback token for the alignment of an object requiring horizontal and vertical movement.
- [func alignmentFeedbackTokenForVerticalMovement(in: NSView?, previousY: CGFloat, alignedY: CGFloat, defaultY: CGFloat) -> (any NSAlignmentFeedbackToken)?](./alignmentfeedbacktokenforverticalmovement%28in,previousy,alignedy,defaulty%29.md)
  Requests a feedback token for the alignment of an object requiring vertical movement only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalignmentfeedbackfilter/alignmentfeedbacktokenforhorizontalmovement(in:previousx:alignedx:defaultx:))*