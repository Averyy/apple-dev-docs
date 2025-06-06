# adjustSelectionBoundary(to:touchPhase:baseIsStart:flags:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Adjusts the selection’s start or end boundary specified by `boundaryIsStart` to the `point`

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func adjustSelectionBoundary(to point: CGPoint, touchPhase touch: BESelectionTouchPhase, baseIsStart boundaryIsStart: Bool, flags: BESelectionFlags)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

For example, the selection’s boundary would be adjusted when the user moves the selection handles

Indicate to the system that the change was handled by invoking: -[BETextInteraction selectionBoundaryAdjustedToPoint:touchPhase:flags:]

Adjusts the start or end boundary of the current selection to the given point.

#### Overview

When you receive this method, call [`selectionBoundaryAdjusted(to:touchPhase:flags:)`](betextinteraction/selectionboundaryadjusted(to:touchphase:flags:).md) to notify the system that your text view handled the update.

## Parameters

- `point`: The new boundary point of the selection.
- `touch`: The touch phase of the gesture.
- `boundaryIsStart`:   if the   is at the new start of the selection;   if it’s at the end.
- `flags`: Extra information about the selection.

## See Also

- [func updateCurrentSelection(to: CGPoint, from: BEGestureType, in: UIGestureRecognizer.State)](betextinput/updatecurrentselection(to:from:in:).md)
  Indicates the `point` the text interaction gesture is tracking has changed
- [func setSelection(from: CGPoint, to: CGPoint, gesture: BEGestureType, state: UIGestureRecognizer.State)](betextinput/setselection(from:to:gesture:state:).md)
  Notifies the text view that its selection needs to change to the text between the given points.
- [func textInteractionGesture(BEGestureType, shouldBeginAt: CGPoint) -> Bool](betextinput/textinteractiongesture(_:shouldbeginat:).md)
  Returns whether a gesture with the given `gestureType` should begin for the given `point`


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/adjustselectionboundary(to:touchphase:baseisstart:flags:))*