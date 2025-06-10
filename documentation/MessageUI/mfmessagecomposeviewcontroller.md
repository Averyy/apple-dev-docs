# MFMessageComposeViewController

**Framework**: Message UI  
**Kind**: class

A standard view controller whose interface lets the user compose and send SMS or MMS messages.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class MFMessageComposeViewController
```

#### Overview

Use an [`MFMessageComposeViewController`](mfmessagecomposeviewcontroller.md) object to display the standard message composition interface inside your app. Before presenting the interface, populate the fields with the set of initial recipients and the message you want to send. After presenting the interface, a person can edit your initial values before sending the message.

The composition interface doesn’t guarantee the delivery of your message; it only lets you construct the initial message and present it for a person’s approval. The person may opt to cancel the composition interface which discards the message and its contents. If the person opts to send the message, the Messages app takes on the responsibility of sending the message.

![a screenshot of the New Message screen, with a phone number in the To field and a short sentence in the composition text field.](https://docs-assets.developer.apple.com/published/e75d28ad3cf6ade12a7f581320e3a862/media-4288093%402x.png)

> ❗ **Important**:  You must not modify the view hierarchy presented by this view controller. However, you can customize the appearance of the interface using the [`UIAppearance`](https://developer.apple.com/documentation/UIKit/UIAppearance) protocol.

An alternate way to compose SMS messages is to create and open a URL that uses the `sms` scheme. URLs of that type go directly to the Messages app, which uses your URL to configure the message. For information about the structure of `sms` URLs, see [`Apple URL Scheme Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899).

##### Checking the Availability of the Composition Interface

Before presenting the message compose view controller, always call the [`canSendText()`](mfmessagecomposeviewcontroller/cansendtext().md) method to see if the person configured the current device to send messages. If the user’s device isn’t set up to send or receive messages, you can notify the user or disable the messaging features in your application. You shouldn’t attempt to use this interface if the [`canSendText()`](mfmessagecomposeviewcontroller/cansendtext().md) method returns [`false`](https://developer.apple.com/documentation/swift/false). If messaging is available, you can also use the [`canSendAttachments()`](mfmessagecomposeviewcontroller/cansendattachments().md) and [`canSendSubject()`](mfmessagecomposeviewcontroller/cansendsubject().md) methods to determine if those specific messaging features are available.

##### Configuring and Displaying the Composition Interface

After verifying that message services are available, you can create and configure the message composition view controller and then present it like any other view controller. Use the methods of this class to specify the message’s recipients and the contents of the message. If attachments or a subject line are supported, you can set values for them as well. The sample code below shows how to configure the composition interface and present it modally. Always assign a delegate to the [`messageComposeDelegate`](mfmessagecomposeviewcontroller/messagecomposedelegate.md) property, because the delegate is responsible for dismissing the composition interface later. The delegate object must conform to the [`MFMessageComposeViewControllerDelegate`](mfmessagecomposeviewcontrollerdelegate.md) protocol.

The message compose view controller isn’t dismissed automatically. When the user taps the buttons to send the message or cancel the interface, the message compose view controller calls the [`messageComposeViewController(_:didFinishWith:)`](mfmessagecomposeviewcontrollerdelegate/messagecomposeviewcontroller(_:didfinishwith:).md) method of its delegate. Your implementation of that method must dismiss the view controller explicitly, as shown in the sample code below. You can also use this method to check the result of the operation.

For more information on how to present and dismiss view controllers, see [`View Controller Programming Guide for iOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457).

##### Detecting Changes to the Availability of Messaging

Add an observer to the [`MFMessageComposeViewControllerTextMessageAvailabilityDidChange`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/MFMessageComposeViewControllerTextMessageAvailabilityDidChange) notification to get notified of changes to the messaging capabilities of the current device. The system delivers that notification to your observer when the status of messaging changes.

## Topics

### Responding to the view controller dismissal
- [var messageComposeDelegate: MFMessageComposeViewControllerDelegate?](mfmessagecomposeviewcontroller/messagecomposedelegate.md)
  The delegate to which message-related notifications should be sent.
- [protocol MFMessageComposeViewControllerDelegate](mfmessagecomposeviewcontrollerdelegate.md)
  An interface for responding to user interactions with a message compose view controller.
### Determining if message composition is available
- [class func canSendText() -> Bool](mfmessagecomposeviewcontroller/cansendtext.md)
  Returns a Boolean value that indicates whether the current device is capable of sending text messages.
- [class func canSendAttachments() -> Bool](mfmessagecomposeviewcontroller/cansendattachments.md)
  Indicates whether or not messages can include attachments.
- [class func canSendSubject() -> Bool](mfmessagecomposeviewcontroller/cansendsubject.md)
  Indicates whether or not messages can include subject lines, according to the user’s configuration in Settings.
- [class func isSupportedAttachmentUTI(String) -> Bool](mfmessagecomposeviewcontroller/issupportedattachmentuti(_:).md)
  Indicates whether or not the message can accept a file, with the specified UTI, as an attachment.
### Setting the initial message information
- [var recipients: [String]?](mfmessagecomposeviewcontroller/recipients.md)
  An array of strings that contains the initial recipients of the message.
- [var subject: String?](mfmessagecomposeviewcontroller/subject.md)
  The initial subject of the message.
- [var body: String?](mfmessagecomposeviewcontroller/body.md)
  The initial content of the message.
- [var message: MSMessage?](mfmessagecomposeviewcontroller/message.md)
  A message object from your iMessage app extension.
### Managing attachments
- [func disableUserAttachments()](mfmessagecomposeviewcontroller/disableuserattachments.md)
  Disables the camera/attachment button in the message composition view.
- [var attachments: [[AnyHashable : Any]]?](mfmessagecomposeviewcontroller/attachments.md)
  Returns an array of dictionaries that describe the properties of an attachment.
- [func addAttachmentURL(URL, withAlternateFilename: String?) -> Bool](mfmessagecomposeviewcontroller/addattachmenturl(_:withalternatefilename:).md)
  Attaches a specified file to the message.
- [func addAttachmentData(Data, typeIdentifier: String, filename: String) -> Bool](mfmessagecomposeviewcontroller/addattachmentdata(_:typeidentifier:filename:).md)
  Attaches arbitrary content to the message.
- [let MFMessageComposeViewControllerAttachmentURL: String](mfmessagecomposeviewcontrollerattachmenturl.md)
  The URL for the item that is attached to the message.
- [let MFMessageComposeViewControllerAttachmentAlternateFilename: String](mfmessagecomposeviewcontrollerattachmentalternatefilename.md)
  The key for the alternate filename for the file-based item attached to the message.
- [func insertCollaborationItemProvider(NSItemProvider) -> Bool](mfmessagecomposeviewcontroller/insertcollaborationitemprovider(_:).md)
### Handling notifications
- [static let MFMessageComposeViewControllerTextMessageAvailabilityDidChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/MFMessageComposeViewControllerTextMessageAvailabilityDidChange.md)
  Posted when the value returned by the [`canSendText()`](doc://com.apple.documentation/documentation/MessageUI/MFMessageComposeViewController/canSendText()) class method has changed.
- [let MFMessageComposeViewControllerTextMessageAvailabilityKey: String](mfmessagecomposeviewcontrollertextmessageavailabilitykey.md)
  The value of this key is a number object that contains a Boolean value.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller)*