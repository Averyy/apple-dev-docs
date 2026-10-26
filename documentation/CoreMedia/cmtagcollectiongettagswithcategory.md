# CMTagCollectionGetTagsWithCategory

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Retrieves a C-style array of tags with a given category from a tag collection.

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
extern OSStatus CMTagCollectionGetTagsWithCategory(CMTagCollectionRef tagCollection, CMTagCategory category, CMTag *tagBuffer, CMItemCount tagBufferCount, CMItemCount *numberOfTagsCopied);
```

#### Return Value

Returns `0` on success and a value from Tag Collection Error Codes on failure.

#### Discussion

> ⚠️ **Warning**:  Using a value for `tagBufferCount` larger than the number of elements that `tagBuffer` holds can cause undefined behavior.

## Parameters

- `tagCollection`: The collection to retrieve tags from.
- `category`: The category to retrieve tags for.
- `tagBuffer`: A pointer to a pre-allocated C-style array of tags, containing the collection’s matching tags on function return.
- `tagBufferCount`: The number of tags that the `tagBuffer` array can hold.
- `numberOfTagsCopied`: The total number of tags copied from the collection to `tagBuffer`.

## See Also

### Inspecting Collections
- [CMTagCollectionGetCount](./cmtagcollectiongetcount.md)
  Gets the number of tags in a tag collection.
- [CMTagCollectionCountTagsWithFilterFunction](./cmtagcollectioncounttagswithfilterfunction.md)
  Counts the number of tags in a collection matching an evaluation function.
- [CMTagCollectionIsEmpty](./cmtagcollectionisempty.md)
  Checks if a tag collection has no elements.
- [CMTagCollectionGetTags](./cmtagcollectiongettags.md)
  Retrieves an arbitrary number of tags from the collection.
- [CMTagCollectionGetTagsWithFilterFunction](./cmtagcollectiongettagswithfilterfunction.md)
  Gets all tags in a collection matching an evaluation function.
- [CMTagCollectionContainsCategory](./cmtagcollectioncontainscategory.md)
  Determines if a tag collection contains tags for a given category.
- [CMTagCollectionGetCountOfCategory](./cmtagcollectiongetcountofcategory.md)
  Retrieves the number of tags in the collection matching a given category.
- [CMTagCollectionContainsTag](./cmtagcollectioncontainstag.md)
  Determines if a tag collection contains a specific tag.
- [CMTagCollectionContainsSpecifiedTags](./cmtagcollectioncontainsspecifiedtags.md)
  Determines if a tag collection contains a subset of tags.
- [CMTagCollectionContainsTagsOfCollection](./cmtagcollectioncontainstagsofcollection.md)
  Determines if one collection of tags contains every tag from another collection.
- [CMTagCollectionCopyDescription](./cmtagcollectioncopydescription.md)
  Retrieves a copy of the tag collection’s description.
- [CMTagCollectionGetTypeID](./cmtagcollectiongettypeid.md)
  Retrieves the internal type ID for tag collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollectiongettagswithcategory)*