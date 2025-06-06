# SMS and Call Spam Reporting

**Framework**: SMS and Call Reporting

Create an app extension that lets users report unwanted SMS messages and calls as junk.

#### Overview

To report SMS messages and calls as spam, the user must enable an Unwanted Communication Reporting extension, called an SMS/Call Reporting extension in the Settings app (see Settings > Phone > SMS/Call Reporting). The user can only enable one Unwanted Communication Reporting extension at a time.

In order to report calls, the user swipes left on an item in the Recents list and selects Report. For SMS messages, they press the Report Messages button when it appears in the Messages transcript. Users can also select messages by long-pressing a message and selecting additional messages, then selecting Report Messages.

When the user reports an SMS message or call, the system launches your Unwanted Communication Reporting extension. Your extension gathers additional information from the user, before deciding whether to report or block the number, as shown in the figure below.

![An illustration showing the system instantiating and displaying your view controller in response to the user reporting an SMS message or call.](https://docs-assets.developer.apple.com/published/7c5673dc5d2fb71f2cde19025ddbb865/media-3012154%402x.png)

Specifically, the system:

1. Instantiates your extension’s [`ILClassificationUIExtensionViewController`](https://developer.apple.com/documentation/identitylookupui/ilclassificationuiextensionviewcontroller) subclass.
2. Calls your controller’s [`prepare(for:)`](https://developer.apple.com/documentation/identitylookupui/ilclassificationuiextensionviewcontroller/prepare(for:)) method and presents the controller to the user.

Use your [`ILClassificationUIExtensionViewController`](https://developer.apple.com/documentation/identitylookupui/ilclassificationuiextensionviewcontroller) subclass to gather data from the user. Override the [`prepare(for:)`](https://developer.apple.com/documentation/identitylookupui/ilclassificationuiextensionviewcontroller/prepare(for:)) method to configure your controller.

##### Cancel or Complete the Report

The system provides a Cancel and a Done button for the controller. By default, the system disables the Done button. As soon as the user has entered all the information you require, enable the Done button by setting the view controller’s [`isReadyForClassificationResponse`](https://developer.apple.com/documentation/identitylookupui/ilclassificationuiextensioncontext/isreadyforclassificationresponse) property to [`true`](https://developer.apple.com/documentation/swift/true).

If the user presses the Cancel button, the system dismisses your view controller, as shown in the figure below.

![An illustration showing the user cancelling your view controller.](https://docs-assets.developer.apple.com/published/1ecc18e802ab0affc09424f1ada9ca61/media-3025730%402x.png)

If the user presses Done, the system calls your view controller’s [`classificationResponse(for:)`](https://developer.apple.com/documentation/identitylookupui/ilclassificationuiextensionviewcontroller/classificationresponse(for:)) method, passing in an [`ILClassificationRequest`](ilclassificationrequest.md) object (see the figure below).

![An illustration showing the user tapping the Done button after entering all the required information in your user interface.](https://docs-assets.developer.apple.com/published/5334663f6c15dba90dedfc6cc0bddf79/media-3025729%402x.png)

Override the [`classificationResponse(for:)`](https://developer.apple.com/documentation/identitylookupui/ilclassificationuiextensionviewcontroller/classificationresponse(for:)) method to return a [`ILClassificationResponse`](ilclassificationresponse.md) based on the data the user has entered and information about the SMS message or call from the request object.

##### Choose a Response

The system takes different actions based on the response. For [`ILClassificationAction.none`](ilclassificationaction/none.md), the system dismisses your view controller, but doesn’t take any other action, as shown in the figure below.

![A circle representing the System Response with a right-facing arrow that points to a rectangle representing an extension with view controller dismissed. That extension has a right-facing arrow that points to a rectangle representing an extension with Deleted for user privacy text. Below that is a dark version of the same diagram.](https://docs-assets.developer.apple.com/published/b75dbbc41d718c616079e1a600573eb3/media-3025747%402x.png)

For [`ILClassificationAction.reportNotJunk`](ilclassificationaction/reportnotjunk.md) or [`ILClassificationAction.reportJunk`](ilclassificationaction/reportjunk.md), the system generates a report based on your response’s [`action`](ilclassificationresponse/action.md) and [`userInfo`](ilclassificationresponse/userinfo.md) properties and then posts it to a network endpoint or sends it using an SMS message, depending on the keys specified in your extension’s `Info.plist` file.

To send a response over the network connection, you must add an associated domain to your extension. For general instructions, see [`Supporting associated domains`](https://developer.apple.com/documentation/Xcode/supporting-associated-domains). Note that you must use `classificationreport` instead of `webcredentials` when specifying the domains. You must also specify the network endpoint’s address using the `ILClassificationExtensionNetworkReportDestination` key in your extension’s `Info.plist` file.

To send your response using SMS, specify a fully qualified destination telephony number using the `ILClassificationExtensionSMSReportDestination` key in your extension’s `Info.plist` file. When your app uses this report path, the system displays the SMS message to give the user the opportunity to send or cancel the message.

When the report step is complete, the system dismisses your view controller and any view controllers related to it (see the figure below).

![A circle representing the System Response with a right-facing arrow that points to a device with Cancel or Send buttons. That device has a right-facing arrow that points to a rectangle representing an extension with a view controller with Cancel and Send buttons. That extension has a right-facing arrow that points to a rectangle representing an extension with Deleted for user privacy text. Below that is a dark version of the same diagram.](https://docs-assets.developer.apple.com/published/d4a77f4e3614400d09331fe8d0846261/media-3025725%402x.png)

For [`ILClassificationAction.reportJunkAndBlockSender`](ilclassificationaction/reportjunkandblocksender.md), the system responds just like in the [`ILClassificationAction.reportJunk`](ilclassificationaction/reportjunk.md) action. However, after the report step, the system presents an alert letting the user know the number will be blocked. Finally, the system blocks the SMS or call number, and dismisses your view controller as shown in the figure below.

![A circle representing the System Response with a right-facing arrow that points to a device with Cancel or Send buttons. That device has a right-facing arrow that points to another device showing Alert SMS/Call blocked text. That device has a right-facing arrow that points to a rectangle representing an extension with a view controller dismissed. That extension has a right-facing arrow that points to a rectangle representing an extension with Deleted for user privacy text. Below that is a dark version of the same diagram.](https://docs-assets.developer.apple.com/published/b9734e3fc56dc8828b13eeed3f5f3472/media-3025734%402x.png)

Blocked numbers are added to the device’s Blocked Contact list. Users can manage this list in the Settings app.

Finally, to protect user privacy, the system always deletes your extension’s container after your extension terminates. For more information, see [`About the iOS File System`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html#//apple_ref/doc/uid/TP40010672-CH2-SW12).

## Topics

### App Extension
- [class ILClassificationUIExtensionViewController](../identitylookupui/ilclassificationuiextensionviewcontroller.md)
  The superclass for an Unwanted Communication Reporting extension’s principal view controller.
### Communications
- [class ILCommunication](ilcommunication.md)
  An abstract superclass representing a message or call to the user.
- [class ILMessageCommunication](ilmessagecommunication.md)
  A concrete subclass representing a SMS message.
- [class ILCallCommunication](ilcallcommunication.md)
  A concrete subclass representing a  phone call.
### Requests
- [class ILClassificationRequest](ilclassificationrequest.md)
  The abstract superclass for classification requests.
- [class ILMessageClassificationRequest](ilmessageclassificationrequest.md)
  A classification request for SMS messages.
- [class ILCallClassificationRequest](ilcallclassificationrequest.md)
  A classification request for phone calls.
### Responses
- [class ILClassificationResponse](ilclassificationresponse.md)
  A response object that tells the system how to handle the reported communications.
- [enum ILClassificationAction](ilclassificationaction.md)
  The actions the system can take in response to the reported communication.
### Queries
- [class ILMessageFilterCapabilitiesQueryRequest](ilmessagefiltercapabilitiesqueryrequest.md)
  A request to query a Message Filter extension about sharing its sub-category capabilities.
- [protocol ILMessageFilterCapabilitiesQueryHandling](ilmessagefiltercapabilitiesqueryhandling.md)
  A set of methods implemented by a Message Filter app extension to handle capabilities query requests.
### Responses
- [class ILMessageFilterCapabilitiesQueryResponse](ilmessagefiltercapabilitiesqueryresponse.md)
  A response to a message filter capabilities query request.
- [enum ILMessageFilterSubAction](ilmessagefiltersubaction.md)
  Responds to a received message with a filter subaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/sms-and-call-spam-reporting)*