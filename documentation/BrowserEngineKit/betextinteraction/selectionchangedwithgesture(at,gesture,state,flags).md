# selectionChangedWithGesture(at:gesture:state:flags:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Notifies the system that the text view changed its selection.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func selectionChangedWithGesture(at point: CGPoint, gesture gestureType: BEGestureType, state gestureState: UIGestureRecognizer.State, flags: BESelectionFlags)
```

```objc
- (void) selectionChangedWithGestureAtPoint:(CGPoint) point gesture:(BEGestureType) gestureType state:(UIGestureRecognizerState) gestureState flags:(BESelectionFlags) flags;
```

#### Discussion

Call this method when your browser text view receives [`updateCurrentSelection(to:from:in:)`](../betextinput/updatecurrentselection%28to,from,in%29.md).

## See Also

### Text selection
- [var delegate: (any BETextInteractionDelegate)?](./delegate.md)
  A delegate object that the interaction notifies when the system changes the text selection.
- [protocol BETextInteractionDelegate](../betextinteractiondelegate.md)
  A set of methods that informs you about selection changes in text views.
- [var textSelectionDisplayInteraction: UITextSelectionDisplayInteraction](./textselectiondisplayinteraction.md)
  An interaction that manages the system’s text-selection UI.
- [func selectionBoundaryAdjusted(to: CGPoint, touchPhase: BESelectionTouchPhase, flags: BESelectionFlags)](./selectionboundaryadjusted%28to,touchphase,flags%29.md)
  Notifies the system after the text view adjusts its selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/selectionchangedwithgesture(at:gesture:state:flags:))*