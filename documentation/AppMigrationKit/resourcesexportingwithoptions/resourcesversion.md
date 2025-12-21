# resourcesVersion

**Framework**: AppMigrationKit  
**Kind**: property  
**Required**: Yes

A property that identifies the version of the format the export uses.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var resourcesVersion: String { get }
```

#### Discussion

AppMigrationKit transmits this value along with the exported resources. Use this value to distinguish between potentially incompatible versions of your app’s data.

## See Also

- [var resourcesSizeEstimate: Int](resourcesexportingwithoptions/resourcessizeestimate.md)
  The estimated size of all resources to export, in bytes.
- [var resourcesCompressible: Bool](resourcesexportingwithoptions/resourcescompressible.md)
  A property that indicates whether the archiver attempts to compress the resources passed to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesexportingwithoptions/resourcesversion)*