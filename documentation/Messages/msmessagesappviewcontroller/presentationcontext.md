# presentationContext

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

The context describing where your iMessage app is presented.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var presentationContext: MSMessagesAppPresentationContext { get }
```

```objc
@property (nonatomic, readonly) MSMessagesAppPresentationContext presentationContext;
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](../adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

#### Discussion

By default, the system only displays iMessage apps in the [`MSMessagesAppPresentationContext.messages`](../msmessagesapppresentationcontext/messages.md) context (the iMessage app only appears inside the Messages app). iMessage apps in the media context have additional limitations and design considerations.

You can control the supported contexts by adding the `MSSupportedPresentationContexts` key to the iMessage app extension’s `Info.plist` file. For example, [`presentationContext`](./presentationcontext.md) enables the iMessage app in effects in Messages and FaceTime.

```plist
<key>MSSupportedPresentationContexts</key>
<array>
  <string>MSMessagesAppPresentationContextMessages</string>
  <string>MSMessagesAppPresentationContextMedia</string>
</array>
```

## See Also

### Working with Presentation Styles and Contexts
- [var presentationStyle: MSMessagesAppPresentationStyle](./presentationstyle.md)
  The extension’s current presentation style.
- [func requestPresentationStyle(MSMessagesAppPresentationStyle)](./requestpresentationstyle%28_%29.md)
  Asks the extension’s user interface to transition to the provided style.
- [func willTransition(to: MSMessagesAppPresentationStyle)](./willtransition%28to%29.md)
  Tells the view controller that the extension is about to transition to a new presentation style.
- [func didTransition(to: MSMessagesAppPresentationStyle)](./didtransition%28to%29.md)
  Tells the view controller that the extension has transitioned to a new presentation style.
- [enum MSMessagesAppPresentationStyle](../msmessagesapppresentationstyle.md)
  Presentation styles that describe your iMessage app’s appearance.
- [enum MSMessagesAppPresentationContext](../msmessagesapppresentationcontext.md)
  Presentation contexts describing where your iMessage app appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/presentationcontext)*