# CMTagCollectionCreateFromData

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a new tag collection from an existing Core Foundation data instance.

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
extern OSStatus CMTagCollectionCreateFromData(CFDataRef data, CFAllocatorRef allocator, CMTagCollectionRef*newCollectionOut);
```

## Return Value

Returns `0` on success and a value from Tag Collection Error Codes on failure.

## Parameters

- `data`: The data instance to create the new tag collection from. Pass an instance created with [`CMTagCollectionCopyAsData`](./cmtagcollectioncopyasdata.md).
- `allocator`: The allocator to use for the new tag collection. Pass `kCFAllocatorDefault` to use the default global allocator.
- `newCollectionOut`: The output destination for the new tag collection.

## See Also

### Creating Collections
- [CMTagCollectionCreate](./cmtagcollectioncreate.md)
  Creates a new tag collection from an existing C-style array of tags.
- [CMTagCollectionCreateMutable](./cmtagcollectioncreatemutable.md)
  Creates a new, mutable, empty tag collection.
- [CMTagCollectionCreateFromDictionary](./cmtagcollectioncreatefromdictionary.md)
  Creates a new tag collection from an existing Core Foundation dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollectioncreatefromdata)*