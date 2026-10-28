---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accesslogger/init(logger:level:message:)"
framework: "swift-configuration/Configuration"
---

# init(logger:level:message:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new access logger that reports configuration access events.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(logger: Logger, level: Logger.Level = .debug, message: Logger.Message = "Config value accessed")
```

## Discussion

```swift
let logger = Logger(label: "my.app.config")

// Log at debug level by default
let accessLogger = AccessLogger(logger: logger)

// Customize the log level
let accessLogger = AccessLogger(logger: logger, level: .info)
```

## Parameters

- `logger`: The logger to emit access events to.
- `level`: The log level for access events. Defaults to `.debug`.
- `message`: The static message text for log entries. Defaults to “Config value accessed”.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/accesslogger/init(logger:level:message:))*