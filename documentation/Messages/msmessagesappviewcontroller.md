# MSMessagesAppViewController

**Framework**: Messages  
**Kind**: class

The principal view controller for iMessage apps.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class MSMessagesAppViewController
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

#### Overview

Use this class to manage your extension. For more information on app extensions, see [`App Extension Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214).

## Topics

### Managing the Extension’s State
- [var activeConversation: MSConversation?](msmessagesappviewcontroller/activeconversation.md)
  The conversation currently displayed in the transcript.
- [func dismiss()](msmessagesappviewcontroller/dismiss.md)
  Dismisses the extension and marks it for termination.
- [func willBecomeActive(with: MSConversation)](msmessagesappviewcontroller/willbecomeactive(with:).md)
  Invoked just before the Messages extension becomes active.
- [func didBecomeActive(with: MSConversation)](msmessagesappviewcontroller/didbecomeactive(with:).md)
  Invoked after the Messages extension becomes active.
- [func willResignActive(with: MSConversation)](msmessagesappviewcontroller/willresignactive(with:).md)
  Invoked just before the message resigns its active status.
- [func didResignActive(with: MSConversation)](msmessagesappviewcontroller/didresignactive(with:).md)
  Invoked after the message resigns its active status.
### Tracking Messages
- [func willSelect(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/willselect(_:conversation:).md)
  Invoked in response to the user selecting a message object in the transcript, before the system updates the conversation’s [`selectedMessage`](msconversation/selectedmessage.md) property.
- [func didSelect(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didselect(_:conversation:).md)
  Invoked in response to the user selecting a message object in the transcript, after the system updates the conversation’s [`selectedMessage`](msconversation/selectedmessage.md) property.
- [func didReceive(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didreceive(_:conversation:).md)
  Invoked when the iMessage app receives a new message object.
- [func didStartSending(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didstartsending(_:conversation:).md)
  Invoked when the user sends a message object.
- [func didCancelSending(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didcancelsending(_:conversation:).md)
  Invoked when the user deletes a message object from the Messages app’s input field.
### Working with Presentation Styles and Contexts
- [var presentationStyle: MSMessagesAppPresentationStyle](msmessagesappviewcontroller/presentationstyle.md)
  The extension’s current presentation style.
- [func requestPresentationStyle(MSMessagesAppPresentationStyle)](msmessagesappviewcontroller/requestpresentationstyle(_:).md)
  Asks the extension’s user interface to transition to the provided style.
- [func willTransition(to: MSMessagesAppPresentationStyle)](msmessagesappviewcontroller/willtransition(to:).md)
  Tells the view controller that the extension is about to transition to a new presentation style.
- [func didTransition(to: MSMessagesAppPresentationStyle)](msmessagesappviewcontroller/didtransition(to:).md)
  Tells the view controller that the extension has transitioned to a new presentation style.
- [enum MSMessagesAppPresentationStyle](msmessagesapppresentationstyle.md)
  Presentation styles that describe your iMessage app’s appearance.
- [var presentationContext: MSMessagesAppPresentationContext](msmessagesappviewcontroller/presentationcontext.md)
  The context describing where your iMessage app is presented.
- [enum MSMessagesAppPresentationContext](msmessagesapppresentationcontext.md)
  Presentation contexts describing where your iMessage app appears.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MSMessagesAppTranscriptPresentation](msmessagesapptranscriptpresentation.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [IceCreamBuilder: Building an iMessage Extension](icecreambuilder-building-an-imessage-extension.md)
  Allow users to collaborate on the design of ice cream sundae stickers.
- [Creating a Sticker App with a Custom Layout](creating-a-sticker-app-with-a-custom-layout.md)
  Expand on the Messages sticker app template to create an app with a customized user interface.
- [protocol MSMessagesAppTranscriptPresentation](msmessagesapptranscriptpresentation.md)
  A protocol that provides support for displaying live messages in the transcript of the Messages app.
- [enum MSMessagesAppPresentationStyle](msmessagesapppresentationstyle.md)
  Presentation styles that describe your iMessage app’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller)*