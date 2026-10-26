# CMTagCollectionCopyAsData

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a new Core Foundation data instance from a tag collection.

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
extern CFDataRefCMTagCollectionCopyAsData(CMTagCollectionRef tagCollection, CFAllocatorRef allocator);
```

#### Discussion

Convert data instances created by this function back to tag collections with [`CMTagCollectionCreateFromData`](./cmtagcollectioncreatefromdata.md).

## Parameters

- `tagCollection`: The tag collection to convert to data.
- `allocator`: The allocator to use for the new data instance. Pass `kCFAllocatorDefault` to use the default global allocator.

## See Also

### Converting to Other Types
- [CMTagCollectionCopyAsDictionary](./cmtagcollectioncopyasdictionary.md)
  Creates a new Core Foundation dictionary from a tag collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollectioncopyasdata)*