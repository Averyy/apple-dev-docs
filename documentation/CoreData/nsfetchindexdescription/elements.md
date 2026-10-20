# elements

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

An array of fetch index element descriptions.

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
var elements: [NSFetchIndexElementDescription] { get set }
```

```objc
@property (copy) NSArray<NSFetchIndexElementDescription *> * elements;
```

#### Discussion

Setting this property to an invalid value throws an exception, such as when the new value includes both R-tree and non-R-tree elements.

## See Also

### Inspecting an Index Description
- [var entity: NSEntityDescription?](./entity.md)
  The entity description for the fetch index description.
- [var name: String](./name.md)
  The name of the fetch index description.
- [var partialIndexPredicate: NSPredicate?](./partialindexpredicate.md)
  A predicate that selects rows for indexing, if the index is a partial index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchindexdescription/elements)*