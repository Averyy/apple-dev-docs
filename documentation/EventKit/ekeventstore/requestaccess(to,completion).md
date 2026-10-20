# requestAccess(to:completion:)

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

Prompts the person using your app to grant or deny access to event or reminder data.

**Availability**:
- iOS 6.0+ - Deprecated in 17.0
- iPadOS 6.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 1.0+ - Deprecated in 10.0

> **Deprecated**: On iOS 17 and later, this method doesn’t prompt for access and immediately calls the completion block with an error. If your app only uses [`EKEventEditViewController`](../../EventKitUI/ekeventeditviewcontroller.md) to let your user create and save calendar events, don’t request events access. Use [`requestWriteOnlyAccessToEvents(completion:)`](./requestwriteonlyaccesstoevents%28completion%29.md) to create calendar events. Use [`requestFullAccessToEvents(completion:)`](./requestfullaccesstoevents%28completion%29.md) to read and write calendar events. Use [`requestFullAccessToReminders(completion:)`](./requestfullaccesstoreminders%28completion%29.md) to read and write reminders.

## Declaration

```swift
func requestAccess(to entityType: EKEntityType, completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func requestAccess(to entityType: EKEntityType) async throws -> Bool
```

```objc
- (void) requestAccessToEntityType:(EKEntityType) entityType completion:(EKEventStoreRequestAccessCompletionHandler) completion;
```

#### Discussion

In iOS 6 and later, requesting access to an event store asynchronously prompts your users for permission to use their data. The user is only prompted the first time your app requests access to an entity type; any subsequent instantiations of `EKEventStore` uses existing permissions. When the user taps to grant or deny access, the completion handler will be called on an arbitrary queue. Your app isn’t blocked while the user decides to grant or deny permission.

After users choose their permission level, the event store either calls the completion handler or broadcasts an [`EKEventStoreChangedNotification`](../ekeventstorechangednotification.md). The completion handler is called on iOS 6 and later, and the notification is broadcasted on iOS 5. Because users may deny access to the event store, your app should handle an empty data case.

> ❗ **Important**:  If your app has never requested access before, you must request access to events or reminders before attempting to fetch or create them. If you request data before prompting the user for access with this method, you’ll need to reset the event store with the [`reset()`](./reset%28%29.md) method in order to start receiving data after the user grants access.

## Parameters

- `entityType`: The event or reminder entity type.
- `completion`: The block to call when the request completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/requestaccess(to:completion:))*