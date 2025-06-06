# NSManagedObjectModelReference

**Framework**: Core Data  
**Kind**: class

An object that describes a specific version of an object model.

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
class NSManagedObjectModelReference
```

## Topics

### Creating a reference
- [init(model: NSManagedObjectModel, versionChecksum: String)](nsmanagedobjectmodelreference/init(model:versionchecksum:).md)
  Creates an object model reference for the specified model.
- [init(fileURL: URL, versionChecksum: String)](nsmanagedobjectmodelreference/init(fileurl:versionchecksum:).md)
  Creates an object model reference for the model at the specified file URL.
- [init(name: String, in: Bundle?, versionChecksum: String)](nsmanagedobjectmodelreference/init(name:in:versionchecksum:).md)
  Creates an object model reference for the named model in the specified bundle.
- [init(entityVersionHashes: [AnyHashable : Any], in: Bundle?, versionChecksum: String)](nsmanagedobjectmodelreference/init(entityversionhashes:in:versionchecksum:).md)
  Creates an object model reference with the entities corresponding to the specified entity version hashes.
### Resolving the model object
- [var resolvedModel: NSManagedObjectModel](nsmanagedobjectmodelreference/resolvedmodel.md)
  The resolved object model.
- [var versionChecksum: String](nsmanagedobjectmodelreference/versionchecksum.md)
  The version checksum of the resolved model.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init(migratingFrom: NSManagedObjectModelReference, to: NSManagedObjectModelReference)](nscustommigrationstage/init(migratingfrom:to:).md)
  Creates a custom migration stage with the specified source and destination model references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodelreference)*