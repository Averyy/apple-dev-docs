# CMSampleBufferGetTaggedBufferGroup

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Gets the tagged buffer group of a sample buffer.

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
extern CMTaggedBufferGroupRefCMSampleBufferGetTaggedBufferGroup(CMSampleBufferRef sbuf);
```

#### Return Value

The sample buffer’s tagged buffer group, or `NULL` if the sample buffer doesn’t belong to a tagged buffer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffergettaggedbuffergroup)*