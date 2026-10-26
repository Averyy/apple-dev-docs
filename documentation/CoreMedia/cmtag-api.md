# CMTag

**Framework**: Core Media  
**Role**: API Collection

Types and interfaces for working with Core Media tags.

## Topics

### Types
- [class CMTag](./cmtag-swift.class.md)
  A tag to set additional metadata on media buffers.
- [CMTag](./cmtag-c.struct.md)
  A tag representing additional metadata on tagged media buffers.
- [CMTagValue](./cmtagvalue.md)
  The type used to represent tag values.
### Constants
- [Tag Values](./tag-values.md)
- [kCMTagCategoryKey](./kcmtagcategorykey.md)
  A constant for use as a key during tag creation from a dictionary, whose value is the tag’s category.
- [kCMTagDataTypeKey](./kcmtagdatatypekey.md)
  A constant for use as a key during tag creation from a dictionary, whose value is the tag’s data type.
- [kCMTagValueKey](./kcmtagvaluekey.md)
  A constant for use as a key during tag creation from a dictionary, whose value is the tag’s contained value.
- [kCMTagInvalid](./kcmtaginvalid.md)
  A constant representing an invalid tag.
### Creating Tags
- [CMTagMakeFromDictionary](./cmtagmakefromdictionary.md)
  Create a new tag from a dictionary object.
- [CMTagMakeWithFlagsValue](./cmtagmakewithflagsvalue.md)
  Creates a new tag with a given category and a value interpreted as a 64-bit flag field.
- [CMTagMakeWithFloat64Value](./cmtagmakewithfloat64value.md)
  Creates a new tag with a given category and a 64-bit floating point value.
- [CMTagMakeWithOSTypeValue](./cmtagmakewithostypevalue.md)
  Creates a new tag with a given category and a 64-bit value for use by the framework.
- [CMTagMakeWithSInt64Value](./cmtagmakewithsint64value.md)
  Creates a new tag with a given category and a 64-bit signed integer.
### Tag Categories
- [CMTagCategory](./cmtagcategory.md)
  A 64-bit representation of a tag’s category.
### Tag Data Types
- [CMTagDataType](./cmtagdatatype.md)
  The data type of a tag’s value.
### Inspecting Tags
- [CMTagCopyDescription](./cmtagcopydescription.md)
  Copies the description of a tag to a new string.
- [CMTagIsValid](./cmtagisvalid.md)
  Whether the provided tag is valid.
- [CMTagGetCategory](./cmtaggetcategory.md)
  Retrieves the category of a tag.
- [CMTagGetValueDataType](./cmtaggetvaluedatatype.md)
  Retrieves the data type of a tag.
- [CMTagHasCategory](./cmtaghascategory.md)
  Checks if a tag contains a specific category.
- [CMTagHasFlagsValue](./cmtaghasflagsvalue.md)
  Whether a given tag contains a value for a 64-bit flag field.
- [CMTagHasFloat64Value](./cmtaghasfloat64value.md)
  Whether a given tag contains a value for a 64-bit floating point number.
- [CMTagHasOSTypeValue](./cmtaghasostypevalue.md)
  Whether a given tag contains a value for use by the operating system.
- [CMTagHasSInt64Value](./cmtaghassint64value.md)
  Whether a given tag contains a value for a signed 64-bit integer.
### Retrieving Tag Values
- [CMTagCopyAsDictionary](./cmtagcopyasdictionary.md)
  Copies an existing tag to a new dictionary object.
- [CMTagGetFlagsValue](./cmtaggetflagsvalue.md)
  Retrieves a tag’s value as a 64-bit field flag.
- [CMTagGetFloat64Value](./cmtaggetfloat64value.md)
  Retrieves a tag’s value as a 64-bit floating point number.
- [CMTagGetOSTypeValue](./cmtaggetostypevalue.md)
  Retrieves a tag’s value for use by the operating system.
- [CMTagGetSInt64Value](./cmtaggetsint64value.md)
  Retrieves a tag’s value as a signed 64-bit integer.
- [CMTagGetValue](./cmtaggetvalue.md)
  Retrieves a tag’s value as an uninterpreted 64-bit wide unsigned integer.
### Comparison and Equality
- [CMTagEqualToTag](./cmtagequaltotag.md)
  Compares two tags for strict equality.
- [CMTagCompare](./cmtagcompare.md)
  Compares two tags in terms of partial equality.
- [CMTagCategoryEqualToTagCategory](./cmtagcategoryequaltotagcategory.md)
  Compares two tags’s categories for equality.
- [CMTagCategoryValueEqualToValue](./cmtagcategoryvalueequaltovalue.md)
  Compares two tags’s values for equality.
- [CMTagHash](./cmtaghash.md)
  Generates a hash identifier for a tag.
### Errors
- [CMTagError](./cmtagerror.md)
  Core media tagging errors reported by the framework.

## See Also

### Metadata
- [CMMetadata](./cmmetadata.md)
  The APIs for working with the framework’s Metadata Identifier Services and Metadata Data Type Registry.
- [class CMTag](./cmtag-swift.class.md)
  A tag to set additional metadata on media buffers.
- [class CMTypedTag](./cmtypedtag.md)
  A tag to set additional metadata on media buffers, with an associated Swift type for its value.
- [CMTagCollection](./cmtagcollection.md)
  Objective-C types and interfaces for working with Core Media tag collections.
- [enum CMProjectionType](./cmprojectiontype.md)
  Constants describing the projection surface information in a 3D video buffer or channel.
- [struct CMStereoViewComponents](./cmstereoviewcomponents.md)
  Constants describing the stereo views contained within a buffer or channel.
- [struct CMStereoViewInterpretationOptions](./cmstereoviewinterpretationoptions.md)
  Create a set of stereo view interpretation options from a constant.
- [enum CMPackingType](./cmpackingtype.md)
  The type of packing within each video frame, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtag-api)*