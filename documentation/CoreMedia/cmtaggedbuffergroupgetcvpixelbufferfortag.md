# CMTaggedBufferGroupGetCVPixelBufferForTag

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Gets the single pixel buffer in a group which contains a given tag, if present.

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
extern CVPixelBufferRefCMTaggedBufferGroupGetCVPixelBufferForTag(CMTaggedBufferGroupRef group, CMTag tag, CFIndex *indexOut);
```

#### Return Value

Returns the unique pixel buffer associated with tag, or `NULL` if there were multiple pixel buffers or no pixel buffer could be found.

## Parameters

- `group`: The tagged buffer group to inspect.
- `tag`: The tag to match in the buffer group.
- `indexOut`: A pointer to the index of the retrieved pixel buffer. The value of indexOut is `NULL` when the function returns `NULL`.

## See Also

### Accessing Pixel Buffers
- [CMTaggedBufferGroupGetCVPixelBufferAtIndex](./cmtaggedbuffergroupgetcvpixelbufferatindex.md)
  Gets the pixel buffer at a given index in the buffer group.
- [CMTaggedBufferGroupGetCVPixelBufferForTagCollection](./cmtaggedbuffergroupgetcvpixelbufferfortagcollection.md)
  Gets the single pixel buffer in a group which contains a given tag collection, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffergroupgetcvpixelbufferfortag)*