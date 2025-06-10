# Sending SMS messages from an app

**Framework**: Messages

Send critical messages from inside your app using the Critical Messaging API.

#### Overview

The Critical Messaging API provides a way for apps to deliver critical messages to a set of phone numbers. This can serve a number of purposes. For example, if an enterprise wants to receive check-ins from employees working in hazardous or rural environments, being able to automatically message a corporate check-in point may help check the safety of those employees without disrupting their work, or if the employee is unable to access or unlock their iPhone.

##### Enable Your App to Use the Critical Messaging Api

Add the `com.apple.developer.messages.critical-messaging` entitlement to your app’s entitlement file in Xcode. For instructions on how to add this entitlement, see [`Critical Messaging`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.messages.critical-messaging).

In addition, add the [`NSCriticalMessagingUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCriticalMessagingUsageDescription) key
to your app’s `Info.plist` file and provide a usage description for the operating system to display when the framework requests a person’s authorization to use this capability.

> ❗ **Important**: Critical messages sent via this API may not transmit in scenarios where SMS service is unavailable.

##### Understand Api Restrictions and Usage Limitations

You app’s use of this API must follow the [`Developer Program License Agreement`](https://developer.apple.comhttps://developer.apple.com/support/terms/apple-developer-program-license-agreement#other-tech); additionally the following API limitations and restrictions apply:

1. The [`send(_:to:)`](mscriticalsmsmessenger/send(_:to:).md) method only works if the app is backgrounded, if it’s called from foreground the framework returns a [`MSCriticalMessagingError.notSupported`](mscriticalmessagingerror/notsupported.md) error.
2. The system may impose a rate limit on frequency of messages sent, if usage exceeds this limit the framework returns a  [`MSCriticalMessagingError.sendFailed`](mscriticalmessagingerror/sendfailed.md) error.
3. When providing phone numbers through [`requestAuthorization(for:)`](mscriticalsmsmessenger/requestauthorization(for:).md), the Messages framework checks if the phone numbers are part of the user’s contacts and populates the users name in the authorization alert as well as in the Settings page.

A person can change the authorization to send critical messages in Settings, under Privacy & Security > Critical Messaging. Check authorization using [`checkAuthorizationStatus(for:)`](mscriticalsmsmessenger/checkauthorizationstatus(for:).md) before using this capability.

##### Send Critical Sms Messages From Your App

To send messages from your app, create an instance of the background messaging manager and recipients, request authorization, then send your message. For example:

```swift
let manager = MSCriticalSMSMessenger()

let recipient1 = MSRecipient(phoneNumber: "18005552222")
let recipient2 = MSRecipient(phoneNumber: "18005553333")
let recipient3 = MSRecipient(phoneNumber: "4401539702257")

let status = try await manager.requestAuthorization(to recipients: [recipient1, recipient2, recipient3])
let status = manager.send(to recipient: recipient1, message: MSCriticalMessage("Hello there"))

// Handle any error response the system returns.
```

## See Also

- [class MSCriticalSMSMessenger](mscriticalsmsmessenger.md)
  The user interface for the Critical Messaging API.
- [struct MSRecipient](msrecipient.md)
  A structure that describes the recipient of a critical message.
- [struct MSCriticalMessage](mscriticalmessage.md)
  MSCriticalMessage A simple struct to encapsulate the message string.
- [enum MSCriticalMessagingAuthorizationStatus](mscriticalmessagingauthorizationstatus.md)
  Values that describe the authorization status for the Critical Messaging API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/critical-messaging-api)*