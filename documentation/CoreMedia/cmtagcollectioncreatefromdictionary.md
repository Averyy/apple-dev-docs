# CMTagCollectionCreateFromDictionary

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a new tag collection from an existing Core Foundation dictionary.

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
extern OSStatus CMTagCollectionCreateFromDictionary(CFDictionaryRef dict, CFAllocatorRef allocator, CMTagCollectionRef*newCollectionOut);
```

#### Return Value

Returns `0` on success and a value from Tag Collection Error Codes on failure.

## Parameters

- `dict`: The dictionary to create the new tag collection from. Pass an instance created with [`CMTagCollectionCopyAsDictionary`](./cmtagcollectioncopyasdictionary.md).
- `allocator`: The allocator to use for the new tag collection. Pass `kCFAllocatorDefault` to use the default global allocator.
- `newCollectionOut`: The output destination for the new tag collection.

## See Also

### Creating Collections
- [CMTagCollectionCreate](./cmtagcollectioncreate.md)
  Creates a new tag collection from an existing C-style array of tags.
- [CMTagCollectionCreateMutable](./cmtagcollectioncreatemutable.md)
  Creates a new, mutable, empty tag collection.
- [CMTagCollectionCreateFromData](./cmtagcollectioncreatefromdata.md)
  Creates a new tag collection from an existing Core Foundation data instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollectioncreatefromdictionary)*