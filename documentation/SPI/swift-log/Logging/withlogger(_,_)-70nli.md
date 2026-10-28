---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/withlogger(_:_:)-70nli"
framework: "swift-log/Logging"
---

# withLogger(_:_:)

**Framework**: swift-log/Logging  
**Kind**: func  
**Role**: Function

Runs `operation` with `logger` bound to the task-local context.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated(nonsending)
func withLogger<Result, Failure>(_ logger: Logger, _ operation: nonisolated(nonsending)) async throws(Failure) -> Result where Failure : Error
```

## Return Value

The value returned by `operation`.

## Discussion

Code called within `operation` can read the logger via [`current`](./logger/current.md) without an explicit parameter. Binding a different logger with this overload **replaces** the current task-local logger; any metadata accumulated by an outer [`withLogger(mergingMetadata:_:)`](./withlogger%28mergingmetadata,_%29-3eduo.md) or [`withLogger(logLevel:handler:metadata:_:)`](./withlogger%28loglevel,handler,metadata,_%29-5nmw6.md) scope is not carried over. Use the modifying overloads to layer or replace aspects of the current logger instead.

This overload is the application-bootstrap binding mechanism: pass a `Logger` constructed via [`init(label:)`](./logger/init%28label%29.md) at your application entry point. Because [`init(label:)`](./logger/init%28label%29.md) consults `LoggingSystem.factory`, the constructed `Logger` only carries a useful handler once [`bootstrap(_:)`](./loggingsystem/bootstrap%28_%29.md) has been called. For mid-call-tree backend swaps that should work without bootstrap (tests, scoped routing), use [`withLogger(logLevel:handler:metadata:_:)`](./withlogger%28loglevel,handler,metadata,_%29-5nmw6.md) instead — it modifies the current logger’s handler in place without constructing a new one.

```swift
let logger = Logger(label: "app")
await withLogger(logger) { logger in
    logger.info("Application started")
    await handleRequests()  // reads Logger.current
}
```

## Parameters

- `logger`: The logger to bind for the duration of `operation`.
- `operation`: The async closure to run with `logger` bound. Receives `logger` as a parameter so the body does not need to re-read [`current`](./logger/current.md).

## See Also

### Task-local logger
- [static var current: Logger](./logger/current.md)
  The current task-local logger.
- [func withLogger<Result, Failure>(Logger, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](./withlogger%28_,_%29-3dt06.md)
  Runs `operation` with `logger` bound to the task-local context.
- [func withLogger<Result, Failure>(mergingMetadata: @autoclosure () -> Logger.Metadata, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](./withlogger%28mergingmetadata,_%29-2c7dy.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) that has `metadata` **layered on top of** the inherited base metadata. Keys present in `metadata` override existing keys with the same name. Other aspects (handler, log level, base metadata not in `metadata`) are preserved.
- [func withLogger<Result, Failure>(mergingMetadata: @autoclosure () -> Logger.Metadata, nonisolated(nonsending)) async throws(Failure) -> Result](./withlogger%28mergingmetadata,_%29-3eduo.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) that has `metadata` **layered on top of** the inherited base metadata. Keys present in `metadata` override existing keys with the same name. Other aspects (handler, log level, base metadata not in `metadata`) are preserved.
- [func withLogger<Result, Failure>(logLevel: Logger.Level?, handler: (any LogHandler)?, metadata: @autoclosure () -> Logger.Metadata?, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](./withlogger%28loglevel,handler,metadata,_%29-2pd9p.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) whose aspects are **replaced** by the provided arguments. `nil` parameters leave the corresponding aspect unchanged.
- [func withLogger<Result, Failure>(logLevel: Logger.Level?, handler: (any LogHandler)?, metadata: @autoclosure () -> Logger.Metadata?, nonisolated(nonsending)) async throws(Failure) -> Result](./withlogger%28loglevel,handler,metadata,_%29-5nmw6.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) whose aspects are **replaced** by the provided arguments. `nil` parameters leave the corresponding aspect unchanged.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/withlogger(_:_:)-70nli)*