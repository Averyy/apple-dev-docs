# resourcesCompressible

**Framework**: AppMigrationKit  
**Kind**: property  
**Required**: Yes

A property that indicates whether the archiver attempts to compress the resources passed to it.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var resourcesCompressible: Bool { get }
```

#### Discussion

If the majority of resources to export are already compressed files – such as most image file formats – implement this property to return `false`, since the files won’t benefit from further compression. On the other hand, if most exported resources are text files or other compressible data, return `true` to allow AppMigrationKit to compress them. The compression allows AppMigrationKit to optimize the migration process.

## See Also

- [var resourcesSizeEstimate: Int](resourcesexportingwithoptions/resourcessizeestimate.md)
  The estimated size of all resources to export, in bytes.
- [var resourcesVersion: String](resourcesexportingwithoptions/resourcesversion.md)
  A property that identifies the version of the format the export uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/resourcesexportingwithoptions/resourcescompressible)*