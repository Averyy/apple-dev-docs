# NSManagedObjectModelReference

**Framework**: Core Data  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSManagedObjectModelReference : NSObject
```

## Topics

### Creating a reference
- [init(model: NSManagedObjectModel, versionChecksum: String)](./nsmanagedobjectmodelreference/init%28model,versionchecksum%29.md)
  Creates an object model reference for the specified model.
- [init(fileURL: URL, versionChecksum: String)](./nsmanagedobjectmodelreference/init%28fileurl,versionchecksum%29.md)
  Creates an object model reference for the model at the specified file URL.
- [init(name: String, in: Bundle?, versionChecksum: String)](./nsmanagedobjectmodelreference/init%28name,in,versionchecksum%29.md)
  Creates an object model reference for the named model in the specified bundle.
- [init(entityVersionHashes: [AnyHashable : Any], in: Bundle?, versionChecksum: String)](./nsmanagedobjectmodelreference/init%28entityversionhashes,in,versionchecksum%29.md)
  Creates an object model reference with the entities corresponding to the specified entity version hashes.
### Resolving the model object
- [var resolvedModel: NSManagedObjectModel](./nsmanagedobjectmodelreference/resolvedmodel.md)
  The resolved object model.
- [var versionChecksum: String](./nsmanagedobjectmodelreference/versionchecksum.md)
  The version checksum of the resolved model.
### Initializers
- [init(entityVersionHashes: [AnyHashable : Any], inBundle: Bundle?, versionChecksum: String)](./nsmanagedobjectmodelreference/init%28entityversionhashes,inbundle,versionchecksum%29.md)
- [init(name: String, inBundle: Bundle?, versionChecksum: String)](./nsmanagedobjectmodelreference/init%28name,inbundle,versionchecksum%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a custom migration stage
- [convenience init(migratingFrom: NSManagedObjectModelReference, to: NSManagedObjectModelReference)](./nscustommigrationstage/init%28migratingfrom,to%29.md)
  Creates a custom migration stage with the specified source and destination model references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectmodelreference)*