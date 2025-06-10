# SMS and MMS Message Filtering

**Framework**: SMS and Call Reporting

Create an app extension that identifies and filters unwanted SMS and MMS messages while preserving user privacy.

#### Overview

When a user receives an SMS or MMS message from an unknown sender, the Messages app can ask your Message Filter app extension to determine whether the message is unsolicited or otherwise unwanted. Your app extension can make this determination by using its own built-in data and logic or by deferring to analysis done by your associated server.

> **Note**:  IdentityLookup works only with SMS and MMS messages from unknown senders; it doesn’t work with messages from senders in a user’s Contacts list or with iMessage messages from any source.

To find out if a message from an unknown sender is unwanted, the Messages app launches the currently enabled Message Filter app extension and queries it, as shown in the figure below.

![On the left, a box represents the Message Filter app extension in the containing app. On the right, a box shows an SMS or MMS message from an unknown sender coming in to the Messages app icon. Below the sets of boxes, on arrow indicates a query request coming from the message to the app, while another indicates the decision being sent back from the containing app to the Messages app. ](https://docs-assets.developer.apple.com/published/735a851d52c84c8b92c463348f6bbb6e/media-2994280%402x.png)

The Messages app uses an [`ILMessageFilterQueryRequest`](ilmessagefilterqueryrequest.md) object to pass information about the message to your Message Filter app extension. If your app extension can determine whether the message is unwanted, it returns its decision to Messages in an [`ILMessageFilterQueryResponse`](ilmessagefilterqueryresponse.md) object.

If your app extension can’t make this determination by itself, it tells Messages to send the information about the message to a server associated with your app. Your server examines the message information and sends a response to Messages, which passes the response to your app extension. The app extension parses the server’s response and returns the final decision to Messages in an [`ILMessageFilterQueryResponse`](ilmessagefilterqueryresponse.md) object, as shown in the figure below.

![On the left, a box represents the Message Filter app extension in the containing app. In the center, a box shows an SMS or MMS message from an unknown sender coming in to the Messages app icon. On the right, a box represents the Server associated with the app. Below the sets of boxes, on arrow indicates a query request coming from the message to the app, while another indicates the decision being sent back from the containing app to the Messages app. ](https://docs-assets.developer.apple.com/published/bb74d2a6d375628c8f818782249185fe/media-2994281%402x.png)

> **Note**:  For privacy reasons, the system handles all communication with your associated server; your Message Filter app extension can’t access the network directly. Your app extension also can’t write data to containers shared with the containing app.

## Topics

### First Steps
- [Creating a Message Filter App Extension](creating-a-message-filter-app-extension.md)
  Create an app extension that helps identify unwanted messages.
### App Extension
- [class ILMessageFilterExtensionContext](ilmessagefilterextensioncontext.md)
  The extension context for a Message Filter app extension.
- [class ILMessageFilterExtension](ilmessagefilterextension.md)
  The abstract base class for the principal class of a Message Filter app extension.
### Queries
- [class ILMessageFilterQueryRequest](ilmessagefilterqueryrequest.md)
  A request for a Message Filter app extension to determine the status of a message received from an unknown sender.
- [protocol ILMessageFilterQueryHandling](ilmessagefilterqueryhandling.md)
  A set of methods implemented by a Message Filter app extension to handle query requests.
### Responses
- [class ILMessageFilterQueryResponse](ilmessagefilterqueryresponse.md)
  A response to a message filter query request.
- [class ILNetworkResponse](ilnetworkresponse.md)
  A response to an HTTPS network request performed on behalf of a Message Filter app extension.
- [enum ILMessageFilterAction](ilmessagefilteraction.md)
  Responds to a received message with a filter action.
### Errors
- [struct ILMessageFilterError](ilmessagefiltererror-swift.struct.md)
  An error type that indicates problems with network requests and responses related to IdentityLookup APIs.
- [let ILMessageFilterErrorDomain: String](ilmessagefiltererrordomain.md)
  The error domain for errors associated with the IdentityLookup APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/sms-and-mms-message-filtering)*