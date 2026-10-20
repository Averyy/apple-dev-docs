# EKEventStoreRequestAccessCompletionHandler

**Framework**: EventKit  
**Kind**: typealias  
**Role**: Type Alias

The signature for a closure that EventKit calls when requesting access to event and reminder data.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
typealias EKEventStoreRequestAccessCompletionHandler = (Bool, (any Error)?) -> Void
```

```c
typedef void (^)(_Bool, NSError *) EKEventStoreRequestAccessCompletionHandler;
```

## Parameters

- `granted`: [`true`](../Swift/true.md) if the user allows the app to access data in the event store; otherwise, [`false`](../Swift/false.md).
- `error`: The error that occurred, if any; otherwise, `nil`.

## See Also

### Requesting access to events and reminders
- [func requestWriteOnlyAccessToEvents(completion: (Bool, (any Error)?) -> Void)](./ekeventstore/requestwriteonlyaccesstoevents%28completion%29.md)
  Prompts the person using your app to grant or deny write access to event data.
- [func requestFullAccessToEvents(completion: (Bool, (any Error)?) -> Void)](./ekeventstore/requestfullaccesstoevents%28completion%29.md)
  Prompts people to grant or deny read and write access to event data.
- [func requestFullAccessToReminders(completion: (Bool, (any Error)?) -> Void)](./ekeventstore/requestfullaccesstoreminders%28completion%29.md)
  Prompts people to grant or deny read and write access to reminders.
- [class func authorizationStatus(for: EKEntityType) -> EKAuthorizationStatus](./ekeventstore/authorizationstatus%28for%29.md)
  Determines the authorization status for the given entity type.
- [enum EKAuthorizationStatus](./ekauthorizationstatus.md)
  The current authorization status for a specific entity type.
- [NSCalendarsFullAccessUsageDescription](../BundleResources/information-property-list/nscalendarsfullaccessusagedescription.md)
  A message that tells people why the app is requesting access to read and write their calendar data.
- [NSCalendarsWriteOnlyAccessUsageDescription](../BundleResources/information-property-list/nscalendarswriteonlyaccessusagedescription.md)
  A message that tells people why the app is requesting access to create calendar events.
- [NSRemindersFullAccessUsageDescription](../BundleResources/information-property-list/nsremindersfullaccessusagedescription.md)
  A message that tells people why the app is requesting access to read and write their reminders data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstorerequestaccesscompletionhandler)*