---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxloghandler"
framework: "mlx-swift/MLX"
---

# MLXLogHandler

**Framework**: mlx-swift/MLX  
**Kind**: protocol  
**Role**: Protocol

Protocol for backing of MLXLogger.

## Declaration

```swift
protocol MLXLogHandler : Sendable
```

## Overview

Install with [`factory`](./mlxlogger/factory.md) or [`install()`](./stderrhandler/install%28%29.md)

## Topics

### Instance Methods
- [func log(level: LogLevel, message: () -> String, metadata: () -> [String : String]?, file: StaticString, function: StaticString, line: UInt)](./mlxloghandler/log%28level,message,metadata,file,function,line%29.md)

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [OSLogHandler](./osloghandler.md)
- [StderrHandler](./stderrhandler.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxloghandler)*