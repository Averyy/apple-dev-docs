# CMTaggedBufferGroupGetCVPixelBufferForTagCollection

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Gets the single pixel buffer in a group which contains a given tag collection, if present.

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
extern CVPixelBufferRefCMTaggedBufferGroupGetCVPixelBufferForTagCollection(CMTaggedBufferGroupRef group, CMTagCollectionRef tagCollection, CFIndex *indexOut);
```

## Return Value

Returns the unique pixel buffer associated with `tagCollection`, or `NULL` if there were multiple pixel buffers or no pixel buffer could be found.

## Parameters

- `group`: The tagged buffer group to inspect.
- `tagCollection`: The tag collection to match in the buffer group.
- `indexOut`: A pointer to the index of the retrieved pixel buffer. The value of indexOut is `NULL` when the function returns `NULL`.

## See Also

### Accessing Pixel Buffers
- [CMTaggedBufferGroupGetCVPixelBufferAtIndex](./cmtaggedbuffergroupgetcvpixelbufferatindex.md)
  Gets the pixel buffer at a given index in the buffer group.
- [CMTaggedBufferGroupGetCVPixelBufferForTag](./cmtaggedbuffergroupgetcvpixelbufferfortag.md)
  Gets the single pixel buffer in a group which contains a given tag, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffergroupgetcvpixelbufferfortagcollection)*