---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loggingsystem/metadataprovider"
framework: "swift-log/Logging"
---

# metadataProvider

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Type Property

System wide [`Logger.MetadataProvider`](../logger/metadataprovider-swift.struct.md) that was configured during the logging system’s `bootstrap`.

## Declaration

```swift
static var metadataProvider: Logger.MetadataProvider? { get }
```

#### Discussion

When creating a [`Logger`](../logger.md) using the plain [`init(label:)`](../logger/init%28label%29.md) initializer, this metadata provider will be provided to it.

When using custom log handler factories, make sure to provide the bootstrapped metadata provider to them, or the metadata will not be filled in automatically using the provider on log-sites. While using a custom factory to avoid using the bootstrapped metadata provider may sometimes be useful, usually it will lead to un-expected behavior, so make sure to always propagate it to your handlers.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loggingsystem/metadataprovider)*