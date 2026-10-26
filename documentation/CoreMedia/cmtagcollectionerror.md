# CMTagCollectionError

**Framework**: Core Media  
**Kind**: enum  
**Role**: Enumeration

Error codes returned by Core Media when working with tag collections.

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
enum CMTagCollectionError : OSStatus;
```

## Topics

### Tag Collection Error Codes
- [kCMTagCollectionError_AllocationFailed](./cmtagcollectionerror/kcmtagcollectionerror_allocationfailed.md)
  Indicates an internal allocation failed.
- [kCMTagCollectionError_ExhaustedBufferSize](./cmtagcollectionerror/kcmtagcollectionerror_exhaustedbuffersize.md)
  Indicates that a buffer was smaller than the number of requested tags.
- [kCMTagCollectionError_InvalidTag](./cmtagcollectionerror/kcmtagcollectionerror_invalidtag.md)
  Indicates that the collection contains an invalid tag.
- [kCMTagCollectionError_InvalidTagCollectionData](./cmtagcollectionerror/kcmtagcollectionerror_invalidtagcollectiondata.md)
  Indicates that a Core Foundation data instance failed to initialize a new tag collection.
- [kCMTagCollectionError_InvalidTagCollectionDataVersion](./cmtagcollectionerror/kcmtagcollectionerror_invalidtagcollectiondataversion.md)
  Indicates that a Core Foundation data instance failed to initialize a new tag collection due to a versioning problem.
- [kCMTagCollectionError_InvalidTagCollectionDictionary](./cmtagcollectionerror/kcmtagcollectionerror_invalidtagcollectiondictionary.md)
  Indicates that a Core Foundation dictionary instance failed to initialize a new tag collection.
- [kCMTagCollectionError_ParamErr](./cmtagcollectionerror/kcmtagcollectionerror_paramerr.md)
  Indicates a parameter to a function was of the wrong type or didn’t meet a necessary condition.
- [kCMTagCollectionError_TagNotFound](./cmtagcollectionerror/kcmtagcollectionerror_tagnotfound.md)
  Indicates that there was no match in a collection for a tag.
- [kCMTagCollectionError_InternalError](./cmtagcollectionerror/kcmtagcollectionerror_internalerror.md)
  Indicates an error occurred inside of the Core Media framework.
### Constants
- [kCMTagCollectionError_NotYetImplemented](./cmtagcollectionerror/kcmtagcollectionerror_notyetimplemented.md)
  Indicates a function lacks a necessary backing implementation in Core Media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagcollectionerror)*