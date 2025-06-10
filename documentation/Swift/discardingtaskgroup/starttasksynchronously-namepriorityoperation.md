# startTaskSynchronously(name:priority:operation:)

**Framework**: Swift  
**Kind**: method

Create and immediately start running a new child task in the context of the calling thread/task.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func startTaskSynchronously(name: String? = nil, priority: TaskPriority? = nil, operation: sending @escaping () async -> Void)
```

#### Discussion

This function  the created task on the calling context. The task will continue executing on the caller’s context until it suspends, and after suspension will resume on the adequate executor. For a nonisolated operation this means running on the global concurrent pool, and on an isolated operation it means the appropriate executor of that isolation context.

As indicated by the lack of `async` on this method, this method does  suspend, and instead takes over the calling task’s (thread’s) execution in a synchronous manner.

Other than the execution semantics discussed above, the created task is semantically equivalent to its basic version which can be created using `DiscardingTaskGroup/addTask`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/discardingtaskgroup/starttasksynchronously(name:priority:operation:))*