---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/subscript(metadatakey:)"
framework: "swift-log/Logging"
---

# subscript(metadataKey:)

**Framework**: swift-log/Logging  
**Kind**: subscript  
**Role**: Instance Subscript

Log a message using the log level and attributed metadata that you provide.

## Declaration

```swift
subscript(metadataKey metadataKey: String) -> Logger.Metadata.Value? { get set }
```

## Mentions

- [Disable log levels during compilation](../disableloglevelsduringcompilation.md)

## Overview

If the `logLevel` passed to this method is more severe than the `Logger`’s [`logLevel`](./loglevel.md), the library logs the message, otherwise nothing will happen.

Add, change, or remove a logging metadata item.

> **Note**: Changing the logging metadata only affects the instance of the `Logger` where you change it.

## See Also

### Adjusting logger metadata
- [Logger.MetadataValue](./metadatavalue.md)
  A logging metadata value.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/subscript(metadatakey:))*