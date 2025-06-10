# checkIsolated()

**Framework**: Swift  
**Kind**: method

Last resort “fallback” isolation check, called when the concurrency runtime is comparing executors e.g. during `assumeIsolated()` and is unable to prove serial equivalence between the expected (this object), and the current executor.

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
final func checkIsolated()
```

#### Discussion

During executor comparison, the Swift concurrency runtime attempts to compare current and expected executors in a few ways (including “complex” equality between executors (see [`isSameExclusiveExecutionContext(other:)`](dummymainexecutor/issameexclusiveexecutioncontext(other:).md)), and if all those checks fail, this method is invoked on the expected executor.

This method MUST crash if it is unable to prove that the current execution context belongs to this executor. At this point usual executor comparison would have already failed, though the executor may have some external tracking of threads it owns, and may be able to prove isolation nevertheless.

A default implementation is provided that unconditionally crashes the program, and prevents calling code from proceeding with potentially not thread-safe execution.

> ⚠️ **Warning**: This method must crash and halt program execution if unable to prove the isolation of the calling context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/dummymainexecutor/checkisolated())*