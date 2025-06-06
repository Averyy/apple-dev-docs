# updateCurrentSelection(to:from:in:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Indicates the `point` the text interaction gesture is tracking has changed

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func updateCurrentSelection(to point: CGPoint, from gestureType: BEGestureType, in state: UIGestureRecognizer.State)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

Indicate to the system the change was handled by invoking: -[BETextInteraction selectionChangedWithGestureAtPoint:gesture:state:flags:]

Indicates that the point at which the system is tracking an active gesture changed.

#### Overview

When you receive this method, call [`selectionChangedWithGesture(at:gesture:state:flags:)`](betextinteraction/selectionchangedwithgesture(at:gesture:state:flags:).md) to notify the system that your text view handled the update.

## Parameters

- `point`: The new location of the gesture.
- `gestureType`: The type of gesture the system is tracking.
- `state`: The state of the gesture.

## See Also

- [func setSelection(from: CGPoint, to: CGPoint, gesture: BEGestureType, state: UIGestureRecognizer.State)](betextinput/setselection(from:to:gesture:state:).md)
  Notifies the text view that its selection needs to change to the text between the given points.
- [func adjustSelectionBoundary(to: CGPoint, touchPhase: BESelectionTouchPhase, baseIsStart: Bool, flags: BESelectionFlags)](betextinput/adjustselectionboundary(to:touchphase:baseisstart:flags:).md)
  Adjusts the selection’s start or end boundary specified by `boundaryIsStart` to the `point`
- [func textInteractionGesture(BEGestureType, shouldBeginAt: CGPoint) -> Bool](betextinput/textinteractiongesture(_:shouldbeginat:).md)
  Returns whether a gesture with the given `gestureType` should begin for the given `point`


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/updatecurrentselection(to:from:in:))*