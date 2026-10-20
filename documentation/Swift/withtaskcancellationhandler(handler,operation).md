# withTaskCancellationHandler(handler:operation:)

**Framework**: Swift  
**Kind**: func  
**Role**: Function

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
func withTaskCancellationHandler<T>(handler: @Sendable () -> Void, operation: () async throws -> T) async rethrows -> T
```

## See Also

### Deprecated
- [typealias Group](./task/group.md)
- [typealias Handle](./task/handle.md)
- [typealias Priority](./task/priority.md)
- [static func CancellationError() -> CancellationError](./task/cancellationerror%28%29.md)
- [func getResult() async -> Result<Success, Failure>](./task/getresult%28%29.md)
- [func get() async throws -> Success](./task/get%28%29-4i2gt.md)
- [func get() async -> Success](./task/get%28%29-4ohks.md)
- [static func sleep(UInt64) async](./task/sleep%28_%29.md)
- [static func suspend() async](./task/suspend%28%29.md)
- [static func runDetached(priority: TaskPriority?, operation: () async throws -> Success) -> Task<Success, any Error>](./task/rundetached%28priority,operation%29-88zf5.md)
  Deprecated, available only for source compatibility reasons.
- [static func runDetached(priority: TaskPriority?, operation: () async -> Success) -> Task<Success, Never>](./task/rundetached%28priority,operation%29-8s8lh.md)
  Deprecated, available only for source compatibility reasons.
- [static func withCancellationHandler<T>(handler: () -> Void, operation: () async throws -> T) async rethrows -> T](./task/withcancellationhandler%28handler,operation%29.md)
- [static func withGroup<TaskResult, BodyResult>(resultType: TaskResult.Type, returning: BodyResult.Type, body: (inout Task<Success, Failure>.Group<TaskResult>) async throws -> BodyResult) async rethrows -> BodyResult](./task/withgroup%28resulttype,returning,body%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withtaskcancellationhandler(handler:operation:))*