---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/stderrhandler"
framework: "mlx-swift/MLX"
---

# StderrHandler

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

A logger that logs to `stderr`.

## Declaration

```swift
struct StderrHandler
```

#### Overview

Callers can set `StderrHandler.logLevel` to filter output by level.

## Topics

### Initializers
- [init(label: String)](./stderrhandler/init%28label%29.md)
### Instance Methods
- [func log(level: LogLevel, message: @autoclosure () -> String, metadata: @autoclosure () -> [String : String]?, file: StaticString, function: StaticString, line: UInt)](./stderrhandler/log%28level,message,metadata,file,function,line%29.md)
### Type Properties
- [static var logLevel: LogLevel](./stderrhandler/loglevel.md)
  Get or set the lowest log level.  Default is `.info`.
### Type Methods
- [static func install()](./stderrhandler/install%28%29.md)

## Relationships

### Conforms To
- [MLXLogHandler](./mlxloghandler.md)
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/stderrhandler)*