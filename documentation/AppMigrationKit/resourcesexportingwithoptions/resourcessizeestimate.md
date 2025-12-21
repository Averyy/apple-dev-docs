# resourcesSizeEstimate

**Framework**: AppMigrationKit  
**Kind**: property  
**Required**: Yes

The estimated size of all resources to export, in bytes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var resourcesSizeEstimate: Int { get async }
```

#### Discussion

AppMigrationKit uses this property when preflighting the app transfer to estimate the data size required for the transfer.

## See Also

- [var resourcesVersion: String](resourcesexportingwithoptions/resourcesversion.md)
  A property that identifies the version of the format the export uses.
- [var resourcesCompressible: Bool](resourcesexportingwithoptions/resourcescompressible.md)
  A property that indicates whether the archiver attempts to compress the resources passed to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesexportingwithoptions/resourcessizeestimate)*