# versionChecksum

**Framework**: Core Data  
**Kind**: property

The Base64-encoded 128-bit model version hash.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var versionChecksum: String { get }
```

#### Discussion

This value is also available in the versioned model’s `VersionInfo.plist` file and in Xcode’s build log.

## See Also

- [var versionIdentifiers: Set<AnyHashable>](nsmanagedobjectmodel/versionidentifiers.md)
  The set of developer-defined version identifiers for the object model.
- [var entityVersionHashesByName: [String : Data]](nsmanagedobjectmodel/entityversionhashesbyname.md)
  The dictionary of the model’s entity names and their corresponding version hashes.
- [func isConfiguration(withName: String?, compatibleWithStoreMetadata: [String : Any]) -> Bool](nsmanagedobjectmodel/isconfiguration(withname:compatiblewithstoremetadata:).md)
  Returns a Boolean value that indicates whether a given configuration in the model is compatible with given metadata from a persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodel/versionchecksum)*