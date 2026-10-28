# requestPresentationStyle(_:)

**Framework**: Messages  
**Kind**: method  
**Role**: Instance Method

Asks the extension’s user interface to transition to the provided style.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func requestPresentationStyle(_ presentationStyle: MSMessagesAppPresentationStyle)
```

```objc
- (void) requestPresentationStyle:(MSMessagesAppPresentationStyle) presentationStyle;
```

## Discussion

Use this method when you need to change the extension’s presentation style. Keep in mind that the user should have ultimate control over the extension’s presentation style. If the user chooses to change the presentation style, you want to respect that choice.

> ❗ **Important**:  You cannot pass the [`MSMessagesAppPresentationStyle.transcript`](../msmessagesapppresentationstyle/transcript.md) presentation style to this method.

If you call this method on a view controller with a [`MSMessagesAppPresentationStyle.transcript`](../msmessagesapppresentationstyle/transcript.md) presentation style (which is a controller that’s presenting an interactive view in the transcript), the system creates a new instance of the view controller and displays it using the provided presentation style.

## Parameters

- `presentationStyle`: The desired presentation style. For a list of possible styles, see [`MSMessagesAppPresentationStyle`](../msmessagesapppresentationstyle.md).

## See Also

### Working with Presentation Styles and Contexts
- [var presentationStyle: MSMessagesAppPresentationStyle](./presentationstyle.md)
  The extension’s current presentation style.
- [func willTransition(to: MSMessagesAppPresentationStyle)](./willtransition%28to%29.md)
  Tells the view controller that the extension is about to transition to a new presentation style.
- [func didTransition(to: MSMessagesAppPresentationStyle)](./didtransition%28to%29.md)
  Tells the view controller that the extension has transitioned to a new presentation style.
- [enum MSMessagesAppPresentationStyle](../msmessagesapppresentationstyle.md)
  Presentation styles that describe your iMessage app’s appearance.
- [var presentationContext: MSMessagesAppPresentationContext](./presentationcontext.md)
  The context describing where your iMessage app is presented.
- [enum MSMessagesAppPresentationContext](../msmessagesapppresentationcontext.md)
  Presentation contexts describing where your iMessage app appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/requestpresentationstyle(_:))*