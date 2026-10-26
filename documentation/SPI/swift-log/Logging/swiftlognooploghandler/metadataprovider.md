---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/swiftlognooploghandler/metadataprovider"
framework: "swift-log/Logging"
---

# metadataProvider

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Instance Property

Default implementation for a metadata provider that defaults to nil.

## Declaration

```swift
var metadataProvider: Logger.MetadataProvider? { get set }
```

#### Discussion

This default exists in order to facilitate the source-compatible introduction of the `metadataProvider` protocol requirement.

## See Also

### Inspecting a log handler
- [var logLevel: Logger.Level](./loglevel.md)
  Get or set the log level configured for this `Logger`.
- [var metadata: Logger.Metadata](./metadata.md)
  Get or set the entire metadata storage as a dictionary.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/swiftlognooploghandler/metadataprovider)*