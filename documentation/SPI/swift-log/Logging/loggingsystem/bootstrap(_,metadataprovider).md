---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loggingsystem/bootstrap(_:metadataprovider:)"
framework: "swift-log/Logging"
---

# bootstrap(_:metadataProvider:)

**Framework**: swift-log/Logging  
**Kind**: method  
**Role**: Type Method

A one-time configuration function that globally selects the implementation for your desired logging backend.

## Declaration

```swift
@preconcurrency
static func bootstrap(_ factory: @escaping @Sendable (String, Logger.MetadataProvider?) -> any LogHandler, metadataProvider: Logger.MetadataProvider?)
```

#### Discussion

> ⚠️ **Warning**:  `bootstrap` can be called at maximum once in any given program, calling it more than once will lead to undefined behavior, most likely a crash.

## Parameters

- `factory`: A closure that provides a [`Logger`](../logger.md) label identifier and produces an instance of the [`LogHandler`](../loghandler.md).
- `metadataProvider`: The `MetadataProvider` used to inject runtime-generated metadata from the execution context.

## See Also

### Initializing the logging system
- [static func bootstrap(@Sendable (String) -> any LogHandler)](./bootstrap%28_%29.md)
  A one-time configuration function that globally selects the implementation for your desired logging backend.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loggingsystem/bootstrap(_:metadataprovider:))*