# MFMessageComposeViewController

**Framework**: Message UI  
**Kind**: class  
**Role**: Class

A standard view controller whose interface lets the user compose and send SMS or MMS messages.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MFMessageComposeViewController
```

```objc
@interface MFMessageComposeViewController : UINavigationController
```

## Overview

Use an [`MFMessageComposeViewController`](./mfmessagecomposeviewcontroller.md) object to display the standard message composition interface inside your app. Before presenting the interface, populate the fields with the set of initial recipients and the message you want to send. After presenting the interface, a person can edit your initial values before sending the message.

The composition interface doesn’t guarantee the delivery of your message; it only lets you construct the initial message and present it for a person’s approval. The person may opt to cancel the composition interface which discards the message and its contents. If the person opts to send the message, the Messages app takes on the responsibility of sending the message.

![a screenshot of the New Message screen, with a phone number in the To field and a short sentence in the composition text field.](https://developer.apple.com/tutorials/images/com.apple.messageui/media-4288093@2x.png)

> ❗ **Important**:  You must not modify the view hierarchy presented by this view controller. However, you can customize the appearance of the interface using the [`UIAppearance`](../UIKit/uiappearance.md) protocol.

An alternate way to compose SMS messages is to create and open a URL that uses the `sms` scheme. URLs of that type go directly to the Messages app, which uses your URL to configure the message. For information about the structure of `sms` URLs, see [Apple URL Scheme Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899).

### Checking the availability of the composition interface

Before presenting the message compose view controller, always call the [`canSendText()`](./mfmessagecomposeviewcontroller/cansendtext%28%29.md) method to see if the person configured the current device to send messages. If the user’s device isn’t set up to send or receive messages, you can notify the user or disable the messaging features in your application. You shouldn’t attempt to use this interface if the [`canSendText()`](./mfmessagecomposeviewcontroller/cansendtext%28%29.md) method returns [`false`](../Swift/false.md). If messaging is available, you can also use the [`canSendAttachments()`](./mfmessagecomposeviewcontroller/cansendattachments%28%29.md) and [`canSendSubject()`](./mfmessagecomposeviewcontroller/cansendsubject%28%29.md) methods to determine if those specific messaging features are available.

**Swift**:

```swift
if !MFMessageComposeViewController.canSendText() {
    print("SMS services are not available")
}

```

**Obj-C**:

```objc
if (![MFMessageComposeViewController canSendText]) {
   NSLog(@"Message services are not available.");
}
```

### Configuring and displaying the composition interface

After verifying that message services are available, you can create and configure the message composition view controller and then present it like any other view controller. Use the methods of this class to specify the message’s recipients and the contents of the message. If attachments or a subject line are supported, you can set values for them as well. The sample code below shows how to configure the composition interface and present it modally. Always assign a delegate to the [`messageComposeDelegate`](./mfmessagecomposeviewcontroller/messagecomposedelegate.md) property, because the delegate is responsible for dismissing the composition interface later. The delegate object must conform to the [`MFMessageComposeViewControllerDelegate`](./mfmessagecomposeviewcontrollerdelegate.md) protocol.

**Swift**:

```swift
let composeVC = MFMessageComposeViewController()
composeVC.messageComposeDelegate = self
 
// Configure the fields of the interface.
composeVC.recipients = ["4085551212"]
composeVC.body = "Hello from California!"
 
// Present the view controller modally.
self.present(composeVC, animated: true, completion: nil)

```

**Obj-C**:

```objc
MFMessageComposeViewController* composeVC = [[MFMessageComposeViewController alloc] init];
composeVC.messageComposeDelegate = self;
 
// Configure the fields of the interface.
composeVC.recipients = @[@"14085551212"];
composeVC.body = @"Hello from California!";
 
// Present the view controller modally.
[self present:composeVC animated:YES completion:nil];

```

The message compose view controller isn’t dismissed automatically. When the user taps the buttons to send the message or cancel the interface, the message compose view controller calls the [`messageComposeViewController(_:didFinishWith:)`](./mfmessagecomposeviewcontrollerdelegate/messagecomposeviewcontroller%28_,didfinishwith%29.md) method of its delegate. Your implementation of that method must dismiss the view controller explicitly, as shown in the sample code below. You can also use this method to check the result of the operation.

**Swift**:

```swift
func messageComposeViewController(controller: MFMessageComposeViewController,
                                  didFinishWithResult result: MessageComposeResult) {
    // Check the result or perform other tasks.
    
    // Dismiss the message compose view controller.
    controller.dismissViewControllerAnimated(true, completion: nil)}

```

**Obj-C**:

```objc
- (void)messageComposeViewController:(MFMessageComposeViewController *)controller
                 didFinishWithResult:(MessageComposeResult)result {
   // Check the result or perform other tasks.    // Dismiss the message compose view controller.
   [self dismissViewControllerAnimated:YES completion:nil];}

```

For more information on how to present and dismiss view controllers, see [View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457).

### Detecting changes to the availability of messaging

Add an observer to the [`MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification`](./mfmessagecomposeviewcontrollertextmessageavailabilitydidchangenotification.md) notification to get notified of changes to the messaging capabilities of the current device. The system delivers that notification to your observer when the status of messaging changes.

## Topics

### Responding to the view controller dismissal
- [var messageComposeDelegate: (any MFMessageComposeViewControllerDelegate)?](./mfmessagecomposeviewcontroller/messagecomposedelegate.md)
  The delegate to which message-related notifications should be sent.
- [protocol MFMessageComposeViewControllerDelegate](./mfmessagecomposeviewcontrollerdelegate.md)
  An interface for responding to user interactions with a message compose view controller.
### Determining if message composition is available
- [class func canSendText() -> Bool](./mfmessagecomposeviewcontroller/cansendtext%28%29.md)
  Returns a Boolean value that indicates whether the current device is capable of sending text messages.
- [class func canSendAttachments() -> Bool](./mfmessagecomposeviewcontroller/cansendattachments%28%29.md)
  Indicates whether or not messages can include attachments.
- [class func canSendSubject() -> Bool](./mfmessagecomposeviewcontroller/cansendsubject%28%29.md)
  Indicates whether or not messages can include subject lines, according to the user’s configuration in Settings.
- [class func isSupportedAttachmentUTI(String) -> Bool](./mfmessagecomposeviewcontroller/issupportedattachmentuti%28_%29.md)
  Indicates whether or not the message can accept a file, with the specified UTI, as an attachment.
### Setting the initial message information
- [var recipients: [String]?](./mfmessagecomposeviewcontroller/recipients.md)
  An array of strings that contains the initial recipients of the message.
- [var subject: String?](./mfmessagecomposeviewcontroller/subject.md)
  The initial subject of the message.
- [var body: String?](./mfmessagecomposeviewcontroller/body.md)
  The initial content of the message.
- [var message: MSMessage?](./mfmessagecomposeviewcontroller/message.md)
  A message object from your iMessage app extension.
### Managing attachments
- [func disableUserAttachments()](./mfmessagecomposeviewcontroller/disableuserattachments%28%29.md)
  Disables the camera/attachment button in the message composition view.
- [var attachments: [[AnyHashable : Any]]?](./mfmessagecomposeviewcontroller/attachments.md)
  Returns an array of dictionaries that describe the properties of an attachment.
- [func addAttachmentURL(URL, withAlternateFilename: String?) -> Bool](./mfmessagecomposeviewcontroller/addattachmenturl%28_,withalternatefilename%29.md)
  Attaches a specified file to the message.
- [func addAttachmentData(Data, typeIdentifier: String, filename: String) -> Bool](./mfmessagecomposeviewcontroller/addattachmentdata%28_,typeidentifier,filename%29.md)
  Attaches arbitrary content to the message.
- [let MFMessageComposeViewControllerAttachmentURL: String](./mfmessagecomposeviewcontrollerattachmenturl.md)
  The URL for the item that is attached to the message.
- [let MFMessageComposeViewControllerAttachmentAlternateFilename: String](./mfmessagecomposeviewcontrollerattachmentalternatefilename.md)
  The key for the alternate filename for the file-based item attached to the message.
- [func insertCollaborationItemProvider(NSItemProvider) -> Bool](./mfmessagecomposeviewcontroller/insertcollaborationitemprovider%28_%29.md)
### Handling notifications
- [let MFMessageComposeViewControllerTextMessageAvailabilityKey: String](./mfmessagecomposeviewcontrollertextmessageavailabilitykey.md)
  The value of this key is a number object that contains a Boolean value.
- [MFMessageComposeViewControllerTextMessageAvailabilityDidChangeNotification](./mfmessagecomposeviewcontrollertextmessageavailabilitydidchangenotification.md)
  Posted when the value returned by the [`canSendText`](./mfmessagecomposeviewcontroller/cansendtext%28%29.md) class method has changed.
### Configuring device validation
- [func setUPIVerificationCodeSendCompletion((Bool) -> Void)](./mfmessagecomposeviewcontroller/setupiverificationcodesendcompletion%28_%29.md)
  Configures the instance of a view for Unified Payments Interface (UPI) device validation.
### Structures
- [MFMessageComposeViewController.TextMessageAvailabilityDidChangeMessage](./mfmessagecomposeviewcontroller/textmessageavailabilitydidchangemessage.md)
  Message type for text message availability change notifications.

## Relationships

### Inherits From
- [UINavigationController](../UIKit/uinavigationcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller)*