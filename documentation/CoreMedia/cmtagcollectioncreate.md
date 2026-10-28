# CMTagCollectionCreate

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a new tag collection from an existing C-style array of tags.

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
extern OSStatus CMTagCollectionCreate(CFAllocatorRef allocator, const CMTag *tags, CMItemCount tagCount, CMTagCollectionRef*newCollectionOut);
```

## Return Value

Returns `0` on success and a value from Tag Collection Error Codes on failure.

## Discussion

> ⚠️ **Warning**:  Using a value of `tagCount` greater than the number of elements in the array starting from `tags` causes undefined behavior.

## Parameters

- `allocator`: The allocator to use for the new tag collection. Pass `kCFAllocatorDefault` to use the default global allocator.
- `tags`: A pointer to the first element of the tag array.
- `tagCount`: The number of tags to copy from the array.
- `newCollectionOut`: The output destination for the new tag collection.

## See Also

### Creating Collections
- [CMTagCollectionCreateMutable](./cmtagcollectioncreatemutable.md)
  Creates a new, mutable, empty tag collection.
- [CMTagCollectionCreateFromData](./cmtagcollectioncreatefromdata.md)
  Creates a new tag collection from an existing Core Foundation data instance.
- [CMTagCollectionCreateFromDictionary](./cmtagcollectioncreatefromdictionary.md)
  Creates a new tag collection from an existing Core Foundation dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollectioncreate)*