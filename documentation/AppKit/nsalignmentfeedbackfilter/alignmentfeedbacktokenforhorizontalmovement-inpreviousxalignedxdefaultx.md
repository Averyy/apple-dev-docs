# alignmentFeedbackTokenForHorizontalMovement(in:previousX:alignedX:defaultX:)

**Framework**: AppKit  
**Kind**: method

Requests a feedback token for the alignment of an object requiring horizontal movement only.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func alignmentFeedbackTokenForHorizontalMovement(in view: NSView?, previousX: CGFloat, alignedX: CGFloat, defaultX: CGFloat) -> (any NSAlignmentFeedbackToken)?
```

#### Return Value

If the system determines that the alignment should not occur, a null value is returned. Otherwise, a feedback token of type `NSAlignmentFeedbackToken` is returned.

#### Discussion

This method requests a feedback token for the alignment of an object requiring horizontal movement only.

If a feedback token is returned, call [`performFeedback(_:performanceTime:)`](nsalignmentfeedbackfilter/performfeedback(_:performancetime:).md) to initiate haptic feedback. Then, move the object to its aligned location.

If no feedback token is returned, don’t perform the horizontal alignment or request haptic feedback. Even if this horizontal alignment fails, be sure to check other alignments. For example, a vertical alignment may still be allowed. If no alignments will occur, move the object to its default location.

## Parameters

- `view`: The view ( ) in which the object was moved.
- `previousX`: The horizontal location ( ) of the object prior to its move.
- `alignedX`: The new horizontal location ( ) of the object if alignment occurs.
- `defaultX`: The current horizontal location ( ) of the object. This is where the user actually moved the object. This location may be offset from the location of the cursor.

## See Also

- [func performFeedback([any NSAlignmentFeedbackToken], performanceTime: NSHapticFeedbackManager.PerformanceTime)](nsalignmentfeedbackfilter/performfeedback(_:performancetime:).md)
  Performs the haptic feedback described by one or more alignment feedback tokens.
- [func alignmentFeedbackTokenForMovement(in: NSView?, previousPoint: NSPoint, alignedPoint: NSPoint, defaultPoint: NSPoint) -> (any NSAlignmentFeedbackToken)?](nsalignmentfeedbackfilter/alignmentfeedbacktokenformovement(in:previouspoint:alignedpoint:defaultpoint:).md)
  Requests a feedback token for the alignment of an object requiring horizontal and vertical movement.
- [func alignmentFeedbackTokenForVerticalMovement(in: NSView?, previousY: CGFloat, alignedY: CGFloat, defaultY: CGFloat) -> (any NSAlignmentFeedbackToken)?](nsalignmentfeedbackfilter/alignmentfeedbacktokenforverticalmovement(in:previousy:alignedy:defaulty:).md)
  Requests a feedback token for the alignment of an object requiring vertical movement only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalignmentfeedbackfilter/alignmentfeedbacktokenforhorizontalmovement(in:previousx:alignedx:defaultx:))*