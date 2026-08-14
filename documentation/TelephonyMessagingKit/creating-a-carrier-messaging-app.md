# Creating a carrier messaging app

**Framework**: TelephonyMessagingKit

Use TelephonyMessagingKit to send and receive SMS, MMS, and RCS messages.

#### Overview

When the person using a device chooses your app to be the default carrier messaging app, the system sends all SMS, MMS, and RCS messages received by the device to your app. You use this framework to send and receive messages with those services.

This article describes how to set up your app to be the default app for carrier messaging. To see how to also make your app the default app for internet-based messaging, see [`Preparing your app to be the default messaging app`](https://developer.apple.com/documentation/messages/preparing-your-app-to-be-the-default-messaging-app).

> ❗ **Important**: You may develop and test `TelephonyMessagingKit` apps on devices in all regions by using an Apple-provided provisioning profile. People using your app must have an account registered in the European Union (EU), and their device must be located within the EU.

##### Configure Your App with the Required Entitlement

To make your app eligible to become the default carrier messaging app, add the  [`Default Carrier Messaging App`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.carrier-messaging-app) entitlement, as described on the entitlement’s documentation page.

When someone uses the device in an environment that supports the use of TelephonyMessagingKit, they can choose a default carrier messaging app from the Settings app. If they choose your app, the system sends all SMS, MMS, and RCS messages to your app. If they choose a different app, your app doesn’t receive and can’t send carrier messages.

To test whether your app can send and receive carrier messages, check the [`TelephonyMessagingSession`](telephonymessagingsession.md) property [`isConfiguredForCarrierMessaging`](telephonymessagingsession/isconfiguredforcarriermessaging.md) before you make any calls to TelephonyMessagingKit.

##### Handle App Launch

If your app isn’t running and the device receives an SMS, MMS, or RCS message, the system launches your app in the background, and gives your app some CPU time to process the received messages. Use this time to collect the messages, add them to your app’s data model or a persistent data store, and then post a local notification.

The person using the device can launch your app by tapping on a local notification you post, or by launching it normally from the app icon. This means there may or may not be messages to collect immediately after the app launches.

> **Note**: TelephonyMessagingKit uses a timeout for queued messages to avoid wasting memory. If your app doesn’t fetch received messages in time, the framework may discard them.

##### Discover Cellular Services

The person using your app may have multiple cellular services active at one time. To get an array of cellular services, use the [`shared`](telephonymessagingsession/shared.md) instance of [`TelephonyMessagingSession`](telephonymessagingsession.md) to get the [`cellularServices`](telephonymessagingsession/cellularservices.md) array. Each member of this array is an instance of [`CellularServiceState`](cellularservicestate.md), which contains a unique identifier for the cellular service and a label string. These labels correspond to the names the person gives to the services in the Settings app, under Settings > Cellular > SIM > Cellular Plan Label.

Your app needs a cellular service identifier when posting messages to specify which cellular service sends the message. Received messages include a cellular service identifier, so you know which service sent them.

If you want to handle changes to the cellular services, such as someone removing a SIM or changing the labels associated with their services, monitor the session’s [`cellularServiceStateUpdates`](telephonymessagingsession/cellularservicestateupdates.md) asynchronous sequence.

##### Receive Messages

The shared instance of [`TelephonyMessagingSession`](telephonymessagingsession.md) also provides access to the device’s messaging services, as the properties [`smsService`](telephonymessagingsession/smsservice.md), [`mmsService`](telephonymessagingsession/mmsservice.md), and [`rcsService`](telephonymessagingsession/rcsservice.md). These properties are instances of the types [`SMSService`](smsservice.md), [`MMSService`](mmsservice.md), and [`RCSService`](rcsservice.md), respectively. Be aware that some or all of these may be available or unavailable at any time, based on carrier offerings and the device’s service plan, and whether your app is the default carrier messaging app.

Each service provides an asynchronous sequence called `incomingMessageNotifications` that you use to receive messages.  Iterate over this sequence with a `for`-`await`-`in` loop to collect any messages that TelephonyMessagingKit queued while your app wasn’t running, and to receive new messages as they arrive. Each notification includes a `message` property to represent the incoming message, along with other service-specific properties, such as group information when using an [`RCSService`](rcsservice.md).

The following example shows a loop that processes incoming SMS messages by calling a hypothetical `storeSMSMessage(_:)` method to add them to a local data store, so they are available for a view elsewhere in the app to display. The loop also sends local notifications with the [`User Notifications`](https://developer.apple.com/documentation/usernotifications) framework in case the app is running in the background, which can happen if messages arrive and the app isn’t running. If the app is running when messages arrive, sending the local notification does nothing.

```swift
guard TelephonyMessagingSession.shared.isConfiguredForCarrierMessaging else { return }
let notifications = try TelephonyMessagingSession.shared.smsService.incomingMessageNotifications
for await smsMessageNotification in notifications {
    let message = smsMessageNotification.message
    // Add message to data store.
    storeSMSMessage(message)

    // Post local notification.
    let notificationContent = UNMutableNotificationContent()
    notificationContent.title = "My Message App"
    notificationContent.subtitle = "From: \(message.handle.phoneNumber)"
    notificationContent.body = message.content.body
    let request = UNNotificationRequest(identifier: "com.example.mymessageapp",
                                        content: notificationContent,
                                        trigger: nil)
    try await UNUserNotificationCenter.current().add(request)
}
```

The process is similar for receiving MMS and RCS messages.

##### Send Messages

Your app can also send messages with SMS, MMS, or RCS.  While there are differences in the `sendMessage()` methods exposed by [`SMSService`](smsservice.md), [`MMSService`](mmsservice.md), and [`RCSService`](rcsservice.md), they all require the following:

- A [`CellularServiceID`](cellularserviceid.md) that indicates which cellular service the framework should use to send the message.
- The phone number of a recipient, wrapped in a “handle” type specific to the messaging service, like [`SMSHandle`](smshandle.md). For MMS, you can send a message to multiple recipients as an array of handles. For RCS, the [`RCSHandle`](rcshandle.md) type can represent either a single recipient or a group of recipients.
- A unique identifier for the message.
- The message content. For SMS, the [`SMSContent`](smscontent.md) type wraps a single string. For MMS, you create an [`MMSContent`](mmscontent.md) instance, which can contain multiple parts of different types. For RCS, there are different supporting types for different kinds of content, like text, acknowledgements of file transfers, geolocation coordinates, and composing indicators (such as “someone is typing”). In the RCS case, separate overloads of the `sendMessage()` method handle each of these different content types.

If there are multiple cellular services in the session’s [`cellularServices`](telephonymessagingsession/cellularservices.md) array, your app can show a list to the person using the app and let them choose one to send the message. If the array contains only one cellular service, you can skip this and default to using the first member of the array.

The following example shows the basic case of sending an SMS text message to a single recipient. This example uses the first cellular service in the session’s [`cellularServices`](telephonymessagingsession/cellularservices.md) array; a more robust app needs to give someone the ability to choose which of their services to use if there are more than one.

```swift
guard TelephonyMessagingSession.shared.isConfiguredForCarrierMessaging else { return }
let service = TelephonyMessagingSession.shared.smsService
let cellularServices = try TelephonyMessagingSession.shared.cellularServices
let cellularServiceID = cellularServices[0].id
guard service.isViable(for: cellularServiceID) else { return }

let message = SMSMessage(
    cellularServiceID: cellularServiceID,
    handle: SMSHandle(phoneNumber: SAMPLE_PHONE_NUMBER),
    messageID: SMSMessageID(rawValue: SAMPLE_SMS_MESSAGE_ID),
    content: SMSContent(body: "Hello There.")
)

try await service.sendMessage(message)
```

## See Also

- [class TelephonyMessagingSession](telephonymessagingsession.md)
  An object that coordinates interaction with the TelephonyMessagingKit framework.
- [Default Carrier Messaging App](../bundleresources/entitlements/com.apple.developer.carrier-messaging-app.md)
  A Boolean value that indicates whether the app can use the TelephonyMessagingKit framework to serve as the default carrier messaging app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/creating-a-carrier-messaging-app)*