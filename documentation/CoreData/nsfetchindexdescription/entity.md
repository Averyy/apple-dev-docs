# entity

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The entity description for the fetch index description.

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
unowned(unsafe) var entity: NSEntityDescription? { get }
```

```objc
@property (nonatomic, assign, readonly, nullable) NSEntityDescription * entity;
```

## See Also

### Inspecting an Index Description
- [var elements: [NSFetchIndexElementDescription]](./elements.md)
  An array of fetch index element descriptions.
- [var name: String](./name.md)
  The name of the fetch index description.
- [var partialIndexPredicate: NSPredicate?](./partialindexpredicate.md)
  A predicate that selects rows for indexing, if the index is a partial index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchindexdescription/entity)*