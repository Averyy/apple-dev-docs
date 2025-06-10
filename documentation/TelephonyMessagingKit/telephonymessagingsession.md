# TelephonyMessagingSession

**Framework**: TelephonyMessagingKit  
**Kind**: class

An object that coordinates interaction with the TelephonyMessagingKit framework.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
final class TelephonyMessagingSession
```

#### Overview

Use the [`shared`](telephonymessagingsession/shared.md) instance provided by this class to access SMS, MMS, and RCS messaging services. You can inspect available services with the [`cellularServices`](telephonymessagingsession/cellularservices.md) property. As service availability changes, the framework publishes changes through the [`cellularServiceStateUpdates`](telephonymessagingsession/cellularservicestateupdates.md) asynchronous sequence.

## Topics

### Obtaining the shared instance
- [static let shared: TelephonyMessagingSession](telephonymessagingsession/shared.md)
  The shared session instance.
### Determining service availability
- [var cellularServices: [CellularServiceState]](telephonymessagingsession/cellularservices.md)
  An array of cellular services available on the system.
- [var cellularServiceStateUpdates: some AsyncSequence<CellularServiceState, Never>](telephonymessagingsession/cellularservicestateupdates.md)
  An asynchronous sequence of cellular service state updates produced by this session.
- [struct CellularServiceState](cellularservicestate.md)
  A structure that contains information about a cellular service.
### Using Short Message Service (SMS)
- [var smsService: SMSService](telephonymessagingsession/smsservice.md)
  The Short Message Service (SMS) service associated with this session.
- [class SMSService](smsservice.md)
  A class that provides an interface for performing SMS operations.
### Using Multimedia Messaging Service (MMS)
- [var mmsService: MMSService](telephonymessagingsession/mmsservice.md)
  MMS service associated with this session.
- [class MMSService](mmsservice.md)
  A class that provides an interface for performing MMS operations.
### Using Rich Communication Services (RCS)
- [var rcsService: RCSService](telephonymessagingsession/rcsservice.md)
  RCS service associated with this session.
- [class RCSService](rcsservice.md)
  A class that provides an interface for performing RCS operations.
### Accessing session properties
- [let id: UUID](telephonymessagingsession/id-swift.property.md)
  Identifier for this session.
### Handling errors
- [TelephonyMessagingSession.Error](telephonymessagingsession/error.md)
  An enumeration of errors that can result from operations on a messaging session.
### Supporting types
- [TelephonyMessagingSession.ID](telephonymessagingsession/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Default Carrier Messaging App](../BundleResources/Entitlements/com.apple.developer.carrier-messaging-app.md)
  A Boolean value that indicates whether the app can use the TelephonyMessagingKit framework to serve as the default carrier messaging app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/telephonymessagingsession)*