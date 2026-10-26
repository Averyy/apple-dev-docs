---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loggingsystem/bootstrap(_:)"
framework: "swift-log/Logging"
---

# bootstrap(_:)

**Framework**: swift-log/Logging  
**Kind**: method  
**Role**: Type Method

A one-time configuration function that globally selects the implementation for your desired logging backend.

## Declaration

```swift
@preconcurrency
static func bootstrap(_ factory: @escaping @Sendable (String) -> any LogHandler)
```

## Mentions

- [003: Logger propagation in libraries](../api-003-acceptingloggers.md)
- [004: Testing code that logs](../api-004-testinglogging.md)

#### Discussion

> ⚠️ **Warning**:  `bootstrap` can be called at maximum once in any given program, calling it more than once will lead to undefined behavior, most likely a crash.

## Parameters

- `factory`: A closure that provides a [`Logger`](../logger.md) label identifier and produces an instance of the [`LogHandler`](../loghandler.md).

## See Also

### Initializing the logging system
- [static func bootstrap(@Sendable (String, Logger.MetadataProvider?) -> any LogHandler, metadataProvider: Logger.MetadataProvider?)](./bootstrap%28_,metadataprovider%29.md)
  A one-time configuration function that globally selects the implementation for your desired logging backend.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loggingsystem/bootstrap(_:))*