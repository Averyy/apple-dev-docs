# currentExecutor

**Framework**: Swift  
**Kind**: property

Get the current executor; this is the executor that the currently executing task is executing on.

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
static var currentExecutor: any Executor { get }
```

#### Discussion

This will return, in order of preference:

1. The custom executor associated with an `Actor` on which we are currently running, or
2. The preferred executor for the currently executing `Task`, or
3. The task executor for the current thread

If none of these exist, returns the default executor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/currentexecutor)*