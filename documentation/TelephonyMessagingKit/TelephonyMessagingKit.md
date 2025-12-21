# TelephonyMessagingKit

**Framework**: TelephonyMessagingKit  
**Kind**: module

Send and receive standards-based messages over cellular networks.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

#### Overview

To use TelephonyMessagingKit, use the shared instance of [`TelephonyMessagingSession`](telephonymessagingsession.md) as your app’s main point of contact with the framework. Using a session, your app can inspect the services currently available on the device. The framework supports Short Message Service (SMS), Multimedia Messaging Service (MMS), and Rich Communication Services (RCS).

Each service provides an asynchronous sequence for notifications of incoming messages that the app can handle. To send a new message, compose the message content and then call the `send` method appropriate to the service. The RCS service, if present, provides functionality that goes beyond one-to-one messaging, including group chat and chatbots.

> **Note**: TelephonyMessagingKit supports SMS, MMS, and RCS messaging only on iPhone devices. The framework has no functionality on iPadOS or on iOS apps running in visionOS or in macOS on Apple silicon. The framework ignores calls from Mac apps built with Mac Catalyst.

##### Default Carrier Messaging Apps

To have access to the TelephonyMessageKit API you must add the [`Default Carrier Messaging App`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.carrier-messaging-app) entitlement to your app. This functionality will be enabled in your app only when the user selects your app to be the default carrier messaging app.

> ❗ **Important**: You may develop and test TelephonyMessagingKit apps on devices in all regions by using an Apple-provided provisioning profile. People using your app must have an account registered in the European Union (EU), and their device must be located within the EU.

## Topics

### Essentials
- [Creating a carrier messaging app](../availability/creating-a-carrier-messaging-app.md)
  Use TelephonyMessagingKit to send and receive SMS, MMS, and RCS messages.
- [class TelephonyMessagingSession](telephonymessagingsession.md)
  An object that coordinates interaction with the TelephonyMessagingKit framework.
- [Default Carrier Messaging App](../BundleResources/Entitlements/com.apple.developer.carrier-messaging-app.md)
  A Boolean value that indicates whether the app can use the TelephonyMessagingKit framework to serve as the default carrier messaging app.
### Supporting types
- [struct RCSFileTransferMetadata](rcsfiletransfermetadata.md)
  A structure that contains metadata about an RCS file transfer.
- [struct RCSGroupContext](rcsgroupcontext.md)
  Structure containing information about a message’s group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TelephonyMessagingKit)*