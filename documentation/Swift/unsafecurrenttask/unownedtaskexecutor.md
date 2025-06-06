# unownedTaskExecutor

**Framework**: Swift  
**Kind**: property

The current [`TaskExecutor`](taskexecutor.md) preference, if this task has one configured.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var unownedTaskExecutor: UnownedTaskExecutor? { get }
```

#### Discussion

The executor may be used to compare for equality with an expected executor preference.

The lifetime of an executor is not guaranteed by an [`UnownedTaskExecutor`](unownedtaskexecutor.md), so accessing it must be handled with great case – and the program must use other means to guarantee the executor remains alive while it is in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafecurrenttask/unownedtaskexecutor)*