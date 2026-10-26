# CMTagCollectionContainsSpecifiedTags

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Determines if a tag collection contains a subset of tags.

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
extern Boolean CMTagCollectionContainsSpecifiedTags(CMTagCollectionRef tagCollection, const CMTag *containedTags, CMItemCount containedTagCount);
```

#### Return Value

Returns `YES` if the tag collection contains all tags from the `containedTags` array.

#### Discussion

> ⚠️ **Warning**:  Using a value of `containedTagCount` greater than the number of elements in the array starting from `containedTags` causes undefined behavior.

## Parameters

- `tagCollection`: The collection to inspect.
- `containedTags`: A pointer to the first element of a C-style array of tags to search the collection for.
- `containedTagCount`: The number of tags in the `tags` array.

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
- [CMTagCollectionGetTagsWithCategory](./cmtagcollectiongettagswithcategory.md)
  Retrieves a C-style array of tags with a given category from a tag collection.
- [CMTagCollectionGetTagsWithFilterFunction](./cmtagcollectiongettagswithfilterfunction.md)
  Gets all tags in a collection matching an evaluation function.
- [CMTagCollectionContainsCategory](./cmtagcollectioncontainscategory.md)
  Determines if a tag collection contains tags for a given category.
- [CMTagCollectionGetCountOfCategory](./cmtagcollectiongetcountofcategory.md)
  Retrieves the number of tags in the collection matching a given category.
- [CMTagCollectionContainsTag](./cmtagcollectioncontainstag.md)
  Determines if a tag collection contains a specific tag.
- [CMTagCollectionContainsTagsOfCollection](./cmtagcollectioncontainstagsofcollection.md)
  Determines if one collection of tags contains every tag from another collection.
- [CMTagCollectionCopyDescription](./cmtagcollectioncopydescription.md)
  Retrieves a copy of the tag collection’s description.
- [CMTagCollectionGetTypeID](./cmtagcollectiongettypeid.md)
  Retrieves the internal type ID for tag collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollectioncontainsspecifiedtags)*