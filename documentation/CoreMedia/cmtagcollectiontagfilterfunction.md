# CMTagCollectionTagFilterFunction

**Framework**: Core Media  
**Kind**: typealias  
**Role**: Type Alias

A type for filtering of tag collections.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```c
typedef unsigned char (*)(struct CMTag, void *) CMTagCollectionTagFilterFunction;
```

## See Also

### Types
- [CMTagCollectionRef](./cmtagcollectionref.md)
  A reference to a tag collection.
- [CMMutableTagCollectionRef](./cmmutabletagcollectionref.md)
  A mutable reference to a tag collection.
- [CMTagCollectionApplierFunction](./cmtagcollectionapplierfunction.md)
  A type for function application over elements of a tag collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollectiontagfilterfunction)*