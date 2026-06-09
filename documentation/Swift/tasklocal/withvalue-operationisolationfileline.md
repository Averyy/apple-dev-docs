# withValue(_:operation:isolation:file:line:)

**Framework**: Swift  
**Kind**: method

Binds the task-local to the specific value for the duration of the asynchronous operation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@backDeployed(before: macOS 15.0, iOS 18.0, watchOS 11.0, tvOS 18.0, visionOS 2.0)
@discardableResult final func withValue<R>(_ valueDuringOperation: Value, operation: () async throws -> R, isolation: isolated (any Actor)? = #isolation, file: String = #fileID, line: UInt = #line) async rethrows -> R
```

#### Discussion

The value is available throughout the execution of the operation closure, including any `get` operations performed by child-tasks created during the execution of the operation closure.

If the same task-local is bound multiple times, be it in the same task, or in specific child tasks, the more specific (i.e. “deeper”) binding is returned when the value is read.

If the value is a reference type, it will be retained for the duration of the operation closure.

If this method is called form a context where no current Swift concurrency task is available, a fallback thread-local is used to manage the task locals and all existing semantics of task-locals are upheld as-if a task was actually available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/tasklocal/withvalue(_:operation:isolation:file:line:))*