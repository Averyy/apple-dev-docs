# requestWriteOnlyAccessToEvents(completion:)

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

Prompts the person using your app to grant or deny write access to event data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func requestWriteOnlyAccessToEvents(completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func requestWriteOnlyAccessToEvents() async throws -> Bool
```

```objc
- (void) requestWriteOnlyAccessToEventsWithCompletion:(EKEventStoreRequestAccessCompletionHandler) completion;
```

## Mentions

- [Accessing the event store](../accessing-the-event-store.md)

## Discussion

Requesting access to an event store asynchronously prompts people for permission to use their data. The operating system only prompts them the first time your app requests write-only event access; any subsequent instantiations of [`EKEventStore`](../ekeventstore.md) uses existing permissions. When they grant or deny access, [EventKit](../EventKit.md) calls the completion handler on an arbitrary queue.

> ❗ **Important**:  If your app has never requested access, you must request write-only or full access to events before attempting to create them. If you request events before prompting the user for access with this method, you’ll need to reset the event store with the [`reset()`](./reset%28%29.md) method to receive data after the user grants access.

Your app isn’t blocked while the person decides to grant or deny permission. Because they may deny permission, your app needs to handle the case where it doesn’t receive access to the event store.

If the person grants permission, your app receives write-only access to the event store. Your app can create events, but it can’t access any of the existing calendars and events on the device, including events your app created. API calls to read event data from the event store don’t return any events.

> **Note**:  Your iOS or Mac Catalyst app can present an [`EKEventEditViewController`](../../EventKitUI/ekeventeditviewcontroller.md) to let your user create events without requesting access to the event store. If your app creates events without using [`EKEventEditViewController`](../../EventKitUI/ekeventeditviewcontroller.md), you must request at least write-only access to event data.

## Parameters

- `completion`: The block to call when the request completes.

## See Also

### Requesting access to events and reminders
- [func requestFullAccessToEvents(completion: (Bool, (any Error)?) -> Void)](./requestfullaccesstoevents%28completion%29.md)
  Prompts people to grant or deny read and write access to event data.
- [func requestFullAccessToReminders(completion: (Bool, (any Error)?) -> Void)](./requestfullaccesstoreminders%28completion%29.md)
  Prompts people to grant or deny read and write access to reminders.
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

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/requestwriteonlyaccesstoevents(completion:))*