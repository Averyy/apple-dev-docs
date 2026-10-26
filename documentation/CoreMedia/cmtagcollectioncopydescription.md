# CMTagCollectionCopyDescription

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Retrieves a copy of the tag collection’s description.

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
extern CFStringRefCMTagCollectionCopyDescription(CFAllocatorRef allocator, CMTagCollectionRef tagCollection);
```

## Parameters

- `allocator`: The allocator to use for the new tag collection. Pass `kCFAllocatorDefault` to use the default global allocator.
- `tagCollection`: The tag collection to copy the description from.

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
- [CMTagCollectionContainsSpecifiedTags](./cmtagcollectioncontainsspecifiedtags.md)
  Determines if a tag collection contains a subset of tags.
- [CMTagCollectionContainsTagsOfCollection](./cmtagcollectioncontainstagsofcollection.md)
  Determines if one collection of tags contains every tag from another collection.
- [CMTagCollectionGetTypeID](./cmtagcollectiongettypeid.md)
  Retrieves the internal type ID for tag collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollectioncopydescription)*