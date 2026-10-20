# get()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

> **Deprecated**: get() has been replaced by .value

## Declaration

```swift
func get() async -> Success
```

Available when `Success` conforms to `Sendable` and `Failure` is `Never`.

## See Also

### Deprecated
- [typealias Group](./group.md)
- [typealias Handle](./handle.md)
- [typealias Priority](./priority.md)
- [static func CancellationError() -> CancellationError](./cancellationerror%28%29.md)
- [func getResult() async -> Result<Success, Failure>](./getresult%28%29.md)
- [func get() async throws -> Success](./get%28%29-4i2gt.md)
- [static func sleep(UInt64) async](./sleep%28_%29.md)
- [static func suspend() async](./suspend%28%29.md)
- [static func runDetached(priority: TaskPriority?, operation: () async throws -> Success) -> Task<Success, any Error>](./rundetached%28priority,operation%29-88zf5.md)
  Deprecated, available only for source compatibility reasons.
- [static func runDetached(priority: TaskPriority?, operation: () async -> Success) -> Task<Success, Never>](./rundetached%28priority,operation%29-8s8lh.md)
  Deprecated, available only for source compatibility reasons.
- [static func withCancellationHandler<T>(handler: () -> Void, operation: () async throws -> T) async rethrows -> T](./withcancellationhandler%28handler,operation%29.md)
- [static func withGroup<TaskResult, BodyResult>(resultType: TaskResult.Type, returning: BodyResult.Type, body: (inout Task<Success, Failure>.Group<TaskResult>) async throws -> BodyResult) async rethrows -> BodyResult](./withgroup%28resulttype,returning,body%29.md)
- [func withTaskCancellationHandler<T>(handler: () -> Void, operation: () async throws -> T) async rethrows -> T](../withtaskcancellationhandler%28handler,operation%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/get()-4ohks)*