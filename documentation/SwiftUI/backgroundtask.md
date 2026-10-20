# BackgroundTask

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

Use a value of this type with the [`backgroundTask(_:action:)`](./scene/backgroundtask%28_,action%29.md) scene modifier to create a handler for background tasks that the system sends to your app or extension. For example, you can use [`urlSession`](./backgroundtask/urlsession.md) to define an asynchronous closure that the system calls when it launches your app or extension to handle a response from a background [`URLSession`](../Foundation/urlsession.md).

## Topics

### Refreshing the app
- [static func appRefresh(String) -> BackgroundTask<Void, Void>](./backgroundtask/apprefresh%28_%29.md)
  A task that updates your app’s state in the background for a matching identifier.
- [static var appRefresh: BackgroundTask<String?, Void>](./backgroundtask/apprefresh.md)
  A task that updates your app’s state in the background.
### Receiving connectivity updates
- [static var bluetoothAlert: BackgroundTask<Void, Void>](./backgroundtask/bluetoothalert.md)
  A background task used to receive critical alerts from paired bluetooth accessories.
- [static var watchConnectivity: BackgroundTask<Void, Void>](./backgroundtask/watchconnectivity.md)
  A background task used to receive background updates from the Watch Connectivity framework.
### Responding to URL sessions
- [static var urlSession: BackgroundTask<String, Void>](./backgroundtask/urlsession.md)
  A task that responds to background URL sessions.
- [static func urlSession(String) -> BackgroundTask<Void, Void>](./backgroundtask/urlsession%28_%29.md)
  A task that responds to background URL sessions matching the given identifier.
- [static func urlSession(matching: (String) -> Bool) -> BackgroundTask<String, Void>](./backgroundtask/urlsession%28matching%29.md)
  A task that responds to background URL sessions matching the given predicate.
### Updating intents and shortcuts
- [static var intentDidRun: BackgroundTask<Void, Void>](./backgroundtask/intentdidrun.md)
  A background task used to update your app after a SiriKit intent runs.
- [static var relevantShortcut: BackgroundTask<Void, Void>](./backgroundtask/relevantshortcut.md)
  A background task used to periodically donate relevant Siri shortcuts.
### Processing tasks
- [static func processingTask(String) -> BackgroundTask<Void, Void>](./backgroundtask/processingtask%28_%29.md)
  A task that processes tasks in the background.
### Deprecated symbols
- [static var snapshot: BackgroundTask<SnapshotData, SnapshotResponse>](./backgroundtask/snapshot.md)
  A background task used to update your app’s user interface in preparation for a snapshot.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling background tasks
- [func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) -> some Scene](./scene/backgroundtask%28_,action%29.md)
  Runs the specified action when the system provides a background task.
- [struct SnapshotData](./snapshotdata.md)
  The associated data of a snapshot background task.
- [struct SnapshotResponse](./snapshotresponse.md)
  Your application’s response to a snapshot background task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/backgroundtask)*