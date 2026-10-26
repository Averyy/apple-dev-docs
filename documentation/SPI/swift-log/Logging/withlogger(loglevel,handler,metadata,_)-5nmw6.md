---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/withlogger(loglevel:handler:metadata:_:)-5nmw6"
framework: "swift-log/Logging"
---

# withLogger(logLevel:handler:metadata:_:)

**Framework**: swift-log/Logging  
**Kind**: func  
**Role**: Function

Runs `operation` with a copy of [`current`](./logger/current.md) whose aspects are **replaced** by the provided arguments. `nil` parameters leave the corresponding aspect unchanged.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
(nonsending) func withLogger<Result, Failure>(logLevel: Logger.Level? = nil, handler: (any LogHandler)? = nil, metadata: @autoclosure () -> Logger.Metadata? = nil, _ operation: nonisolated(nonsending)) async throws(Failure) -> Result where Failure : Error
```

#### Return Value

The value returned by `operation`.

#### Discussion

Unlike [`withLogger(mergingMetadata:_:)`](./withlogger%28mergingmetadata,_%29-3eduo.md), which layers metadata on top of the inherited base, this overload **replaces** the base metadata when `metadata` is non-nil. Pass `metadata: [:]` to wipe the inherited metadata entirely for the scope.

With no arguments, this overload re-binds [`current`](./logger/current.md) unchanged — a convenient way to extract it into a local variable for repeated use inside the closure.

```swift
withLogger(mergingMetadata: ["request.id": "\(request.id)"]) { _ in
    // Start a background job with metadata unrelated to the request that scheduled it.
    withLogger(metadata: ["job.id": "\(job.id)"]) { logger in
        logger.info("running")  // metadata: job.id only — request.id wiped
    }
}
```

When no `withLogger` scope has been set up, [`current`](./logger/current.md) (and therefore this function) returns the process-wide unbound default — a `Logger(label: "")` cached from the first time the task-local is touched. Bootstrap before reading [`current`](./logger/current.md) for predictable backend selection.

## Parameters

- `logLevel`: When non-nil, replaces the current log level for the scope. When `nil`, the inherited log level is preserved.
- `handler`: When non-nil, replaces the current logger’s handler for the scope. Useful in tests to route logs through an `InMemoryLogHandler` or similar while keeping the caller’s label. When `nil`, the inherited handler is preserved.
- `metadata`: When non-nil, replaces the handler’s base metadata dictionary for the scope. Pass `[:]` to erase inherited metadata; pass a fresh dictionary to start a scope from a known state. When `nil`, the inherited base metadata is preserved.
- `operation`: The async closure to run with the modified logger bound. Receives the modified logger as a parameter.

## See Also

### Task-local logger
- [static var current: Logger](./logger/current.md)
  The current task-local logger.
- [func withLogger<Result, Failure>(Logger, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](./withlogger%28_,_%29-3dt06.md)
  Runs `operation` with `logger` bound to the task-local context.
- [func withLogger<Result, Failure>(Logger, nonisolated(nonsending)) async throws(Failure) -> Result](./withlogger%28_,_%29-70nli.md)
  Runs `operation` with `logger` bound to the task-local context.
- [func withLogger<Result, Failure>(mergingMetadata: @autoclosure () -> Logger.Metadata, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](./withlogger%28mergingmetadata,_%29-2c7dy.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) that has `metadata` **layered on top of** the inherited base metadata. Keys present in `metadata` override existing keys with the same name. Other aspects (handler, log level, base metadata not in `metadata`) are preserved.
- [func withLogger<Result, Failure>(mergingMetadata: @autoclosure () -> Logger.Metadata, nonisolated(nonsending)) async throws(Failure) -> Result](./withlogger%28mergingmetadata,_%29-3eduo.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) that has `metadata` **layered on top of** the inherited base metadata. Keys present in `metadata` override existing keys with the same name. Other aspects (handler, log level, base metadata not in `metadata`) are preserved.
- [func withLogger<Result, Failure>(logLevel: Logger.Level?, handler: (any LogHandler)?, metadata: @autoclosure () -> Logger.Metadata?, (Logger) throws(Failure) -> Result) throws(Failure) -> Result](./withlogger%28loglevel,handler,metadata,_%29-2pd9p.md)
  Runs `operation` with a copy of [`current`](./logger/current.md) whose aspects are **replaced** by the provided arguments. `nil` parameters leave the corresponding aspect unchanged.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/withlogger(loglevel:handler:metadata:_:)-5nmw6)*