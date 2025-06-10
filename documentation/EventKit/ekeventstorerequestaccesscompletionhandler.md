# EKEventStoreRequestAccessCompletionHandler

**Framework**: EventKit  
**Kind**: typealias

The signature for a closure that EventKit calls when requesting access to event and reminder data.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias EKEventStoreRequestAccessCompletionHandler = (Bool, (any Error)?) -> Void
```

## Parameters

- `granted`:   if the user allows the app to access data in the event store; otherwise,  .
- `error`: The error that occurred, if any; otherwise,  .

## See Also

- [func requestWriteOnlyAccessToEvents(completion: (Bool, (any Error)?) -> Void)](ekeventstore/requestwriteonlyaccesstoevents(completion:).md)
  Prompts the person using your app to grant or deny write access to event data.
- [func requestFullAccessToEvents(completion: (Bool, (any Error)?) -> Void)](ekeventstore/requestfullaccesstoevents(completion:).md)
  Prompts people to grant or deny read and write access to event data.
- [func requestFullAccessToReminders(completion: (Bool, (any Error)?) -> Void)](ekeventstore/requestfullaccesstoreminders(completion:).md)
  Prompts people to grant or deny read and write access to reminders.
- [class func authorizationStatus(for: EKEntityType) -> EKAuthorizationStatus](ekeventstore/authorizationstatus(for:).md)
  Determines the authorization status for the given entity type.
- [enum EKAuthorizationStatus](ekauthorizationstatus.md)
  The current authorization status for a specific entity type.
- [NSCalendarsFullAccessUsageDescription](../BundleResources/Information-Property-List/NSCalendarsFullAccessUsageDescription.md)
  A message that tells people why the app is requesting access to read and write their calendar data.
- [NSCalendarsWriteOnlyAccessUsageDescription](../BundleResources/Information-Property-List/NSCalendarsWriteOnlyAccessUsageDescription.md)
  A message that tells people why the app is requesting access to create calendar events.
- [NSRemindersFullAccessUsageDescription](../BundleResources/Information-Property-List/NSRemindersFullAccessUsageDescription.md)
  A message that tells people why the app is requesting access to read and write their reminders data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstorerequestaccesscompletionhandler)*