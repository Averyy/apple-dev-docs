# CMTagCollection

**Framework**: Core Media  
**Role**: API Collection

Objective-C types and interfaces for working with Core Media tag collections.

## Topics

### Creating Collections
- [CMTagCollectionCreate](./cmtagcollectioncreate.md)
  Creates a new tag collection from an existing C-style array of tags.
- [CMTagCollectionCreateMutable](./cmtagcollectioncreatemutable.md)
  Creates a new, mutable, empty tag collection.
- [CMTagCollectionCreateFromData](./cmtagcollectioncreatefromdata.md)
  Creates a new tag collection from an existing Core Foundation data instance.
- [CMTagCollectionCreateFromDictionary](./cmtagcollectioncreatefromdictionary.md)
  Creates a new tag collection from an existing Core Foundation dictionary.
### Converting to Other Types
- [CMTagCollectionCopyAsData](./cmtagcollectioncopyasdata.md)
  Creates a new Core Foundation data instance from a tag collection.
- [CMTagCollectionCopyAsDictionary](./cmtagcollectioncopyasdictionary.md)
  Creates a new Core Foundation dictionary from a tag collection.
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
- [CMTagCollectionCopyDescription](./cmtagcollectioncopydescription.md)
  Retrieves a copy of the tag collection’s description.
- [CMTagCollectionGetTypeID](./cmtagcollectiongettypeid.md)
  Retrieves the internal type ID for tag collections.
### Modifying Collection Tags
- [CMTagCollectionAddTag](./cmtagcollectionaddtag.md)
  Adds a new tag to an existing collection.
- [CMTagCollectionAddTagsFromArray](./cmtagcollectionaddtagsfromarray.md)
  Adds the tags contained in a C-style array to a tag collection.
- [CMTagCollectionAddTagsFromCollection](./cmtagcollectionaddtagsfromcollection.md)
  Add the tags contained in one collection to another.
- [CMTagCollectionRemoveAllTags](./cmtagcollectionremovealltags.md)
  Removes all tags from a collection.
- [CMTagCollectionRemoveAllTagsOfCategory](./cmtagcollectionremovealltagsofcategory.md)
  Removes all tags of a given category from a collection.
- [CMTagCollectionRemoveTag](./cmtagcollectionremovetag.md)
  Removes a specific tag from a collection.
### Deriving New Collections
- [CMTagCollectionCreateCopy](./cmtagcollectioncreatecopy.md)
  Creates a copy of a tag collection.
- [CMTagCollectionCreateMutableCopy](./cmtagcollectioncreatemutablecopy.md)
  Creates a new mutable copy from an existing tag collection.
- [CMTagCollectionCopyTagsOfCategories](./cmtagcollectioncopytagsofcategories.md)
  Creates a new tag collection from an existing collection, copying all tags which match a list of categories.
- [CMTagCollectionCreateUnion](./cmtagcollectioncreateunion.md)
  Creates a new tag collection containing all tags from two collections without duplicates.
- [CMTagCollectionCreateDifference](./cmtagcollectioncreatedifference.md)
  Creates a new tag collection with the difference of two existing collections.
- [CMTagCollectionCreateExclusiveOr](./cmtagcollectioncreateexclusiveor.md)
  Creates a new tag collection from two existing tag collections, copying elements which are in one collection or the other, but not both.
- [CMTagCollectionCreateIntersection](./cmtagcollectioncreateintersection.md)
  Creates a new tag collection containing only the tags from two existing collections which match.
### Iterating Over Tags
- [CMTagCollectionApply](./cmtagcollectionapply.md)
  Applies a function to all tags in a collection.
- [CMTagCollectionApplyUntil](./cmtagcollectionapplyuntil.md)
  Applies a Boolean function to tags in a collection, stopping when it returns true.
### Types
- [CMTagCollectionRef](./cmtagcollectionref.md)
  A reference to a tag collection.
- [CMMutableTagCollectionRef](./cmmutabletagcollectionref.md)
  A mutable reference to a tag collection.
- [CMTagCollectionApplierFunction](./cmtagcollectionapplierfunction.md)
  A type for function application over elements of a tag collection.
- [CMTagCollectionTagFilterFunction](./cmtagcollectiontagfilterfunction.md)
  A type for filtering of tag collections.
### Constants
- [kCMTagCollectionTagsArrayKey](./kcmtagcollectiontagsarraykey.md)
  A dictionary key for assigning tag collections to.
### Errors
- [CMTagCollectionError](./cmtagcollectionerror.md)
  Error codes returned by Core Media when working with tag collections.

## See Also

### Metadata
- [CMMetadata](./cmmetadata.md)
  The APIs for working with the framework’s Metadata Identifier Services and Metadata Data Type Registry.
- [CMTag](./cmtag-api.md)
  Types and interfaces for working with Core Media tags.
- [class CMTag](./cmtag-swift.class.md)
  A tag to set additional metadata on media buffers.
- [class CMTypedTag](./cmtypedtag.md)
  A tag to set additional metadata on media buffers, with an associated Swift type for its value.
- [enum CMProjectionType](./cmprojectiontype.md)
  Constants describing the projection surface information in a 3D video buffer or channel.
- [struct CMStereoViewComponents](./cmstereoviewcomponents.md)
  Constants describing the stereo views contained within a buffer or channel.
- [struct CMStereoViewInterpretationOptions](./cmstereoviewinterpretationoptions.md)
  Create a set of stereo view interpretation options from a constant.
- [enum CMPackingType](./cmpackingtype.md)
  The type of packing within each video frame, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollection)*