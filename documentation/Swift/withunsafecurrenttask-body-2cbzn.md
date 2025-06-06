# withUnsafeCurrentTask(body:)

**Framework**: Swift  
**Kind**: func

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
func withUnsafeCurrentTask<T>(body: (UnsafeCurrentTask?) async throws -> T) async rethrows -> T
```

## See Also

- [func withUnsafeCurrentTask<T>(body: (UnsafeCurrentTask?) throws -> T) rethrows -> T](withunsafecurrenttask(body:)-6gvhl.md)
  Calls a closure with an unsafe reference to the current task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withunsafecurrenttask(body:)-2cbzn)*