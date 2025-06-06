# NSFetchIndexDescription

**Framework**: Core Data  
**Kind**: class

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

## Topics

### Creating an Index Description
- [init(name: String, elements: [NSFetchIndexElementDescription]?)](nsfetchindexdescription/init(name:elements:).md)
  Creates a fetch index description using the specified name and element descriptions.
### Inspecting an Index Description
- [var elements: [NSFetchIndexElementDescription]](nsfetchindexdescription/elements.md)
  An array of fetch index element descriptions.
- [var entity: NSEntityDescription?](nsfetchindexdescription/entity.md)
  The entity description for the fetch index description.
- [var name: String](nsfetchindexdescription/name.md)
  The name of the fetch index description.
- [var partialIndexPredicate: NSPredicate?](nsfetchindexdescription/partialindexpredicate.md)
  A predicate that selects rows for indexing, if the index is a partial index.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [enum NSFetchIndexElementType](nsfetchindexelementtype.md)
  Defines the possible types of index elements.
- [class NSFetchIndexElementDescription](nsfetchindexelementdescription.md)
  Description of an Index Element


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchindexdescription)*