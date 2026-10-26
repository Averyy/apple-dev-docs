# CMTaggedBufferGroupGetCMSampleBufferAtIndex

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Gets the sample buffer at a given index in the buffer group.

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
extern CMSampleBufferRefCMTaggedBufferGroupGetCMSampleBufferAtIndex(CMTaggedBufferGroupRef group, CFIndex index);
```

#### Return Value

Returns the sample buffer at index, or `NULL` if the index is out of bounds or points to a pixel buffer.

## See Also

### Accessing Sample Buffers
- [CMTaggedBufferGroupGetCMSampleBufferForTag](./cmtaggedbuffergroupgetcmsamplebufferfortag.md)
  Gets the single sample buffer in a group which contains a given tag, if present.
- [CMTaggedBufferGroupGetCMSampleBufferForTagCollection](./cmtaggedbuffergroupgetcmsamplebufferfortagcollection.md)
  Gets the single sample buffer in a group which contains a given tag collection, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffergroupgetcmsamplebufferatindex)*