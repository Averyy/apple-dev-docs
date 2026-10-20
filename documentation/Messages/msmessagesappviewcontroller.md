# MSMessagesAppViewController

**Framework**: Messages  
**Kind**: class  
**Role**: Class

The principal view controller for iMessage apps.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MSMessagesAppViewController
```

```objc
@interface MSMessagesAppViewController : UIViewController
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](./adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

#### Overview

Use this class to manage your extension. For more information on app extensions, see [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214).

## Topics

### Managing the Extension’s State
- [var activeConversation: MSConversation?](./msmessagesappviewcontroller/activeconversation.md)
  The conversation currently displayed in the transcript.
- [func dismiss()](./msmessagesappviewcontroller/dismiss%28%29.md)
  Dismisses the extension and marks it for termination.
- [func willBecomeActive(with: MSConversation)](./msmessagesappviewcontroller/willbecomeactive%28with%29.md)
  Invoked just before the Messages extension becomes active.
- [func didBecomeActive(with: MSConversation)](./msmessagesappviewcontroller/didbecomeactive%28with%29.md)
  Invoked after the Messages extension becomes active.
- [func willResignActive(with: MSConversation)](./msmessagesappviewcontroller/willresignactive%28with%29.md)
  Invoked just before the message resigns its active status.
- [func didResignActive(with: MSConversation)](./msmessagesappviewcontroller/didresignactive%28with%29.md)
  Invoked after the message resigns its active status.
### Tracking Messages
- [func willSelect(MSMessage, conversation: MSConversation)](./msmessagesappviewcontroller/willselect%28_,conversation%29.md)
  Invoked in response to the user selecting a message object in the transcript, before the system updates the conversation’s [`selectedMessage`](./msconversation/selectedmessage.md) property.
- [func didSelect(MSMessage, conversation: MSConversation)](./msmessagesappviewcontroller/didselect%28_,conversation%29.md)
  Invoked in response to the user selecting a message object in the transcript, after the system updates the conversation’s [`selectedMessage`](./msconversation/selectedmessage.md) property.
- [func didReceive(MSMessage, conversation: MSConversation)](./msmessagesappviewcontroller/didreceive%28_,conversation%29.md)
  Invoked when the iMessage app receives a new message object.
- [func didStartSending(MSMessage, conversation: MSConversation)](./msmessagesappviewcontroller/didstartsending%28_,conversation%29.md)
  Invoked when the user sends a message object.
- [func didCancelSending(MSMessage, conversation: MSConversation)](./msmessagesappviewcontroller/didcancelsending%28_,conversation%29.md)
  Invoked when the user deletes a message object from the Messages app’s input field.
### Working with Presentation Styles and Contexts
- [var presentationStyle: MSMessagesAppPresentationStyle](./msmessagesappviewcontroller/presentationstyle.md)
  The extension’s current presentation style.
- [func requestPresentationStyle(MSMessagesAppPresentationStyle)](./msmessagesappviewcontroller/requestpresentationstyle%28_%29.md)
  Asks the extension’s user interface to transition to the provided style.
- [func willTransition(to: MSMessagesAppPresentationStyle)](./msmessagesappviewcontroller/willtransition%28to%29.md)
  Tells the view controller that the extension is about to transition to a new presentation style.
- [func didTransition(to: MSMessagesAppPresentationStyle)](./msmessagesappviewcontroller/didtransition%28to%29.md)
  Tells the view controller that the extension has transitioned to a new presentation style.
- [enum MSMessagesAppPresentationStyle](./msmessagesapppresentationstyle.md)
  Presentation styles that describe your iMessage app’s appearance.
- [var presentationContext: MSMessagesAppPresentationContext](./msmessagesappviewcontroller/presentationcontext.md)
  The context describing where your iMessage app is presented.
- [enum MSMessagesAppPresentationContext](./msmessagesapppresentationcontext.md)
  Presentation contexts describing where your iMessage app appears.

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MSMessagesAppTranscriptPresentation](./msmessagesapptranscriptpresentation.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Custom iMessage app interface
- [IceCreamBuilder: Building an iMessage Extension](./icecreambuilder-building-an-imessage-extension.md)
  Allow users to collaborate on the design of ice cream sundae stickers.
- [Creating a Sticker App with a Custom Layout](./creating-a-sticker-app-with-a-custom-layout.md)
  Expand on the Messages sticker app template to create an app with a customized user interface.
- [protocol MSMessagesAppTranscriptPresentation](./msmessagesapptranscriptpresentation.md)
  A protocol that provides support for displaying live messages in the transcript of the Messages app.
- [enum MSMessagesAppPresentationStyle](./msmessagesapppresentationstyle.md)
  Presentation styles that describe your iMessage app’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller)*