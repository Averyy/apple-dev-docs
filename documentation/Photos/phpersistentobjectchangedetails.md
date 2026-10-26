# PHPersistentObjectChangeDetails

**Framework**: Photos  
**Kind**: class  
**Role**: Class

An object that represents the local identifiers that change between requests using a change token.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class PHPersistentObjectChangeDetails
```

```objc
@interface PHPersistentObjectChangeDetails : NSObject
```

## Topics

### Getting the Object Type
- [var objectType: PHObjectType](./phpersistentobjectchangedetails/objecttype.md)
  The model type the change represents.
- [enum PHObjectType](./phobjecttype.md)
  Identifies the type of objects in a change request.
### Getting the Change Details
- [var insertedLocalIdentifiers: Set<String>](./phpersistentobjectchangedetails/insertedlocalidentifiers.md)
  The local identifiers the system inserts since the change token you specify.
- [var updatedLocalIdentifiers: Set<String>](./phpersistentobjectchangedetails/updatedlocalidentifiers.md)
  The local identifiers the system updates since the change token you specify.
- [var deletedLocalIdentifiers: Set<String>](./phpersistentobjectchangedetails/deletedlocalidentifiers.md)
  The local identifiers the system deletes since the change token you specify.

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Change History
- [func changeDetails(for: PHObjectType) throws -> PHPersistentObjectChangeDetails](./phpersistentchange/changedetails%28for%29.md)
  Returns the change history that contains the local identifiers for object inserts, updates, and deletes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phpersistentobjectchangedetails)*