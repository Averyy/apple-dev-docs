# CMTaggedBufferGroupCreateCombined

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a new tagged buffer group from an array of existing tagged buffer groups.

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
extern OSStatus CMTaggedBufferGroupCreateCombined(CFAllocatorRef allocator, CFArrayRef taggedBufferGroups, CMTaggedBufferGroupRef*groupOut);
```

#### Return Value

Returns `0` on success and a value from Tagged Buffer Group Error Codes on failure.

#### Discussion

Buffers strongly retain their references when creating a new tagged buffer group, rather than performing a copy.

## Parameters

- `allocator`: The allocator to use for the new tag collection. Pass `kCFAllocatorDefault` to use the default global allocator.
- `taggedBufferGroups`: An array of tagged buffer groups to combine into the new, single buffer group.
- `groupOut`: The output destination for the new tagged buffer group.

## See Also

### Creating Tagged Buffer Groups
- [CMTaggedBufferGroupCreate](./cmtaggedbuffergroupcreate.md)
  Creates a new tagged buffer group from a pair of buffers and the tags to associate with them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffergroupcreatecombined)*