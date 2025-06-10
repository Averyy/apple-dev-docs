# MFMailComposeViewController

**Framework**: Message UI  
**Kind**: class

A standard view controller, whose interface lets the user manage, edit, and send email messages.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class MFMailComposeViewController
```

#### Overview

Use this view controller to display a standard email interface inside your app. Before presenting the interface, populate the fields with initial values for the subject, email recipients, body text, and attachments of the email. After presenting the interface, the person can edit your initial values before sending the email.

The composition interface doesn’t guarantee the delivery of your email message; it only lets you construct the initial message and present it for user approval. The person may opt to cancel the composition interface which discards the message and its contents. If the person opts to send the message, the message queues in the user’s Mail app outbox. The Mail app is ultimately responsible for sending the message.

![Screenshot of the email composition view in Mail, indicating the fields for recipients, subject, and body. ](https://docs-assets.developer.apple.com/published/a4e2bdda7e18fb7a247132800fdb87e8/media-4288076%402x.png)

> ❗ **Important**:  You must not modify the view hierarchy presented by this view controller. However, you can customize the appearance of the interface using the [`UIAppearance`](https://developer.apple.com/documentation/UIKit/UIAppearance) protocol.

An alternate way to compose emails is to create and open a URL that uses the `mailto` scheme. URLs of that type go directly to the built-in Mail app, which uses your URL to configure a message. For information about the structure of `mailto` URLs, see [`Apple URL Scheme Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899).

##### Checking the Availability of the Composition Interface

Before presenting the mail compose view controller, always call the [`canSendMail()`](mfmailcomposeviewcontroller/cansendmail().md) method to see if the person configured the current device to send email. If the person’s device isn’t set up for the delivery of email, you can notify the person or disable the email dispatch features in your application. You shouldn’t attempt to use this interface if the [`canSendMail()`](mfmailcomposeviewcontroller/cansendmail().md) method returns [`false`](https://developer.apple.com/documentation/swift/false).

##### Configuring and Displaying the Composition Interface

After verifying that mail services are available, you can create and configure the mail composition view controller and then present it as any other view controller. Use the methods of this class to specify the subject, recipients, and message body of the email, including any attachments you want to send with the message. The sample code below shows how to configure the composition interface and present it modally. Always assign a delegate to the [`mailComposeDelegate`](mfmailcomposeviewcontroller/mailcomposedelegate.md) property, because the delegate is responsible for dismissing the composition interface later.

> ❗ **Important**:  After presenting a mail compose view controller, the system ignores any attempts to modify the email using the methods of this class. The user can still edit the content of the email, but your app can’t. Therefore, always configure the fields of your email  presenting the view controller.

The mail compose view controller isn’t dismissed automatically. When the user taps the buttons to send the email or cancel the interface, the mail compose view controller calls the [`mailComposeController(_:didFinishWith:error:)`](mfmailcomposeviewcontrollerdelegate/mailcomposecontroller(_:didfinishwith:error:).md) method of its delegate. Your implementation of that method must dismiss the view controller explicitly, as shown in sample code below. You can also use this method to check the result of the operation.

The user can delete a queued message before it’s sent. Although the view controller reports the success or failure of the operation to its delegate, this class doesn’t provide a way for you to verify if the email sent.

For more information on how to present and dismiss view controllers, see [`View Controller Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457).

## Topics

### Responding to the view controller dismissal
- [var mailComposeDelegate: MFMailComposeViewControllerDelegate?](mfmailcomposeviewcontroller/mailcomposedelegate.md)
  The mail composition view controller’s delegate.
- [protocol MFMailComposeViewControllerDelegate](mfmailcomposeviewcontrollerdelegate.md)
  An interface for responding to user interactions with a mail compose view controller.
### Determining mail availability
- [class func canSendMail() -> Bool](mfmailcomposeviewcontroller/cansendmail.md)
  Returns a Boolean that indicates whether the current device is able to send email.
### Setting mail fields programmatically
- [func setSubject(String)](mfmailcomposeviewcontroller/setsubject(_:).md)
  Sets the initial text for the subject line of the email.
- [func setToRecipients([String]?)](mfmailcomposeviewcontroller/settorecipients(_:).md)
  Sets the initial recipients to include in the email’s To field.
- [func setCcRecipients([String]?)](mfmailcomposeviewcontroller/setccrecipients(_:).md)
  Sets the initial recipients to include in the email’s Cc field.
- [func setBccRecipients([String]?)](mfmailcomposeviewcontroller/setbccrecipients(_:).md)
  Sets the initial recipients to include in the email’s Bcc field.
- [func setMessageBody(String, isHTML: Bool)](mfmailcomposeviewcontroller/setmessagebody(_:ishtml:).md)
  Sets the initial body text to include in the email.
- [func addAttachmentData(Data, mimeType: String, fileName: String)](mfmailcomposeviewcontroller/addattachmentdata(_:mimetype:filename:).md)
  Adds the specified data as an attachment to the message.
- [func setPreferredSendingEmailAddress(String)](mfmailcomposeviewcontroller/setpreferredsendingemailaddress(_:).md)
  Sets the preferred email address to use in the From field, if such an address is available.
### Responding to errors
- [struct MFMailComposeError](mfmailcomposeerror.md)
  Mail composition errors.
- [let MFMailComposeErrorDomain: String](mfmailcomposeerrordomain.md)
  The domain used for error objects that are associated with the mail composition interface.
- [MFMailComposeError.Code](mfmailcomposeerror/code.md)
  Error codes for [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) objects that are associated with the mail composition interface.
### Instance Methods
- [func insertCollaborationItemProvider(NSItemProvider, completionHandler: (Bool) -> Void)](mfmailcomposeviewcontroller/insertcollaborationitemprovider(_:completionhandler:).md)

## Relationships

### Inherits From
- [UINavigationController](../UIKit/UINavigationController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller)*