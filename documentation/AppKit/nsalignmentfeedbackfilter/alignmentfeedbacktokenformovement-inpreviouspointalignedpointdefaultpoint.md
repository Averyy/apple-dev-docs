# alignmentFeedbackTokenForMovement(in:previousPoint:alignedPoint:defaultPoint:)

**Framework**: AppKit  
**Kind**: method

Requests a feedback token for the alignment of an object requiring horizontal and vertical movement.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func alignmentFeedbackTokenForMovement(in view: NSView?, previousPoint: NSPoint, alignedPoint: NSPoint, defaultPoint: NSPoint) -> (any NSAlignmentFeedbackToken)?
```

#### Return Value

A null value if the system determines that the alignment should not occur. Otherwise, a feedback token of type `NSAlignmentFeedbackToken` is returned.

#### Discussion

This method requests a feedback token for the alignment of an object requiring horizontal and vertical movement.

If a feedback token is returned, call [`performFeedback(_:performanceTime:)`](nsalignmentfeedbackfilter/performfeedback(_:performancetime:).md) to initiate haptic feedback. Then, move the object to its aligned location.

If no feedback token is returned, don’t perform the alignment or request haptic feedback. Even if this joint horizontal and vertical alignment fails, be sure to check other alignments. For example, an individual horizontal or vertical alignment may still be allowed. If no alignments will occur, move the object to its default location.

## Parameters

- `view`: The view ( ) in which the object was moved.
- `previousPoint`: The location ( ) of the object prior to its move.
- `alignedPoint`: The new location ( ) of the object if alignment occurs.
- `defaultPoint`: The current location ( ) of the object. This is where the user actually moved the object. This location may be offset from the location of the cursor.

## See Also

- [func performFeedback([any NSAlignmentFeedbackToken], performanceTime: NSHapticFeedbackManager.PerformanceTime)](nsalignmentfeedbackfilter/performfeedback(_:performancetime:).md)
  Performs the haptic feedback described by one or more alignment feedback tokens.
- [func alignmentFeedbackTokenForHorizontalMovement(in: NSView?, previousX: CGFloat, alignedX: CGFloat, defaultX: CGFloat) -> (any NSAlignmentFeedbackToken)?](nsalignmentfeedbackfilter/alignmentfeedbacktokenforhorizontalmovement(in:previousx:alignedx:defaultx:).md)
  Requests a feedback token for the alignment of an object requiring horizontal movement only.
- [func alignmentFeedbackTokenForVerticalMovement(in: NSView?, previousY: CGFloat, alignedY: CGFloat, defaultY: CGFloat) -> (any NSAlignmentFeedbackToken)?](nsalignmentfeedbackfilter/alignmentfeedbacktokenforverticalmovement(in:previousy:alignedy:defaulty:).md)
  Requests a feedback token for the alignment of an object requiring vertical movement only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalignmentfeedbackfilter/alignmentfeedbacktokenformovement(in:previouspoint:alignedpoint:defaultpoint:))*