# MMSService

**Framework**: TelephonyMessagingKit  
**Kind**: class

A class that provides an interface for performing MMS operations.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final class MMSService
```

#### Overview

Use the [`TelephonyMessagingSession`](telephonymessagingsession.md) property [`mmsService`](telephonymessagingsession/mmsservice.md) to get an instance of this class. You can then monitor the [`incomingMessageNotifications`](mmsservice/incomingmessagenotifications.md) asynchronous sequence to receive notification of incoming messages, and the [`sendMessage(_:)`](mmsservice/sendmessage(_:).md) method to send outgoing messages.

The following example shows how to send an message consisting of a text portion and an image attachment.

```swift
import TelephonyMessagingKit

let service = TelephonyMessagingSession.shared.mmsService

let cellularServices = try session.cellularServices
let cellularServiceID = cellularServices[0].id

guard service.isViable(for: cellularServiceID) else {
    return
}

var recipients: [MMSHandle] = []
for phone in recipientPhoneNumbers {
    recipients.append(MMSHandle(phoneNumber: phone))
}
var parts: [MMSPartContent] = []

let content1 = MMSPartContent(data: text.data(using: .utf8)!,
                              contentType: UTType.plainText,
                              contentID: UUID().uuidString,
                              disposition: .inline,
                              fileName: "")

let content2 = MMSPartContent(data: imageData,
                              contentType: UTType.jpeg,
                              contentID: UUID().uuidString,
                              disposition: .attachment,
                              fileName: "Image_1.jpg")

parts.append(content1)
parts.append(content2)

let content = MMSContent(parts: parts, recipients: recipients, subject: "")
let msgID = MMSMessageID(rawValue: SAMPLE_MMS_MESSAGE_ID)

let message = MMSMessage(cellularServiceID: cellularServiceID,
                         messageID: msgID,
                         content: content)

Task {
    do {
        try await service.sendMessage(message:message)
        // Handle MMS send success.
    } catch {
        // Handle MMS send failure.
    }
}

```

To receive messages, iterate over the [`incomingMessageNotifications`](mmsservice/incomingmessagenotifications.md) asynchronous sequence, and call [`receiveMessage(using:messageID:)`](mmsservice/receivemessage(using:messageid:).md) with the identifiers from each notification, as shown here:

```swift
import TelephonyMessagingKit

let service = TelephonyMessagingSession.shared.smsService

let incomingMessageNotifications = try service.incomingMessageNotifications
Task {
    for await notification in incomingMessageNotifications {
        try await handleIncomingMMS(for: notification.cellularServiceID,
                                    messageID: notification.messageID)
    }
}

func handleIncomingMMS(for cellularServiceID: CellularServiceID, messageID: MMSMessageID) async throws {
    // Retrieve MMS message with identifiers from incomingMessageNotifications.
    // A client may also delay retrieving the message if MMS isn't currently viable.
    let message = try await service.receiveMessage(using: cellularServiceID,
                                                   messageID: messageID)
    // Process message.
}
```

## Topics

### Determining service viabililty
- [func isViable(for: CellularServiceID) -> Bool](mmsservice/isviable(for:).md)
  Queries whether the device can perform MMS operations at this time.
- [var viabilityNotifications: some AsyncSequence<MMSService.ViabilityNotification, Never>](mmsservice/viabilitynotifications.md)
  An asynchronous sequence of service viability notifications produced by the service.
- [MMSService.ViabilityNotification](mmsservice/viabilitynotification.md)
  A notification that indicates if MMS is viable for a given cellular service.
### Sending messages
- [func sendMessage(MMSMessage) async throws](mmsservice/sendmessage(_:).md)
  Sends an MMS message to the given destination.
- [struct MMSMessage](mmsmessage.md)
  A structure that contains the data of an MMS message.
### Receiving messages
- [func receiveMessage(using: CellularServiceID, messageID: MMSMessageID) async throws -> MMSMessage](mmsservice/receivemessage(using:messageid:).md)
  Retrieves an MMS message that matches the given identifiers.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [struct MMSMessageID](mmsmessageid.md)
  A structure that represents an MMS message identifier.
- [var incomingMessageNotifications: some AsyncSequence<MMSService.IncomingMessageNotification, Never>](mmsservice/incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by the service.
- [MMSService.IncomingMessageNotification](mmsservice/incomingmessagenotification.md)
  A structure that contains information about an incoming MMS message.
### Reporting spam
- [func reportSpam(MMSMessage) async throws](mmsservice/reportspam(_:).md)
  Reports an MMS message as spam to the carrier and to partners.
### Handling errors
- [MMSService.Error](mmsservice/error.md)
  Enumeration for errors that can occur when performing MMS operations.
### Structures
- [MMSService.Configuration](mmsservice/configuration.md)
  A structure that provides information about MMS messages sent and received using the current carrier.
### Instance Methods
- [func configuration(for: CellularServiceID) async throws -> MMSService.Configuration](mmsservice/configuration(for:).md)
  Retrieves the MMS configuration for the carrier.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var mmsService: MMSService](telephonymessagingsession/mmsservice.md)
  MMS service associated with this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice)*