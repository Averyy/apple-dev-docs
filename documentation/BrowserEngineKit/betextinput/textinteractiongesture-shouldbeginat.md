# textInteractionGesture(_:shouldBeginAt:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Returns whether a gesture with the given `gestureType` should begin for the given `point`

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func textInteractionGesture(_ gestureType: BEGestureType, shouldBeginAt point: CGPoint) -> Bool
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Return Value

`true` to permit the text system to proceed with the gesture; `false` otherwise.

#### Discussion

Returns whether a gesture at the given point in the view needs to begin.

## Parameters

- `gestureType`: The type of gesture that’s possibly beginning.
- `point`: The location of the gesture in the text view.

## See Also

- [func updateCurrentSelection(to: CGPoint, from: BEGestureType, in: UIGestureRecognizer.State)](betextinput/updatecurrentselection(to:from:in:).md)
  Indicates the `point` the text interaction gesture is tracking has changed
- [func setSelection(from: CGPoint, to: CGPoint, gesture: BEGestureType, state: UIGestureRecognizer.State)](betextinput/setselection(from:to:gesture:state:).md)
  Notifies the text view that its selection needs to change to the text between the given points.
- [func adjustSelectionBoundary(to: CGPoint, touchPhase: BESelectionTouchPhase, baseIsStart: Bool, flags: BESelectionFlags)](betextinput/adjustselectionboundary(to:touchphase:baseisstart:flags:).md)
  Adjusts the selection’s start or end boundary specified by `boundaryIsStart` to the `point`


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/textinteractiongesture(_:shouldbeginat:))*