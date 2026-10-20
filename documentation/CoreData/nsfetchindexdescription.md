# NSFetchIndexDescription

**Framework**: Core Data  
**Kind**: class  
**Role**: Class

The description of the index.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class NSFetchIndexDescription
```

```objc
@interface NSFetchIndexDescription : NSObject
```

## Topics

### Creating an Index Description
- [init(name: String, elements: [NSFetchIndexElementDescription]?)](./nsfetchindexdescription/init%28name,elements%29.md)
  Creates a fetch index description using the specified name and element descriptions.
### Inspecting an Index Description
- [var elements: [NSFetchIndexElementDescription]](./nsfetchindexdescription/elements.md)
  An array of fetch index element descriptions.
- [var entity: NSEntityDescription?](./nsfetchindexdescription/entity.md)
  The entity description for the fetch index description.
- [var name: String](./nsfetchindexdescription/name.md)
  The name of the fetch index description.
- [var partialIndexPredicate: NSPredicate?](./nsfetchindexdescription/partialindexpredicate.md)
  A predicate that selects rows for indexing, if the index is a partial index.
### Initializers
- [init?(coder: NSCoder)](./nsfetchindexdescription/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working with indexes
- [enum NSFetchIndexElementType](./nsfetchindexelementtype.md)
  Defines the possible types of index elements.
- [class NSFetchIndexElementDescription](./nsfetchindexelementdescription.md)
  Description of an Index Element


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchindexdescription)*