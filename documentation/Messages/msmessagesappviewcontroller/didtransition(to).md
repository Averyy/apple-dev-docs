# didTransition(to:)

**Framework**: Messages  
**Kind**: method  
**Role**: Instance Method

Tells the view controller that the extension has transitioned to a new presentation style.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func didTransition(to presentationStyle: MSMessagesAppPresentationStyle)
```

```objc
- (void) didTransitionToPresentationStyle:(MSMessagesAppPresentationStyle) presentationStyle;
```

## Discussion

Override this method to respond after the extension’s user interface has transitioned to a new presentation style. The user can switch between styles by tapping the collapse and expand buttons in the Messages app. You can also programmatically trigger a transition by calling [`requestPresentationStyle(_:)`](./requestpresentationstyle%28_%29.md).

The system doesn’t call this method on a view controller that is presenting a live view in the transcript or input field—in other words, when the view controller’s [`presentationStyle`](./presentationstyle.md) property is set to the [`MSMessagesAppPresentationStyle.transcript`](../msmessagesapppresentationstyle/transcript.md) value.

## Parameters

- `presentationStyle`: The new presentation style. For a list of possible styles, see [`MSMessagesAppPresentationStyle`](../msmessagesapppresentationstyle.md).

## See Also

### Working with Presentation Styles and Contexts
- [var presentationStyle: MSMessagesAppPresentationStyle](./presentationstyle.md)
  The extension’s current presentation style.
- [func requestPresentationStyle(MSMessagesAppPresentationStyle)](./requestpresentationstyle%28_%29.md)
  Asks the extension’s user interface to transition to the provided style.
- [func willTransition(to: MSMessagesAppPresentationStyle)](./willtransition%28to%29.md)
  Tells the view controller that the extension is about to transition to a new presentation style.
- [enum MSMessagesAppPresentationStyle](../msmessagesapppresentationstyle.md)
  Presentation styles that describe your iMessage app’s appearance.
- [var presentationContext: MSMessagesAppPresentationContext](./presentationcontext.md)
  The context describing where your iMessage app is presented.
- [enum MSMessagesAppPresentationContext](../msmessagesapppresentationcontext.md)
  Presentation contexts describing where your iMessage app appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/didtransition(to:))*