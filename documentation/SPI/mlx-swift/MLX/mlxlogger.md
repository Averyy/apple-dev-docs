---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlogger"
framework: "mlx-swift/MLX"
---

# MLXLogger

**Framework**: mlx-swift/MLX  
**Kind**: class  
**Role**: Class

Thin wrapper for logging in MLX and MLX libraries.  This provides a hook for library code if it needs logging without adding a dependency or requiring a certain logging backend.

## Declaration

```swift
final class MLXLogger
```

#### Overview

By default it will log to `OSLog` (macOS, iOS) or `stderr` (others).  Developers can override the backing by implementing [`MLXLogHandler`](./mlxloghandler.md) and installing it with [`factory`](./mlxlogger/factory.md), e.g.

```swift
MLXLogger.factory = { StderrHandler(label: $0) }
```

The factory is used at the time of the first log for the given logger – whatever factory is installed at that time will be used.

Callers can use this the same way that `swift-log` is used:

```swift
private let logger = MLXLogger(label: "KVCache")

func ...() {
    logger.error("Failed to ...")
}
```

## Topics

### Initializers
- [init(label: String)](./mlxlogger/init%28label%29.md)
### Instance Methods
- [func debug(@autoclosure () -> String, metadata: @autoclosure () -> [String : String]?, file: StaticString, function: StaticString, line: UInt)](./mlxlogger/debug%28_,metadata,file,function,line%29.md)
  Log a debug message.
- [func error(@autoclosure () -> String, metadata: @autoclosure () -> [String : String]?, file: StaticString, function: StaticString, line: UInt)](./mlxlogger/error%28_,metadata,file,function,line%29.md)
  Log an error message.
- [func info(@autoclosure () -> String, metadata: @autoclosure () -> [String : String]?, file: StaticString, function: StaticString, line: UInt)](./mlxlogger/info%28_,metadata,file,function,line%29.md)
  Log a info message.
- [func log(level: LogLevel, message: @autoclosure () -> String, metadata: @autoclosure () -> [String : String]?, file: StaticString, function: StaticString, line: UInt)](./mlxlogger/log%28level,message,metadata,file,function,line%29.md)
  Log with the given level and message.
- [func trace(@autoclosure () -> String, metadata: @autoclosure () -> [String : String]?, file: StaticString, function: StaticString, line: UInt)](./mlxlogger/trace%28_,metadata,file,function,line%29.md)
  Log a trace message.
- [func warning(@autoclosure () -> String, metadata: @autoclosure () -> [String : String]?, file: StaticString, function: StaticString, line: UInt)](./mlxlogger/warning%28_,metadata,file,function,line%29.md)
  Log a warning message.
### Type Properties
- [static var factory: MLXLogHandlerFactory](./mlxlogger/factory.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxlogger)*