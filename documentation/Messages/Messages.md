# Messages

**Framework**: Messages  
**Kind**: module

Create app extensions that allow users to send text, stickers, media files, and interactive messages.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+

#### Overview

You can use the Messages framework to create sticker packs and iMessage apps. You can create sticker packs and iMessage apps as either standalone apps or as app extensions within a containing iOS app. For more information on creating and working with app extensions, see [`App extensions`](https://developer.apple.comhttps://developer.apple.com/app-extensions/).

iMessage apps and stickers help people interact and communicate in the context of a Messages conversation. For design guidance, see [`Human Interface Guidelines > iMessage apps and stickers`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers).

##### Imessage Apps

iMessage apps leverage the full framework to interact with the Messages app.

> **Note**:  To avoid a crash, an iMessage app linked on or after iOS 10 must include usage description keys for the device features it needs to access in its `Info.plist` file. Specifically, it must include [`NSCameraUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCameraUsageDescription) to access the device’s camera, and it must include [`NSMicrophoneUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMicrophoneUsageDescription) to access the device’s microphones.

Use iMessage apps to:

- Present a custom user interface inside the Messages app; see [`MSMessagesAppViewController`](msmessagesappviewcontroller.md).
- Create a custom or dynamic sticker browser; see [`MSStickerBrowserViewController`](msstickerbrowserviewcontroller.md).
- Insert text, stickers, or media files into the Messages app’s input field; see [`MSConversation`](msconversation.md).
- Create interactive messages that carry app-specific data; see [`MSMessage`](msmessage.md).
- Update interactive messages (for example, to create games or collaborative apps); see [`MSSession`](mssession.md).

For more information on submitting iMessage Apps to the App Store, see [`Preparing Your iMessage App for Submission`](https://developer.apple.comhttps://developer.apple.com/app-store/imessage-app-submissions/).

In iOS 17, Messages allows you to interactively resize iMessage apps with a vertical pan gesture. Messages handles any conflicts between resize gestures and your custom gestures. If your app uses manual touch handling such as [`touchesBegan(_:with:)`](https://developer.apple.com/documentation/UIKit/UIGestureRecognizer/touchesBegan(_:with:)), [`touchesMoved(_:with:)`](https://developer.apple.com/documentation/UIKit/UIGestureRecognizer/touchesMoved(_:with:)), and [`touchesEnded(_:with:)`](https://developer.apple.com/documentation/UIKit/UIGestureRecognizer/touchesEnded(_:with:)), you can do either of the following:

- Change your manual touch handling code to use a gesture recognizer instead.
- Use your [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) to override [`gestureRecognizerShouldBegin(_:)`](https://developer.apple.com/documentation/UIKit/UIGestureRecognizerDelegate/gestureRecognizerShouldBegin(_:)) and return `NO` when your iMessage app doesn’t own the gesture.

##### Become the Default Messaging App

In iOS and iPadOS 18.2 and later, a person may select an app other than the Messages app to send instant messages. If you wish to make your app the default messages app, see [`Preparing your app to be the default messaging app`](preparing-your-app-to-be-the-default-messaging-app.md).

## Topics

### Default messaging app
- [Preparing your app to be the default messaging app](preparing-your-app-to-be-the-default-messaging-app.md)
  Configure your messaging app so people can set it as the default on their device.
### Custom sticker packs
- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)
  Enable your Sticker pack or iMessage app in the media context.
- [Adding your sticker packs to Messages](adding-your-sticker-packs-to-messages.md)
  Drag and drop your sticker pack into the Stickers asset catalog to let people access your stickers from Messages.
- [class MSStickerBrowserViewController](msstickerbrowserviewcontroller.md)
  A view controller that provides dynamic content to the standard sticker browser.
- [class MSStickerBrowserView](msstickerbrowserview.md)
  A browser view that displays a dynamically generated list of stickers.
- [class MSStickerView](msstickerview.md)
  A view for displaying a sticker.
- [enum MSStickerSize](msstickersize.md)
  The size of the stickers in the browser view.
### Custom iMessage app interface
- [IceCreamBuilder: Building an iMessage Extension](icecreambuilder-building-an-imessage-extension.md)
  Allow users to collaborate on the design of ice cream sundae stickers.
- [Creating a Sticker App with a Custom Layout](creating-a-sticker-app-with-a-custom-layout.md)
  Expand on the Messages sticker app template to create an app with a customized user interface.
- [class MSMessagesAppViewController](msmessagesappviewcontroller.md)
  The principal view controller for iMessage apps.
- [protocol MSMessagesAppTranscriptPresentation](msmessagesapptranscriptpresentation.md)
  A protocol that provides support for displaying live messages in the transcript of the Messages app.
- [enum MSMessagesAppPresentationStyle](msmessagesapppresentationstyle.md)
  Presentation styles that describe your iMessage app’s appearance.
### Message content
- [class MSConversation](msconversation.md)
  An object that represents a conversation in the Messages app.
- [class MSSticker](mssticker.md)
  A sticker that can be sent as a new message or attached to an existing balloon in the Messages app’s  transcript.
### Interactive messages
- [class MSMessage](msmessage.md)
  A custom message object.
- [class MSSession](mssession.md)
  A session object used to create and update messages.
- [class MSMessageLayout](msmessagelayout.md)
  An abstract base class that defines the appearance of [`MSMessage`](msmessage.md) objects in the conversation transcript.
- [class MSMessageTemplateLayout](msmessagetemplatelayout.md)
  A template-based layout for custom messages.
- [class MSMessageLiveLayout](msmessagelivelayout.md)
  A layout that provides a custom, interactive view inside the transcript.
### Critical messages
- [Sending SMS messages from an app](critical-messaging-api.md)
  Send critical messages from inside your app using the Critical Messaging API.
- [class MSCriticalSMSMessenger](mscriticalsmsmessenger.md)
  The user interface for the Critical Messaging API.
- [struct MSRecipient](msrecipient.md)
  A structure that describes the recipient of a critical message.
- [struct MSCriticalMessage](mscriticalmessage.md)
  MSCriticalMessage A simple struct to encapsulate the message string.
- [enum MSCriticalMessagingAuthorizationStatus](mscriticalmessagingauthorizationstatus.md)
  Values that describe the authorization status for the Critical Messaging API.
### Errors
- [let MSStickersErrorDomain: String](msstickerserrordomain.md)
  The error domain for stickers.
- [let MSMessagesErrorDomain: String](msmessageserrordomain.md)
  The error domain for iMessage apps.
- [enum MSMessageErrorCode](msmessageerrorcode.md)
  The error codes that the Messages framework generates.
- [enum MSCriticalMessagingError](mscriticalmessagingerror.md)
  Values that describe errors the Critical Messaging API returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Messages)*