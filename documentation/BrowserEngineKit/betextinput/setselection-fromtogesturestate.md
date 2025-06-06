# setSelection(from:to:gesture:state:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Notifies the text view that its selection needs to change to the text between the given points.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func setSelection(from: CGPoint, to: CGPoint, gesture: BEGestureType, state: UIGestureRecognizer.State)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

## Parameters

- `from`: The start of the selected region.
- `to`: The end of the selected region.
- `gesture`: The gesture that changes the selection.
- `state`: The state of the gesture.

## See Also

- [func updateCurrentSelection(to: CGPoint, from: BEGestureType, in: UIGestureRecognizer.State)](betextinput/updatecurrentselection(to:from:in:).md)
  Indicates the `point` the text interaction gesture is tracking has changed
- [func adjustSelectionBoundary(to: CGPoint, touchPhase: BESelectionTouchPhase, baseIsStart: Bool, flags: BESelectionFlags)](betextinput/adjustselectionboundary(to:touchphase:baseisstart:flags:).md)
  Adjusts the selection’s start or end boundary specified by `boundaryIsStart` to the `point`
- [func textInteractionGesture(BEGestureType, shouldBeginAt: CGPoint) -> Bool](betextinput/textinteractiongesture(_:shouldbeginat:).md)
  Returns whether a gesture with the given `gestureType` should begin for the given `point`


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/setselection(from:to:gesture:state:))*