---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/osloghandler"
framework: "mlx-swift/MLX"
---

# OSLogHandler

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

On systems that support it, a log handler that is backed by OSLog.

## Declaration

```swift
struct OSLogHandler
```

## Topics

### Initializers
- [init(label: String)](./osloghandler/init%28label%29.md)
### Instance Methods
- [func log(level: LogLevel, message: () -> String, metadata: () -> [String : String]?, file: StaticString, function: StaticString, line: UInt)](./osloghandler/log%28level,message,metadata,file,function,line%29.md)
### Type Methods
- [static func install()](./osloghandler/install%28%29.md)

## Relationships

### Conforms To
- [MLXLogHandler](./mlxloghandler.md)
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/osloghandler)*