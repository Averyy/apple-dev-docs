# NSFetchIndexElementDescription

**Framework**: Core Data  
**Kind**: class  
**Role**: Class

Description of an Index Element

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
class NSFetchIndexElementDescription
```

```objc
@interface NSFetchIndexElementDescription : NSObject
```

## Topics

### Creating an Index Element Description
- [init(property: NSPropertyDescription, collationType: NSFetchIndexElementType)](./nsfetchindexelementdescription/init%28property,collationtype%29.md)
  Creates an index element description using the specified property description and collation type.
### Inspecting an Index Element Description
- [var collationType: NSFetchIndexElementType](./nsfetchindexelementdescription/collationtype.md)
  The type of collation that the index element uses, either binary or R-tree.
- [var indexDescription: NSFetchIndexDescription?](./nsfetchindexelementdescription/indexdescription.md)
- [var isAscending: Bool](./nsfetchindexelementdescription/isascending.md)
  A Boolean value that controls whether an index that supports direction is an ascending or descending index.
- [var property: NSPropertyDescription?](./nsfetchindexelementdescription/property.md)
  A property description.
- [var propertyName: String?](./nsfetchindexelementdescription/propertyname.md)
  The specified name in the property description.
### Initializers
- [init?(coder: NSCoder)](./nsfetchindexelementdescription/init%28coder%29.md)

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
- [class NSFetchIndexDescription](./nsfetchindexdescription.md)
  The description of the index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchindexelementdescription)*