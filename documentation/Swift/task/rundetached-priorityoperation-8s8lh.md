# runDetached(priority:operation:)

**Framework**: Swift  
**Kind**: method

Deprecated, available only for source compatibility reasons.

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
@discardableResult
static func runDetached(priority: TaskPriority? = nil, operation: @escaping @isolated(any) () async -> Success) -> Task<Success, Never>
```

## See Also

- [typealias Group](task/group.md)
- [typealias Handle](task/handle.md)
- [typealias Priority](task/priority.md)
- [static func CancellationError() -> CancellationError](task/cancellationerror.md)
- [func getResult() async -> Result<Success, Failure>](task/getresult.md)
- [func get() async throws -> Success](task/get-4i2gt.md)
- [func get() async -> Success](task/get-4ohks.md)
- [static func sleep(UInt64) async](task/sleep(_:).md)
- [static func suspend() async](task/suspend.md)
- [static func runDetached(priority: TaskPriority?, operation: () async throws -> Success) -> Task<Success, any Error>](task/rundetached(priority:operation:)-88zf5.md)
  Deprecated, available only for source compatibility reasons.
- [static func startSynchronously(name: String?, priority: TaskPriority?, sending () async -> Success) -> Task<Success, Never>](task/startsynchronously(name:priority:_:)-38jhc.md)
- [static func startSynchronously(name: String?, priority: TaskPriority?, sending () async throws -> Success) -> Task<Success, any Error>](task/startsynchronously(name:priority:_:)-47sar.md)
- [static func withCancellationHandler<T>(handler: () -> Void, operation: () async throws -> T) async rethrows -> T](task/withcancellationhandler(handler:operation:).md)
- [static func withGroup<TaskResult, BodyResult>(resultType: TaskResult.Type, returning: BodyResult.Type, body: (inout Task<Success, Failure>.Group<TaskResult>) async throws -> BodyResult) async rethrows -> BodyResult](task/withgroup(resulttype:returning:body:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/rundetached(priority:operation:)-8s8lh)*