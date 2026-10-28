# CMTagCollectionCreateDifference

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a new tag collection with the difference of two existing collections.

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
extern OSStatus CMTagCollectionCreateDifference(CMTagCollectionRef tagCollectionMinuend, CMTagCollectionRef tagCollectionSubtrahend, CMTagCollectionRef*tagCollectionOut);
```

## Return Value

Returns `0` on success and a value from Tag Collection Error Codes on failure.

## Discussion

This function is non-commutative, meaning that the ordering of arguments is important. To produce a disjoint collection of tags rather than a difference, use [`CMTagCollectionCreateExclusiveOr`](./cmtagcollectioncreateexclusiveor.md).

## Parameters

- `tagCollectionMinuend`: The tag collection to remove elements from.
- `tagCollectionSubtrahend`: The elements to remove from `tagCollectionMinuend`, if present.
- `tagCollectionOut`: The output destination for the new tag collection.

## See Also

### Deriving New Collections
- [CMTagCollectionCreateCopy](./cmtagcollectioncreatecopy.md)
  Creates a copy of a tag collection.
- [CMTagCollectionCreateMutableCopy](./cmtagcollectioncreatemutablecopy.md)
  Creates a new mutable copy from an existing tag collection.
- [CMTagCollectionCopyTagsOfCategories](./cmtagcollectioncopytagsofcategories.md)
  Creates a new tag collection from an existing collection, copying all tags which match a list of categories.
- [CMTagCollectionCreateUnion](./cmtagcollectioncreateunion.md)
  Creates a new tag collection containing all tags from two collections without duplicates.
- [CMTagCollectionCreateExclusiveOr](./cmtagcollectioncreateexclusiveor.md)
  Creates a new tag collection from two existing tag collections, copying elements which are in one collection or the other, but not both.
- [CMTagCollectionCreateIntersection](./cmtagcollectioncreateintersection.md)
  Creates a new tag collection containing only the tags from two existing collections which match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollectioncreatedifference)*