# getResult()

**Framework**: Swift  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
func getResult() async -> Result<Success, Failure>
```

## See Also

- [typealias Group](task/group.md)
- [typealias Handle](task/handle.md)
- [typealias Priority](task/priority.md)
- [static func CancellationError() -> CancellationError](task/cancellationerror.md)
- [func get() async throws -> Success](task/get-4i2gt.md)
- [static func sleep(UInt64) async](task/sleep(_:).md)
- [static func suspend() async](task/suspend.md)
- [static func runDetached(priority: TaskPriority?, operation: () async throws -> Success) -> Task<Success, Failure>](task/rundetached(priority:operation:).md)
- [static func withCancellationHandler<T>(handler: () -> Void, operation: () async throws -> T) async rethrows -> T](task/withcancellationhandler(handler:operation:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/getresult())*