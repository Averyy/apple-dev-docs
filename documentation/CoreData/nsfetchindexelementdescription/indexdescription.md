# indexDescription

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

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
unowned(unsafe) var indexDescription: NSFetchIndexDescription? { get }
```

```objc
@property (nonatomic, assign, readonly, nullable) NSFetchIndexDescription * indexDescription;
```

## See Also

### Inspecting an Index Element Description
- [var collationType: NSFetchIndexElementType](./collationtype.md)
  The type of collation that the index element uses, either binary or R-tree.
- [var isAscending: Bool](./isascending.md)
  A Boolean value that controls whether an index that supports direction is an ascending or descending index.
- [var property: NSPropertyDescription?](./property.md)
  A property description.
- [var propertyName: String?](./propertyname.md)
  The specified name in the property description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchindexelementdescription/indexdescription)*