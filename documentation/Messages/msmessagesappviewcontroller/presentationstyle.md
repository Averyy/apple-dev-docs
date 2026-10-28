# presentationStyle

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

The extension’s current presentation style.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var presentationStyle: MSMessagesAppPresentationStyle { get }
```

```objc
@property (nonatomic, assign, readonly) MSMessagesAppPresentationStyle presentationStyle;
```

## Discussion

The presentation style defines how the extension appears in the Messages app. The property’s value is set by the following actions:

- The user selects the extension in the app drawer: The Messages app launches the extension using the [`MSMessagesAppPresentationStyle.compact`](../msmessagesapppresentationstyle/compact.md) style.
- The user selects a message in the transcript that represents one of the extension’s [`MSMessage`](../msmessage.md) objects: The Messages app launches the extension using the [`MSMessagesAppPresentationStyle.expanded`](../msmessagesapppresentationstyle/expanded.md) style.
- The user taps the collapse and expand buttons while the extension is running: The Messages app changes the current presentation style.
- You programmatically set the presentation style by calling the [`requestPresentationStyle(_:)`](./requestpresentationstyle%28_%29.md) method.

## See Also

### Working with Presentation Styles and Contexts
- [func requestPresentationStyle(MSMessagesAppPresentationStyle)](./requestpresentationstyle%28_%29.md)
  Asks the extension’s user interface to transition to the provided style.
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

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/presentationstyle)*