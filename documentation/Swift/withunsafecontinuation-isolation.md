# withUnsafeContinuation(isolation:_:)

**Framework**: Swift  
**Kind**: func

Invokes the passed in closure with a unsafe continuation for the current task.

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
func withUnsafeContinuation<T>(isolation: isolated (any Actor)? = #isolation, _ fn: (UnsafeContinuation<T, Never>) -> Void) async -> sending T
```

#### Return Value

The value continuation is resumed with.

#### Discussion

The body of the closure executes synchronously on the calling task, and once it returns the calling task is suspended. It is possible to immediately resume the task, or escape the continuation in order to complete it afterwards, which will then resume the suspended task.

You must invoke the continuation’s `resume` method exactly once.

Missing to invoke it (eventually) will cause the calling task to remain suspended indefinitely which will result in the task “hanging” as well as being leaked with no possibility to destroy it.

Unlike the “checked” continuation variant, the `UnsafeContinuation` does not detect or diagnose any kind of misuse, so you need to be extra careful to avoid calling `resume` twice or forgetting to call resume before letting go of the continuation object.

> **Note**: `withUnsafeThrowingContinuation(function:_:)`

`withUnsafeThrowingContinuation(function:_:)`

> **Note**: `withCheckedContinuation(function:_:)`

`withCheckedContinuation(function:_:)`

> **Note**: `withCheckedThrowingContinuation(function:_:)`

`withCheckedThrowingContinuation(function:_:)`

## Parameters

- `fn`: A closure that takes an   parameter.

## See Also

- [struct CheckedContinuation](checkedcontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [func withCheckedContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, Never>) -> Void) async -> sending T](withcheckedcontinuation(isolation:function:_:).md)
  Invokes the passed in closure with a checked continuation for the current task.
- [func withCheckedThrowingContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T](withcheckedthrowingcontinuation(isolation:function:_:).md)
  Invokes the passed in closure with a checked continuation for the current task.
- [struct UnsafeContinuation](unsafecontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, without correctness checking.
- [typealias UnsafeThrowingContinuation](unsafethrowingcontinuation.md)
- [func withUnsafeThrowingContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T](withunsafethrowingcontinuation(isolation:_:).md)
  Invokes the passed in closure with a unsafe continuation for the current task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withunsafecontinuation(isolation:_:))*