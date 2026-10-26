# CMTagCollectionRemoveAllTagsOfCategory

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Removes all tags of a given category from a collection.

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
extern OSStatus CMTagCollectionRemoveAllTagsOfCategory(CMMutableTagCollectionRef tagCollection, CMTagCategory category);
```

#### Return Value

Returns `0` on success and a value from Tag Collection Error Codes on failure.

## Parameters

- `tagCollection`: The collection to remove tags from.
- `category`: The category to remove all tags for.

## See Also

### Modifying Collection Tags
- [CMTagCollectionAddTag](./cmtagcollectionaddtag.md)
  Adds a new tag to an existing collection.
- [CMTagCollectionAddTagsFromArray](./cmtagcollectionaddtagsfromarray.md)
  Adds the tags contained in a C-style array to a tag collection.
- [CMTagCollectionAddTagsFromCollection](./cmtagcollectionaddtagsfromcollection.md)
  Add the tags contained in one collection to another.
- [CMTagCollectionRemoveAllTags](./cmtagcollectionremovealltags.md)
  Removes all tags from a collection.
- [CMTagCollectionRemoveTag](./cmtagcollectionremovetag.md)
  Removes a specific tag from a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollectionremovealltagsofcategory)*