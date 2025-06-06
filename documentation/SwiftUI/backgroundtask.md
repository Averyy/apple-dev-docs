# BackgroundTask

**Framework**: SwiftUI  
**Kind**: struct

The kinds of background tasks that your app or extension can handle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct BackgroundTask<Request, Response>
```

#### Overview

Use a value of this type with the [`backgroundTask(_:action:)`](scene/backgroundtask(_:action:).md) scene modifier to create a handler for background tasks that the system sends to your app or extension. For example, you can use [`urlSession`](backgroundtask/urlsession.md) to define an asynchronous closure that the system calls when it launches your app or extension to handle a response from a background [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession).

## Topics

### Refreshing the app
- [static var appRefresh: BackgroundTask<String?, Void>](backgroundtask/apprefresh.md)
  A task that updates your app’s state in the background.
- [static func appRefresh(String) -> BackgroundTask<Void, Void>](backgroundtask/apprefresh(_:).md)
  A task that updates your app’s state in the background for a matching identifier.
### Preparing for a snapshot
- [static var snapshot: BackgroundTask<SnapshotData, SnapshotResponse>](backgroundtask/snapshot.md)
  A background task used to update your app’s user interface in preparation for a snapshot.
### Receiving connectivity updates
- [static var bluetoothAlert: BackgroundTask<Void, Void>](backgroundtask/bluetoothalert.md)
  A background task used to receive critical alerts from paired bluetooth accessories.
- [static var watchConnectivity: BackgroundTask<Void, Void>](backgroundtask/watchconnectivity.md)
  A background task used to receive background updates from the Watch Connectivity framework.
### Responding to URL sessions
- [static var urlSession: BackgroundTask<String, Void>](backgroundtask/urlsession.md)
  A task that responds to background URL sessions.
- [static func urlSession(String) -> BackgroundTask<Void, Void>](backgroundtask/urlsession(_:).md)
  A task that responds to background URL sessions matching the given identifier.
- [static func urlSession(matching: (String) -> Bool) -> BackgroundTask<String, Void>](backgroundtask/urlsession(matching:).md)
  A task that responds to background URL sessions matching the given predicate.
### Updating intents and shortcuts
- [static var intentDidRun: BackgroundTask<Void, Void>](backgroundtask/intentdidrun.md)
  A background task used to update your app after a SiriKit intent runs.
- [static var relevantShortcut: BackgroundTask<Void, Void>](backgroundtask/relevantshortcut.md)
  A background task used to periodically donate relevant Siri shortcuts.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) -> some Scene](scene/backgroundtask(_:action:).md)
  Runs the specified action when the system provides a background task.
- [struct SnapshotData](snapshotdata.md)
  The associated data of a snapshot background task.
- [struct SnapshotResponse](snapshotresponse.md)
  Your appplication’s response to a snapshot background task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/backgroundtask)*