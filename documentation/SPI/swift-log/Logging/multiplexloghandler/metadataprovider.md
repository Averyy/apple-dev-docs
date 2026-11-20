---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler/metadataprovider"
framework: "swift-log/Logging"
---

# metadataProvider

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Instance Property

The metadata provider.

## Declaration

```swift
var metadataProvider: Logger.MetadataProvider? { get set }
```

## Discussion

Setting this property sets the provider on all underlying handlers and replaces the provider passed to [`init(_:metadataProvider:)`](./init%28_,metadataprovider%29.md).

## See Also

### Inspecting a log handler
- [var logLevel: Logger.Level](./loglevel.md)
  Get or set the log level configured for this `Logger`.
- [var metadata: Logger.Metadata](./metadata.md)
  Get or set the entire metadata storage as a dictionary.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler/metadataprovider)*