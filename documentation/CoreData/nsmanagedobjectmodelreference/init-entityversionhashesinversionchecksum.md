# init(entityVersionHashes:in:versionChecksum:)

**Framework**: Core Data  
**Kind**: init

Creates an object model reference with the entities corresponding to the specified entity version hashes.

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
init(entityVersionHashes versionHash: [AnyHashable : Any], in bundle: Bundle?, versionChecksum: String)
```

#### Discussion

To determine an object model’s version checksum, use its [`versionChecksum`](nsmanagedobjectmodel/versionchecksum.md) property. Alternatively, you can find the checksum in the versioned model’s `VersionInfo.plist` file or in Xcode’s build log.

## Parameters

- `versionHash`: The dictionary of entity names and their corresponding version hashes.
- `bundle`: The bundle to search.
- `versionChecksum`: The checksum of the object model’s version.

## See Also

- [init(model: NSManagedObjectModel, versionChecksum: String)](nsmanagedobjectmodelreference/init(model:versionchecksum:).md)
  Creates an object model reference for the specified model.
- [init(fileURL: URL, versionChecksum: String)](nsmanagedobjectmodelreference/init(fileurl:versionchecksum:).md)
  Creates an object model reference for the model at the specified file URL.
- [init(name: String, in: Bundle?, versionChecksum: String)](nsmanagedobjectmodelreference/init(name:in:versionchecksum:).md)
  Creates an object model reference for the named model in the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodelreference/init(entityversionhashes:in:versionchecksum:))*