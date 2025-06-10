# EKAuthorizationStatus

**Framework**: EventKit  
**Kind**: enum

The current authorization status for a specific entity type.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum EKAuthorizationStatus
```

## Topics

### Status
- [EKAuthorizationStatus.fullAccess](ekauthorizationstatus/fullaccess.md)
  The app has both read and write access to the requested entity type.
- [EKAuthorizationStatus.writeOnly](ekauthorizationstatus/writeonly.md)
  The app has write-only access to the requested entity type.
- [EKAuthorizationStatus.denied](ekauthorizationstatus/denied.md)
  The person explicitly denied access to the service for the app.
- [EKAuthorizationStatus.notDetermined](ekauthorizationstatus/notdetermined.md)
  The person hasn’t chosen whether the app may access the service.
- [EKAuthorizationStatus.restricted](ekauthorizationstatus/restricted.md)
  The app isn’t authorized to access the service.
### Deprecated values
- [static var authorized: EKAuthorizationStatus](ekauthorizationstatus/authorized.md)
  The app can access the service.
### Initializers
- [init?(rawValue: Int)](ekauthorizationstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func requestWriteOnlyAccessToEvents(completion: (Bool, (any Error)?) -> Void)](ekeventstore/requestwriteonlyaccesstoevents(completion:).md)
  Prompts the person using your app to grant or deny write access to event data.
- [func requestFullAccessToEvents(completion: (Bool, (any Error)?) -> Void)](ekeventstore/requestfullaccesstoevents(completion:).md)
  Prompts people to grant or deny read and write access to event data.
- [func requestFullAccessToReminders(completion: (Bool, (any Error)?) -> Void)](ekeventstore/requestfullaccesstoreminders(completion:).md)
  Prompts people to grant or deny read and write access to reminders.
- [class func authorizationStatus(for: EKEntityType) -> EKAuthorizationStatus](ekeventstore/authorizationstatus(for:).md)
  Determines the authorization status for the given entity type.
- [typealias EKEventStoreRequestAccessCompletionHandler](ekeventstorerequestaccesscompletionhandler.md)
  The signature for a closure that EventKit calls when requesting access to event and reminder data.
- [NSCalendarsFullAccessUsageDescription](../BundleResources/Information-Property-List/NSCalendarsFullAccessUsageDescription.md)
  A message that tells people why the app is requesting access to read and write their calendar data.
- [NSCalendarsWriteOnlyAccessUsageDescription](../BundleResources/Information-Property-List/NSCalendarsWriteOnlyAccessUsageDescription.md)
  A message that tells people why the app is requesting access to create calendar events.
- [NSRemindersFullAccessUsageDescription](../BundleResources/Information-Property-List/NSRemindersFullAccessUsageDescription.md)
  A message that tells people why the app is requesting access to read and write their reminders data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekauthorizationstatus)*