# CMTaggedBufferGroupGetNumberOfMatchesForTagCollection

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Gets the number of buffers in the group associated with a given tag collection.

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
extern CMItemCount CMTaggedBufferGroupGetNumberOfMatchesForTagCollection(CMTaggedBufferGroupRef group, CMTagCollectionRef tagCollection);
```

#### Discussion

When this function returns a value other than `1`, avoid using the `tagCollection` to retrieve a buffer from this group. The results of retrieving a buffer with `tagCollection` is `NULL`, since either the group doesn’t contain those tags or the match is ambiguous.

## Parameters

- `group`: The tagged buffer group to inspect.
- `tagCollection`: The collection of tags to search the buffer group for.

## See Also

### Inspecting Tagged Buffer Groups
- [CMTaggedBufferGroupGetCount](./cmtaggedbuffergroupgetcount.md)
  Gets the number of buffers contained within a tagged buffer group.
- [CMTaggedBufferGroupGetTagCollectionAtIndex](./cmtaggedbuffergroupgettagcollectionatindex.md)
  Gets the collection of tags for a buffer at a given index in the group.
- [CMTaggedBufferGroupGetTypeID](./cmtaggedbuffergroupgettypeid.md)
  Gets the internal type ID for a tagged buffer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffergroupgetnumberofmatchesfortagcollection)*