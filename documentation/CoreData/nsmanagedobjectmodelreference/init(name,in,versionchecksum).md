# init(name:in:versionChecksum:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Creates an object model reference for the named model in the specified bundle.

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
init(name modelName: String, in bundle: Bundle?, versionChecksum: String)
```

```objc
- (instancetype) initWithName:(NSString *) modelName inBundle:(NSBundle *) bundle versionChecksum:(NSString *) versionChecksum;
```

#### Discussion

To determine an object model’s version checksum, use its [`versionChecksum`](../nsmanagedobjectmodel/versionchecksum.md) property. Alternatively, you can find the checksum in the versioned model’s `VersionInfo.plist` file or in Xcode’s build log.

## Parameters

- `modelName`: The name of the managed object model in the specified bundle.
- `bundle`: The bundle to search.
- `versionChecksum`: The checksum of the object model’s version.

## See Also

### Creating a reference
- [init(model: NSManagedObjectModel, versionChecksum: String)](./init%28model,versionchecksum%29.md)
  Creates an object model reference for the specified model.
- [init(fileURL: URL, versionChecksum: String)](./init%28fileurl,versionchecksum%29.md)
  Creates an object model reference for the model at the specified file URL.
- [init(entityVersionHashes: [AnyHashable : Any], in: Bundle?, versionChecksum: String)](./init%28entityversionhashes,in,versionchecksum%29.md)
  Creates an object model reference with the entities corresponding to the specified entity version hashes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodelreference/init(name:in:versionchecksum:))*