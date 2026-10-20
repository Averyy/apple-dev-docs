# alignmentFeedbackTokenForMovement(in:previousPoint:alignedPoint:defaultPoint:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Requests a feedback token for the alignment of an object requiring horizontal and vertical movement.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func alignmentFeedbackTokenForMovement(in view: NSView?, previousPoint: NSPoint, alignedPoint: NSPoint, defaultPoint: NSPoint) -> (any NSAlignmentFeedbackToken)?
```

```objc
- (id<NSAlignmentFeedbackToken>) alignmentFeedbackTokenForMovementInView:(NSView *) view previousPoint:(NSPoint) previousPoint alignedPoint:(NSPoint) alignedPoint defaultPoint:(NSPoint) defaultPoint;
```

#### Return Value

A null value if the system determines that the alignment should not occur. Otherwise, a feedback token of type `NSAlignmentFeedbackToken` is returned.

#### Discussion

This method requests a feedback token for the alignment of an object requiring horizontal and vertical movement.

If a feedback token is returned, call [`performFeedback(_:performanceTime:)`](./performfeedback%28_,performancetime%29.md) to initiate haptic feedback. Then, move the object to its aligned location.

If no feedback token is returned, don’t perform the alignment or request haptic feedback. Even if this joint horizontal and vertical alignment fails, be sure to check other alignments. For example, an individual horizontal or vertical alignment may still be allowed. If no alignments will occur, move the object to its default location.

## Parameters

- `view`: The view ([`NSView`](../nsview.md)) in which the object was moved.
- `previousPoint`: The location ([`NSPoint`](../../Foundation/nspoint.md)) of the object prior to its move.
- `alignedPoint`: The new location ([`NSPoint`](../../Foundation/nspoint.md)) of the object if alignment occurs.
- `defaultPoint`: The current location ([`NSPoint`](../../Foundation/nspoint.md)) of the object. This is where the user actually moved the object. This location may be offset from the location of the cursor.

## See Also

### Related Documentation
- [func performFeedback([any NSAlignmentFeedbackToken], performanceTime: NSHapticFeedbackManager.PerformanceTime)](./performfeedback%28_,performancetime%29.md)
  Performs the haptic feedback described by one or more alignment feedback tokens.
### Preparing Haptic Feedback for Alignment
- [func alignmentFeedbackTokenForHorizontalMovement(in: NSView?, previousX: CGFloat, alignedX: CGFloat, defaultX: CGFloat) -> (any NSAlignmentFeedbackToken)?](./alignmentfeedbacktokenforhorizontalmovement%28in,previousx,alignedx,defaultx%29.md)
  Requests a feedback token for the alignment of an object requiring horizontal movement only.
- [func alignmentFeedbackTokenForVerticalMovement(in: NSView?, previousY: CGFloat, alignedY: CGFloat, defaultY: CGFloat) -> (any NSAlignmentFeedbackToken)?](./alignmentfeedbacktokenforverticalmovement%28in,previousy,alignedy,defaulty%29.md)
  Requests a feedback token for the alignment of an object requiring vertical movement only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalignmentfeedbackfilter/alignmentfeedbacktokenformovement(in:previouspoint:alignedpoint:defaultpoint:))*