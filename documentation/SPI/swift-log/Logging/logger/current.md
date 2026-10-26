---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/current"
framework: "swift-log/Logging"
---

# current

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Type Property

The current task-local logger.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
static var current: Logger { get }
```

## Mentions

- [003: Logger propagation in libraries](../api-003-acceptingloggers.md)
- [004: Testing code that logs](../api-004-testinglogging.md)
- [Implementing a log handler](../implementingaloghandler.md)

#### Discussion

Returns the logger bound by the nearest enclosing [`withLogger(_:_:)`](../withlogger%28_,_%29-70nli.md) scope. If none is active, returns the process-wide unbound default — a `Logger(label: "")` constructed via `LoggingSystem.factory` the first time the task-local is touched, then reused for the lifetime of the process. The empty label is the deliberate diagnostic signal that no `withLogger` scope was set up before the read.

Because the unbound default is captured at first access, [`bootstrap(_:)`](../loggingsystem/bootstrap%28_%29.md) must be called before any task-local logger API is exercised; otherwise the unbound default uses the swift-log default [`StreamLogHandler`](../streamloghandler.md) and a later bootstrap is not visible to [`current`](./current.md) outside of a `withLogger` scope.

Task-local values propagate through structured concurrency (`async let`, `withTaskGroup`, child `Task {}`) but are **not** inherited by `Task.detached`. Capture the logger explicitly across detached boundaries.

## See Also

### Task-local logger
- [func withLogger<Result, Failure>(Logger, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](../withlogger%28_,_%29-3dt06.md)
  Runs `operation` with `logger` bound to the task-local context.
- [func withLogger<Result, Failure>(Logger, nonisolated(nonsending)) async throws(Failure) -> Result](../withlogger%28_,_%29-70nli.md)
  Runs `operation` with `logger` bound to the task-local context.
- [func withLogger<Result, Failure>(mergingMetadata: @autoclosure () -> Logger.Metadata, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](../withlogger%28mergingmetadata,_%29-2c7dy.md)
  Runs `operation` with a copy of [`current`](./current.md) that has `metadata` **layered on top of** the inherited base metadata. Keys present in `metadata` override existing keys with the same name. Other aspects (handler, log level, base metadata not in `metadata`) are preserved.
- [func withLogger<Result, Failure>(mergingMetadata: @autoclosure () -> Logger.Metadata, nonisolated(nonsending)) async throws(Failure) -> Result](../withlogger%28mergingmetadata,_%29-3eduo.md)
  Runs `operation` with a copy of [`current`](./current.md) that has `metadata` **layered on top of** the inherited base metadata. Keys present in `metadata` override existing keys with the same name. Other aspects (handler, log level, base metadata not in `metadata`) are preserved.
- [func withLogger<Result, Failure>(logLevel: Logger.Level?, handler: (any LogHandler)?, metadata: @autoclosure () -> Logger.Metadata?, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](../withlogger%28loglevel,handler,metadata,_%29-2pd9p.md)
  Runs `operation` with a copy of [`current`](./current.md) whose aspects are **replaced** by the provided arguments. `nil` parameters leave the corresponding aspect unchanged.
- [func withLogger<Result, Failure>(logLevel: Logger.Level?, handler: (any LogHandler)?, metadata: @autoclosure () -> Logger.Metadata?, nonisolated(nonsending)) async throws(Failure) -> Result](../withlogger%28loglevel,handler,metadata,_%29-5nmw6.md)
  Runs `operation` with a copy of [`current`](./current.md) whose aspects are **replaced** by the provided arguments. `nil` parameters leave the corresponding aspect unchanged.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/current)*