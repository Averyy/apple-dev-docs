# CMTaggedBufferGroupGetCount

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Gets the number of buffers contained within a tagged buffer group.

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
extern CMItemCount CMTaggedBufferGroupGetCount(CMTaggedBufferGroupRef group);
```

## See Also

### Inspecting Tagged Buffer Groups
- [CMTaggedBufferGroupGetNumberOfMatchesForTagCollection](./cmtaggedbuffergroupgetnumberofmatchesfortagcollection.md)
  Gets the number of buffers in the group associated with a given tag collection.
- [CMTaggedBufferGroupGetTagCollectionAtIndex](./cmtaggedbuffergroupgettagcollectionatindex.md)
  Gets the collection of tags for a buffer at a given index in the group.
- [CMTaggedBufferGroupGetTypeID](./cmtaggedbuffergroupgettypeid.md)
  Gets the internal type ID for a tagged buffer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffergroupgetcount)*