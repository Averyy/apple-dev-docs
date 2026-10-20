# compressedBytes

**Framework**: AppMigrationKit  
**Kind**: property  
**Role**: Instance Property

The number of compressed bytes written to the migration infrastructure, if the extension uses compression.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
let compressedBytes: Int?
```

#### Discussion

Use this information in testing to determine if your extension might benefit from data compression during migration.

If the extension doesn’t use compression, this property is `nil`.

## See Also

### Inspecting data size properties
- [let uncompressedBytes: Int](./uncompressedbytes.md)
  The number of uncompressed bytes written to the exporter.
- [let sizeEstimate: Int](./sizeestimate.md)
  The size estimate provided by the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appmigrationkit/appmigrationtester/devicetodeviceexportproperties/compressedbytes)*