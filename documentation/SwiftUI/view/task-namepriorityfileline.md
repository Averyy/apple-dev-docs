# task(name:priority:file:line:_:)

**Framework**: SwiftUI  
**Kind**: method

Adds an asynchronous task to perform before this view appears.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@export(implementation)
nonisolated func task(name: String? = nil, priority: TaskPriority = .userInitiated, file: String = #fileID, line: Int = #line, _ action: sending @escaping @isolated(any) () async -> Void) -> some View
```

#### Return Value

A view that runs the specified action asynchronously before the view appears.

#### Discussion

Use this modifier to perform an asynchronous task with a lifetime that matches that of the modified view. If the task doesn’t finish before SwiftUI removes the view or the view changes identity, SwiftUI cancels the task.

Use the `await` keyword inside the task to wait for an asynchronous call to complete, or to wait on the values of an [`AsyncSequence`](https://developer.apple.com/documentation/swift/asyncsequence) instance. For example, you can modify a [`Text`](text.md) view to start a task that loads content from a remote resource:

```swift
let url = URL(string: "https://example.com")!
@State private var message = "Loading..."

var body: some View {
    Text(message)
        .task {
            do {
                var receivedLines = [String]()
                for try await line in url.lines {
                    receivedLines.append(line)
                    message = "Received \(receivedLines.count) lines"
                }
            } catch {
                message = "Failed to load"
            }
        }
}
```

This example uses the [`lines`](https://developer.apple.com/documentation/foundation/url/lines) method to get the content stored at the specified [`URL`](https://developer.apple.com/documentation/foundation/url) as an asynchronous sequence of strings. When each new line arrives, the body of the `for`-`await`-`in` loop stores the line in an array of strings and updates the content of the text view to report the latest line count.

The task is created by `Task.immediate`. Its action begins execution synchronously until it suspends at the first `await`.

## Parameters

- `name`: Human readable name for the task. A name will be generated if this argument is `nil`. This value is a no-op prior to iOS 26.4, macOS 26.4, watchOS 26.4, tvOS 26.4, and visionOS 26.4.
- `priority`: The task priority to use when creating the asynchronous task. The default priority is [`userInitiated`](https://developer.apple.com/documentation/swift/taskpriority/userinitiated).
- `file`: File name used in default task name. SwiftUI uses the callsite of .task by default. This value is a no-op prior to iOS 26.4, macOS 26.4, watchOS 26.4, tvOS 26.4, and visionOS 26.4.
- `line`: Line number used in default task name. SwiftUI uses the callsite of .task by default. This value is a no-op prior to iOS 26.4, macOS 26.4, watchOS 26.4, tvOS 26.4, and visionOS 26.4.
- `action`: A closure that SwiftUI calls as an asynchronous task before the view appears. SwiftUI will automatically cancel the task at some point after the view disappears before the action completes.

## See Also

- [func task<T>(id: T, name: String?, executorPreference: any TaskExecutor, priority: TaskPriority, file: String, line: Int, sending () async -> Void) -> some View](view/task(id:name:executorpreference:priority:file:line:_:).md)
  Adds a task to perform before this view appears or when a specified value changes.
- [func task<T>(id: T, name: String?, priority: TaskPriority, file: String, line: Int, sending () async -> Void) -> some View](view/task(id:name:priority:file:line:_:).md)
  Adds a task to perform before this view appears or when a specified value changes.
- [func task(name: String?, executorPreference: any TaskExecutor, priority: TaskPriority, file: String, line: Int, action: sending () async -> Void) -> some View](view/task(name:executorpreference:priority:file:line:action:).md)
  Adds an asynchronous task to perform before this view appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/task(name:priority:file:line:_:))*