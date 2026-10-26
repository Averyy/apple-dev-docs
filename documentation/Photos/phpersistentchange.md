# PHPersistentChange

**Framework**: Photos  
**Kind**: class  
**Role**: Class

An object that represents a change in the Photos library, and allows for requesting local identifiers that identify the changes for a library object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class PHPersistentChange
```

```objc
@interface PHPersistentChange : NSObject
```

## Topics

### Getting the Change Token
- [var changeToken: PHPersistentChangeToken](./phpersistentchange/changetoken.md)
  An opaque object that represents the state of Photos library.
- [class PHPersistentChangeToken](./phpersistentchangetoken.md)
  An opaque object that tracks the state of the Photos library between runs, and that you can copy and serialize for future use.
### Getting the Change History
- [func changeDetails(for: PHObjectType) throws -> PHPersistentObjectChangeDetails](./phpersistentchange/changedetails%28for%29.md)
  Returns the change history that contains the local identifiers for object inserts, updates, and deletes.
- [class PHPersistentObjectChangeDetails](./phpersistentobjectchangedetails.md)
  An object that represents the local identifiers that change between requests using a change token.

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

### Performing Operations with Objects in a Fetch Request
- [- enumerateChangesWithBlock:](./phpersistentchangefetchresult/enumeratechangeswithblock_.md)
  Executes the block you specify by using the objects in the fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phpersistentchange)*