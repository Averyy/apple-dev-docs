# CMTagCollectionCopyTagsOfCategories

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a new tag collection from an existing collection, copying all tags which match a list of categories.

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
extern OSStatus CMTagCollectionCopyTagsOfCategories(CFAllocatorRef allocator, CMTagCollectionRef tagCollection, const CMTagCategory *categories, CMItemCount categoriesCount, CMTagCollectionRef*collectionWithTagsOfCategories);
```

#### Return Value

Returns `0` on success and a value from Tag Collection Error Codes on failure.

#### Discussion

> ⚠️ **Warning**:  Using a value of `categoriesCount` greater than the number of elements in the array starting from `categories` causes undefined behavior.

## Parameters

- `allocator`: The allocator to use for the new tag collection. Pass `kCFAllocatorDefault` to use the default global allocator.
- `tagCollection`: The tag collection to copy tags from.
- `categories`: A C-style array containing the categories to match.
- `categoriesCount`: The number of categories.
- `collectionWithTagsOfCategories`: The output destination for the new tag collection.

## See Also

### Deriving New Collections
- [CMTagCollectionCreateCopy](./cmtagcollectioncreatecopy.md)
  Creates a copy of a tag collection.
- [CMTagCollectionCreateMutableCopy](./cmtagcollectioncreatemutablecopy.md)
  Creates a new mutable copy from an existing tag collection.
- [CMTagCollectionCreateUnion](./cmtagcollectioncreateunion.md)
  Creates a new tag collection containing all tags from two collections without duplicates.
- [CMTagCollectionCreateDifference](./cmtagcollectioncreatedifference.md)
  Creates a new tag collection with the difference of two existing collections.
- [CMTagCollectionCreateExclusiveOr](./cmtagcollectioncreateexclusiveor.md)
  Creates a new tag collection from two existing tag collections, copying elements which are in one collection or the other, but not both.
- [CMTagCollectionCreateIntersection](./cmtagcollectioncreateintersection.md)
  Creates a new tag collection containing only the tags from two existing collections which match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollectioncopytagsofcategories)*