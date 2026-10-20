# collationType

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The type of collation that the index element uses, either binary or R-tree.

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
var collationType: NSFetchIndexElementType { get set }
```

```objc
@property NSFetchIndexElementType collationType;
```

## See Also

### Inspecting an Index Element Description
- [var indexDescription: NSFetchIndexDescription?](./indexdescription.md)
- [var isAscending: Bool](./isascending.md)
  A Boolean value that controls whether an index that supports direction is an ascending or descending index.
- [var property: NSPropertyDescription?](./property.md)
  A property description.
- [var propertyName: String?](./propertyname.md)
  The specified name in the property description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchindexelementdescription/collationtype)*