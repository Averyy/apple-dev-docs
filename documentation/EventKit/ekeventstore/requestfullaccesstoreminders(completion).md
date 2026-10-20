# requestFullAccessToReminders(completion:)

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

Prompts people to grant or deny read and write access to reminders.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func requestFullAccessToReminders(completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func requestFullAccessToReminders() async throws -> Bool
```

```objc
- (void) requestFullAccessToRemindersWithCompletion:(EKEventStoreRequestAccessCompletionHandler) completion;
```

## Mentions

- [Accessing the event store](../accessing-the-event-store.md)

#### Discussion

Requesting access to an event store asynchronously prompts people for permission to use their data. The operating system only prompts them the first time your app requests access to reminders; any subsequent instantiations of [`EKEventStore`](../ekeventstore.md) uses existing permissions. When they grant or deny access, [EventKit](../EventKit.md) calls the completion handler on an arbitrary queue.

Your app isn’t blocked while the person decides to grant or deny permission. Because they may deny permission, your app should handle cases where it doesn’t receive access to the event store.

> ❗ **Important**:  If your app has never requested access, you must request access to reminders before attempting to fetch or create them. If you request reminders before prompting the person for access with this method, you’ll need to reset the event store with the [`reset()`](./reset%28%29.md) method to receive data after they grant access.

## Parameters

- `completion`: The block to call when the request completes.

## See Also

### Requesting access to events and reminders
- [func requestWriteOnlyAccessToEvents(completion: (Bool, (any Error)?) -> Void)](./requestwriteonlyaccesstoevents%28completion%29.md)
  Prompts the person using your app to grant or deny write access to event data.
- [func requestFullAccessToEvents(completion: (Bool, (any Error)?) -> Void)](./requestfullaccesstoevents%28completion%29.md)
  Prompts people to grant or deny read and write access to event data.
- [class func authorizationStatus(for: EKEntityType) -> EKAuthorizationStatus](./authorizationstatus%28for%29.md)
  Determines the authorization status for the given entity type.
- [enum EKAuthorizationStatus](../ekauthorizationstatus.md)
  The current authorization status for a specific entity type.
- [typealias EKEventStoreRequestAccessCompletionHandler](../ekeventstorerequestaccesscompletionhandler.md)
  The signature for a closure that EventKit calls when requesting access to event and reminder data.
- [NSCalendarsFullAccessUsageDescription](../../BundleResources/information-property-list/nscalendarsfullaccessusagedescription.md)
  A message that tells people why the app is requesting access to read and write their calendar data.
- [NSCalendarsWriteOnlyAccessUsageDescription](../../BundleResources/information-property-list/nscalendarswriteonlyaccessusagedescription.md)
  A message that tells people why the app is requesting access to create calendar events.
- [NSRemindersFullAccessUsageDescription](../../BundleResources/information-property-list/nsremindersfullaccessusagedescription.md)
  A message that tells people why the app is requesting access to read and write their reminders data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/requestfullaccesstoreminders(completion:))*