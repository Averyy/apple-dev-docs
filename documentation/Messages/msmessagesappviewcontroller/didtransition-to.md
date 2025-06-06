# didTransition(to:)

**Framework**: Messages  
**Kind**: method

Tells the view controller that the extension has transitioned to a new presentation style.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func didTransition(to presentationStyle: MSMessagesAppPresentationStyle)
```

#### Discussion

Override this method to respond after the extension’s user interface has transitioned to a new presentation style. The user can switch between styles by tapping the collapse and expand buttons in the Messages app. You can also programmatically trigger a transition by calling [`requestPresentationStyle(_:)`](msmessagesappviewcontroller/requestpresentationstyle(_:).md).

The system doesn’t call this method on a view controller that is presenting a live view in the transcript or input field—in other words, when the view controller’s [`presentationStyle`](msmessagesappviewcontroller/presentationstyle.md) property is set to the [`MSMessagesAppPresentationStyle.transcript`](msmessagesapppresentationstyle/transcript.md) value.

## Parameters

- `presentationStyle`: The new presentation style. For a list of possible styles, see  .

## See Also

- [var presentationStyle: MSMessagesAppPresentationStyle](msmessagesappviewcontroller/presentationstyle.md)
  The extension’s current presentation style.
- [func requestPresentationStyle(MSMessagesAppPresentationStyle)](msmessagesappviewcontroller/requestpresentationstyle(_:).md)
  Asks the extension’s user interface to transition to the provided style.
- [func willTransition(to: MSMessagesAppPresentationStyle)](msmessagesappviewcontroller/willtransition(to:).md)
  Tells the view controller that the extension is about to transition to a new presentation style.
- [enum MSMessagesAppPresentationStyle](msmessagesapppresentationstyle.md)
  Presentation styles that describe your iMessage app’s appearance.
- [var presentationContext: MSMessagesAppPresentationContext](msmessagesappviewcontroller/presentationcontext.md)
  The context describing where your iMessage app is presented.
- [enum MSMessagesAppPresentationContext](msmessagesapppresentationcontext.md)
  Presentation contexts describing where your iMessage app appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/didtransition(to:))*