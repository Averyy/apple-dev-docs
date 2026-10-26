# CMTaggedBufferGroupCreate

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a new tagged buffer group from a pair of buffers and the tags to associate with them.

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
extern OSStatus CMTaggedBufferGroupCreate(CFAllocatorRef allocator, CFArrayRef tagCollections, CFArrayRef buffers, CMTaggedBufferGroupRef*groupOut);
```

#### Return Value

Returns `0` on success and a value from Tagged Buffer Group Error Codes on failure.

#### Discussion

Buffers strongly retain their references when creating a new tagged buffer group, rather than performing a copy. The number of elements in `tagCollections` and `buffers` must be the same.

## Parameters

- `allocator`: The allocator to use for the new tag collection. Pass `kCFAllocatorDefault` to use the default global allocator.
- `tagCollections`: The tag collections to apply to each buffer, in order.
- `buffers`: An array of buffer instances to place in the tagged buffer group.
- `groupOut`: The output destination for the new tagged buffer group.

## See Also

### Creating Tagged Buffer Groups
- [CMTaggedBufferGroupCreateCombined](./cmtaggedbuffergroupcreatecombined.md)
  Creates a new tagged buffer group from an array of existing tagged buffer groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffergroupcreate)*