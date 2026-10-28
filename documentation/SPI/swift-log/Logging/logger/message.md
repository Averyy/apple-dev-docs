---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/message"
framework: "swift-log/Logging"
---

# Logger.Message

**Framework**: swift-log/Logging  
**Kind**: struct  
**Role**: Structure

The content of log message.

## Declaration

```swift
struct Message
```

## Overview

It is usually created using string literals.

Example creating a `Logger.Message`:

```
let world: String = "world"
let myLogMessage: Logger.Message = "Hello \(world)"
```

Most commonly, `Logger.Message`s appear simply as the parameter to a logging method such as:

```
logger.info("Hello \(world)")
```

## Topics

### Creating a log message
- [init(stringLiteral: String)](./message/init%28stringliteral%29.md)
### Inspecting a log message
- [var description: String](./message/description.md)
### Type Aliases
- [Logger.Message.StringLiteralType](./message/stringliteraltype.md)
### Default Implementations
- [Equatable Implementations](./message/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](./message/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringInterpolation Implementations](./message/expressiblebystringinterpolation-implementations.md)
- [ExpressibleByStringLiteral Implementations](./message/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.ExpressibleByExtendedGraphemeClusterLiteral
- Swift.ExpressibleByStringInterpolation
- Swift.ExpressibleByStringLiteral
- Swift.ExpressibleByUnicodeScalarLiteral
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Sending general log messages
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, file: String, function: String, line: UInt)](./log%28level,_,metadata,file,function,line%29.md)
  Log a message using the log level you provide.
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./log%28level,_,metadata,source,file,function,line%29.md)
  Log a message using the log level and source that you provide.
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)?, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./log%28level,_,error,metadata,source,file,function,line%29.md)
  Log a message using the log level and source that you provide.
- [Logger.Level](./level.md)
  The log level.
- [typealias Metadata](./metadata.md)
  The type of the metadata storage.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/message)*