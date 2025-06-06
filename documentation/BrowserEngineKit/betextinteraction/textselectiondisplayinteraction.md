# textSelectionDisplayInteraction

**Framework**: BrowserEngineKit  
**Kind**: property

An interaction that manages the system’s text-selection UI.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
var textSelectionDisplayInteraction: UITextSelectionDisplayInteraction { get }
```

## See Also

- [var delegate: (any BETextInteractionDelegate)?](betextinteraction/delegate.md)
  A delegate object that the interaction notifies when the system changes the text selection.
- [protocol BETextInteractionDelegate](betextinteractiondelegate.md)
  A set of methods that informs you about selection changes in text views.
- [func selectionBoundaryAdjusted(to: CGPoint, touchPhase: BESelectionTouchPhase, flags: BESelectionFlags)](betextinteraction/selectionboundaryadjusted(to:touchphase:flags:).md)
  Notifies the system after the text view adjusts its selection.
- [func selectionChangedWithGesture(at: CGPoint, gesture: BEGestureType, state: UIGestureRecognizer.State, flags: BESelectionFlags)](betextinteraction/selectionchangedwithgesture(at:gesture:state:flags:).md)
  Notifies the system that the text view changed its selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteraction/textselectiondisplayinteraction)*