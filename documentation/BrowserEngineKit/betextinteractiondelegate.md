# BETextInteractionDelegate

**Framework**: BrowserEngineKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that informs you about selection changes in text views.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
protocol BETextInteractionDelegate
```

```objc
@protocol BETextInteractionDelegate
```

## Topics

### Text selection changes
- [func systemWillChangeSelection(for: BETextInteraction)](./betextinteractiondelegate/systemwillchangeselection%28for%29.md)
  Invoked by the system when the selection is about to change in the document.
- [func systemDidChangeSelection(for: BETextInteraction)](./betextinteractiondelegate/systemdidchangeselection%28for%29.md)
  Invoked by the system when the selection is about to change in the document.

## See Also

### Interaction responses
- [class BETextInteraction](./betextinteraction.md)
  An interaction you add to a text view to support extended text gestures.
- [protocol BEResponderEditActions](./berespondereditactions.md)
  A set of methods that defines extended interactions in browser text views.
- [enum BEGestureType](./begesturetype.md)
  The types of touch gestures that operate on input text.
- [protocol BEResponderEditActions](./berespondereditactions.md)
  A set of methods that defines extended interactions in browser text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinteractiondelegate)*