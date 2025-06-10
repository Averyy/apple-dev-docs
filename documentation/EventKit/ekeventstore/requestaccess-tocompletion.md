# requestAccess(to:completion:)

**Framework**: EventKit  
**Kind**: method

Prompts the person using your app to grant or deny access to event or reminder data.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func requestAccess(to entityType: EKEntityType) async throws -> Bool
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func requestAccess(to entityType: EKEntityType) async throws -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

In iOS 6 and later, requesting access to an event store asynchronously prompts your users for permission to use their data. The user is only prompted the first time your app requests access to an entity type; any subsequent instantiations of `EKEventStore` uses existing permissions. When the user taps to grant or deny access, the completion handler will be called on an arbitrary queue. Your app isn’t blocked while the user decides to grant or deny permission.

After users choose their permission level, the event store either calls the completion handler or broadcasts an [`EKEventStoreChangedNotification`](ekeventstorechangednotification.md). The completion handler is called on iOS 6 and later, and the notification is broadcasted on iOS 5. Because users may deny access to the event store, your app should handle an empty data case.

> ❗ **Important**:  If your app has never requested access before, you must request access to events or reminders before attempting to fetch or create them. If you request data before prompting the user for access with this method, you’ll need to reset the event store with the [`reset()`](ekeventstore/reset().md) method in order to start receiving data after the user grants access.

## Parameters

- `entityType`: The event or reminder entity type.
- `completion`: The block to call when the request completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekeventstore/requestaccess(to:completion:))*