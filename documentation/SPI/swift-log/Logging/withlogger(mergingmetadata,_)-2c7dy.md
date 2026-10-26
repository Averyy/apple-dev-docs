---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/withlogger(mergingmetadata:_:)-2c7dy"
framework: "swift-log/Logging"
---

# withLogger(mergingMetadata:_:)

**Framework**: swift-log/Logging  
**Kind**: func  
**Role**: Function

Runs `operation` with a copy of [`current`](./logger/current.md) that has `metadata` **layered on top of** the inherited base metadata. Keys present in `metadata` override existing keys with the same name. Other aspects (handler, log level, base metadata not in `metadata`) are preserved.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func withLogger<Result, Failure>(mergingMetadata metadata: @autoclosure () -> Logger.Metadata, _ operation: (Logger) throws(Failure) -> Result) throws(Failure) -> Result where Failure : Error
```

#### Return Value

The value returned by `operation`.

#### Discussion

Use this overload at request boundaries and any point where context should accumulate. Nested [`withLogger(mergingMetadata:_:)`](./withlogger%28mergingmetadata,_%29-2c7dy.md) scopes layer on top of each other.

```swift
withLogger(mergingMetadata: ["request.id": "\(request.id)"]) { logger in
    logger.info("Handling request")
    withLogger(mergingMetadata: ["user.id": "\(user.id)"]) { logger in
        logger.info("Authenticated")  // sees both request.id and user.id
    }
}
```

## Parameters

- `metadata`: Metadata keys merged onto the inherited base metadata for the scope. Keys override existing values with the same name.
- `operation`: The closure to run with the merged logger bound. Receives the merged logger as a parameter.

## See Also

### Task-local logger
- [static var current: Logger](./logger/current.md)
  The current task-local logger.
- [func withLogger<Result, Failure>(Logger, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](./withlogger%28_,_%29-3dt06.md)
  Runs `operation` with `logger` bound to the task-local context.
- [func withLogger<Result, Failure>(Logger, nonisolated(nonsending)) async throws(Failure) -> Result](./withlogger%28_,_%29-70nli.md)
  Runs `operation` with `logger` bound to the task-local context.
- [func withLogger<Result, Failure>(mergingMetadata: @autoclosure () -> Logger.Metadata, nonisolated(nonsending)) async throws(Failure) -> Result](./withlogger%28mergingmetadata,_%29-3eduo.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) that has `metadata` **layered on top of** the inherited base metadata. Keys present in `metadata` override existing keys with the same name. Other aspects (handler, log level, base metadata not in `metadata`) are preserved.
- [func withLogger<Result, Failure>(logLevel: Logger.Level?, handler: (any LogHandler)?, metadata: @autoclosure () -> Logger.Metadata?, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](./withlogger%28loglevel,handler,metadata,_%29-2pd9p.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) whose aspects are **replaced** by the provided arguments. `nil` parameters leave the corresponding aspect unchanged.
- [func withLogger<Result, Failure>(logLevel: Logger.Level?, handler: (any LogHandler)?, metadata: @autoclosure () -> Logger.Metadata?, nonisolated(nonsending)) async throws(Failure) -> Result](./withlogger%28loglevel,handler,metadata,_%29-5nmw6.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) whose aspects are **replaced** by the provided arguments. `nil` parameters leave the corresponding aspect unchanged.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/withlogger(mergingmetadata:_:)-2c7dy)*