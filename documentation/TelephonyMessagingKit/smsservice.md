# SMSService

**Framework**: TelephonyMessagingKit  
**Kind**: class

A class that provides an interface for performing SMS operations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final class SMSService
```

## Mentions

- [Creating a carrier messaging app](../availability/creating-a-carrier-messaging-app.md)

#### Overview

Use the [`TelephonyMessagingSession`](telephonymessagingsession.md) property [`smsService`](telephonymessagingsession/smsservice.md) to get an instance of this class. You can then monitor the [`incomingMessageNotifications`](smsservice/incomingmessagenotifications.md) asynchronous sequence to receive notifications of incoming messages, and the [`sendMessage(_:)`](smsservice/sendmessage(_:).md) method to send outgoing messages.

The following example shows how to send an SMS message with the first service found in the session’s [`cellularServices`](telephonymessagingsession/cellularservices.md) array.

```swift
import TelephonyMessagingKit

let service = TelephonyMessagingSession.shared.smsService

let cellularServices = try session.cellularServices
let cellularServiceID = cellularServices[0].id

guard service.isViable(for: cellularServiceID) else { return }

let message = SMSMessage(
    cellularServiceID: cellularServiceID,
    handle: SMSHandle(phoneNumber: SAMPLE_PHONE_NUMBER),
    messageID: SMSMessageID(rawValue: SAMPLE_MESSAGE_ID),
    content: SMSContent(body: "Hello there.")
)

try await service.sendMessage(message)
```

To receive messages, iterate over the [`incomingMessageNotifications`](smsservice/incomingmessagenotifications.md) asynchronous sequence, and retrieve messages from each notification as it arrives, as shown below:

```swift
import TelephonyMessagingKit

let service = TelephonyMessagingSession.shared.smsService

let incomingMessageNotifications = try service.incomingMessageNotifications
Task {
    for await notification in incomingMessageNotifications {
        let receivedMessage = notification.message
        // Process receivedMessage.
    }
}
```

## Topics

### Determining service viabililty
- [func isViable(for: CellularServiceID) -> Bool](smsservice/isviable(for:).md)
  Queries whether the device can perform SMS operations at this time.
- [var viabilityNotifications: some AsyncSequence<SMSService.ViabilityNotification, Never>](smsservice/viabilitynotifications.md)
  An asynchronous sequence of service viability notifications produced by this service.
- [SMSService.ViabilityNotification](smsservice/viabilitynotification.md)
  A notification that indicates whether SMS is viable for a given cellular service.
### Sending messages
- [func sendMessage(SMSMessage) async throws](smsservice/sendmessage(_:).md)
  Sends an SMS message to the given destination.
- [struct SMSMessage](smsmessage.md)
  A structure that contains the data of an SMS message.
### Receiving messages
- [var incomingMessageNotifications: some AsyncSequence<SMSService.IncomingMessageNotification, Never>](smsservice/incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by this service.
- [SMSService.IncomingMessageNotification](smsservice/incomingmessagenotification.md)
  A structure that contains information about an incoming SMS message.
### Handling critical state changes
- [var criticalMessageStateNotifications: some AsyncSequence<SMSService.CriticalMessageStateNotification, Never>](smsservice/criticalmessagestatenotifications.md)
  An asynchronous sequence of critical message state notifications.
- [SMSService.CriticalMessageStateNotification](smsservice/criticalmessagestatenotification.md)
  A structure that contains information about a critical SMS message.
### Reporting spam
- [func reportSpam(SMSMessage) async throws](smsservice/reportspam(_:).md)
  Reports an SMS message as spam to the carrier and to partners.
### Handling errors
- [SMSService.Error](smsservice/error.md)
  A type to define errors that can occur when performing SMS operations.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var smsService: SMSService](telephonymessagingsession/smsservice.md)
  The Short Message Service (SMS) service associated with this session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice)*