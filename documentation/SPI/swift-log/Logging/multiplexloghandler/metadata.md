---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler/metadata"
framework: "swift-log/Logging"
---

# metadata

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Instance Property

Get or set the entire metadata storage as a dictionary.

## Declaration

```swift
var metadata: Logger.Metadata { get set }
```

## Discussion

The getter merges the metadata of the underlying handlers in initialization order. On a key conflict, the first handler’s value wins, as in [`subscript(metadataKey:)`](./subscript%28metadatakey%29.md). The dictionary does not contain values from metadata providers.

## See Also

### Inspecting a log handler
- [var logLevel: Logger.Level](./loglevel.md)
  Get or set the log level configured for this `Logger`.
- [var metadataProvider: Logger.MetadataProvider?](./metadataprovider.md)
  The metadata provider.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler/metadata)*