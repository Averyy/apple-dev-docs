# CMTagCollectionAddTagsFromArray

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Adds the tags contained in a C-style array to a tag collection.

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
extern OSStatus CMTagCollectionAddTagsFromArray(CMMutableTagCollectionRef tagCollection, CMTag *tags, CMItemCount tagCount);
```

#### Return Value

Returns `0` on success and a value from Tag Collection Error Codes on failure.

#### Discussion

> ⚠️ **Warning**:  Using a value of `containedTagCount` greater than the number of elements in the array starting from `containedTags` causes undefined behavior.

## Parameters

- `tagCollection`: The tag collection to add tags to.
- `tags`: A pointer to the start of an array of tags to copy.
- `tagCount`: The number of tags to add from the `tags` array.

## See Also

### Modifying Collection Tags
- [CMTagCollectionAddTag](./cmtagcollectionaddtag.md)
  Adds a new tag to an existing collection.
- [CMTagCollectionAddTagsFromCollection](./cmtagcollectionaddtagsfromcollection.md)
  Add the tags contained in one collection to another.
- [CMTagCollectionRemoveAllTags](./cmtagcollectionremovealltags.md)
  Removes all tags from a collection.
- [CMTagCollectionRemoveAllTagsOfCategory](./cmtagcollectionremovealltagsofcategory.md)
  Removes all tags of a given category from a collection.
- [CMTagCollectionRemoveTag](./cmtagcollectionremovetag.md)
  Removes a specific tag from a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollectionaddtagsfromarray)*