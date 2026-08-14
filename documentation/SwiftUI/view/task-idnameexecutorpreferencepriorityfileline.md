# task(id:name:executorPreference:priority:file:line:_:)

**Framework**: SwiftUI  
**Kind**: method

Adds a task to perform before this view appears or when a specified value changes.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
nonisolated
func task<T>(id: T, name: String? = nil, executorPreference taskExecutor: any TaskExecutor, priority: TaskPriority = .userInitiated, file: String = #fileID, line: Int = #line, _ action: sending @escaping @isolated(any) () async -> Void) -> some View where T : Equatable
```

#### Return Value

A view that runs the specified action asynchronously before the view appears, or restarts the task when the `id` value changes.

#### Discussion

This method behaves like `View/task(priority:_:)`, except that it also cancels and recreates the task when a specified value changes. To detect a change, the modifier tests whether a new value for the `id` parameter equals the previous value. For this to work, the value’s type must conform to the [`Equatable`](https://developer.apple.com/documentation/swift/equatable) protocol.

For example, if you define an equatable `Server` type that posts custom notifications whenever its state changes — for example, from *signed out* to *signed in* — you can use the task modifier to update the contents of a [`Text`](text.md) view to reflect the state of the currently selected server:

```swift
Text(status ?? "Signed Out")
    .task(id: server) {
        let sequence = NotificationCenter.default.notifications(
            named: .didUpdateStatus,
            object: server
        ).compactMap {
            $0.userInfo?["status"] as? String
        }
        for await value in sequence {
            status = value
        }
    }
```

This example uses the [`notifications(named:object:)`](https://developer.apple.com/documentation/foundation/notificationcenter/notifications(named:object:)) method to create an asynchronous sequence of notifications, given by an [`AsyncSequence`](https://developer.apple.com/documentation/swift/asyncsequence) instance. The example then maps the notification sequence to a sequence of strings that correspond to values stored with each notification.

Elsewhere, the server defines a custom `didUpdateStatus` notification:

```swift
extension NSNotification.Name {
    static var didUpdateStatus: NSNotification.Name {
        NSNotification.Name("didUpdateStatus")
    }
}
```

Whenever the server status changes, like after the user signs in, the server posts a notification of this custom type:

```swift
let notification = Notification(
    name: .didUpdateStatus,
    object: self,
    userInfo: ["status": "Signed In"])
NotificationCenter.default.post(notification)
```

The task attached to the [`Text`](text.md) view gets and displays the status value from the notification’s user information dictionary. When the user chooses a different server, SwiftUI cancels the task and creates a new one, which then waits for notifications from the new server.

## Parameters

- `id`: The value to observe for changes. The value must conform to the [`Equatable`](https://developer.apple.com/documentation/swift/equatable) protocol.
- `name`: Human readable name for the task. A name will be generated if this argument is `nil`.
- `priority`: The task priority to use when creating the asynchronous task. The default priority is [`userInitiated`](https://developer.apple.com/documentation/swift/taskpriority/userinitiated).
- `file`: File name used in default task name. SwiftUI uses the callsite of .task by default.
- `line`: Line number used in default task name. SwiftUI uses the callsite of .task by default.
- `action`: A closure that SwiftUI calls as an asynchronous task before the view appears. SwiftUI can automatically cancel the task after the view disappears before the action completes. If the `id` value changes, SwiftUI cancels and restarts the task.

## See Also

- [func task<T>(id: T, name: String?, priority: TaskPriority, file: String, line: Int, sending () async -> Void) -> some View](view/task(id:name:priority:file:line:_:).md)
  Adds a task to perform before this view appears or when a specified value changes.
- [func task(name: String?, executorPreference: any TaskExecutor, priority: TaskPriority, file: String, line: Int, action: sending () async -> Void) -> some View](view/task(name:executorpreference:priority:file:line:action:).md)
  Adds an asynchronous task to perform before this view appears.
- [func task(name: String?, priority: TaskPriority, file: String, line: Int, sending () async -> Void) -> some View](view/task(name:priority:file:line:_:).md)
  Adds an asynchronous task to perform before this view appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/task(id:name:executorpreference:priority:file:line:_:))*