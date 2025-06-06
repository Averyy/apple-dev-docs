# MSSession

**Framework**: Messages  
**Kind**: class

A session object used to create and update messages.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MSSession
```

#### Overview

> **Note**:  The [`MSSession`](mssession.md) class does not declare any instance methods or properties. iMessage apps use [`MSSession`](mssession.md) objects to identify and track updatable messages.

[`MSMessage`](msmessage.md) objects associated with a session receive the following treatment in the transcript:

- The first time a session is used, the message appears normally in the transcript.
- If a later message is sent using the same session, the previous message is removed from the transcript. The new message, with the updated content, is added to the bottom of the transcript, as normal.
- If the previous message has a non-`nil` [`summaryText`](msmessage/summarytext.md) property, the Messages app creates a summary message from the text and inserts it in the message’s previous location.

##### Create New Updatable Messages

Use the following workflow to create a new, updatable message.

1. Create the following:

- A new URL that encodes the message’s initial state. For example, you could encode data as key-value pairs in the URL’s query string. For more information, see the [`MSMessage`](msmessage.md) class’s [`url`](msmessage/url.md) property.
- A new layout object that describes the initial message’s appearance. For more information, see the [`MSMessage`](msmessage.md) class’s [`layout`](msmessage/layout.md) property.
- A string that describes the message’s current state. For more information, see the [`MSMessage`](msmessage.md) class’s [`summaryText`](msmessage/summarytext.md) property.

1. Instantiate a new [`MSSession`](mssession.md) object by calling its [`init()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/init()) method.
2. Instantiate a new [`MSMessage`](msmessage.md) object by calling its [`init(session:)`](msmessage/init(session:).md) method and passing the session object. Set the message’s [`url`](msmessage/url.md), [`layout`](msmessage/layout.md), and [`summaryText`](msmessage/summarytext.md) properties.
3. Send the message by calling the conversation’s [`insert(_:completionHandler:)`](msconversation/insert(_:completionhandler:)-3g248.md) method. Pass `nil` for the change description.

The Messages app adds the message to the transcript as soon as the user taps the send button.

##### Update Messages

Use the following workflow to receive and update a message.

1. When the user taps on one of your [`MSMessage`](msmessage.md) entries, the conversation’s [`selectedMessage`](msconversation/selectedmessage.md) property is changed to the tapped message. Use key-value observing to respond to these changes. Extract the current state from the message’s [`url`](msmessage/url.md) property, and present it to the user. For more information on receiving messages, see [`MSMessage`](msmessage.md).
2. After the user responds, create the following:

- A new URL that encodes the updated message state. For example, you could encode the data as key-value pairs in the URL’s query string. For more information, see the [`MSMessage`](msmessage.md) class’s [`url`](msmessage/url.md) property.
- A new layout object that describes the updated message’s appearance. For more information, see the [`MSMessage`](msmessage.md) class’s [`layout`](msmessage/layout.md) property.
- A string that describes the message’s current state. For more information, see the [`MSMessage`](msmessage.md) class’s [`summaryText`](msmessage/summarytext.md) property.

1. Instantiate a new [`MSMessage`](msmessage.md) object by calling its [`init(session:)`](msmessage/init(session:).md) method and passing the currently selected message’s [`MSSession`](mssession.md) object. Set the message’s [`url`](msmessage/url.md), [`layout`](msmessage/layout.md), and [`summaryText`](msmessage/summarytext.md) properties.
2. Send the updated message by calling the conversation’s [`insert(_:completionHandler:)`](msconversation/insert(_:completionhandler:)-3g248.md) method.

The Messages app updates the message in the transcript as soon as the user taps the send button.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MSMessage](msmessage.md)
  A custom message object.
- [class MSMessageLayout](msmessagelayout.md)
  An abstract base class that defines the appearance of [`MSMessage`](msmessage.md) objects in the conversation transcript.
- [class MSMessageTemplateLayout](msmessagetemplatelayout.md)
  A template-based layout for custom messages.
- [class MSMessageLiveLayout](msmessagelivelayout.md)
  A layout that provides a custom, interactive view inside the transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Messages/mssession)*