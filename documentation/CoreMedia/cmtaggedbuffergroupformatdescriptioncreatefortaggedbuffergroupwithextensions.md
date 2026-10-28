# CMTaggedBufferGroupFormatDescriptionCreateForTaggedBufferGroupWithExtensions

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
extern OSStatus CMTaggedBufferGroupFormatDescriptionCreateForTaggedBufferGroupWithExtensions(CFAllocatorRef allocator, CMTaggedBufferGroupRef taggedBufferGroup, CFDictionaryRef extensions, CMTaggedBufferGroupFormatDescriptionRef*formatDescriptionOut);
```

## Discussion

Creates a format description for a CMTaggedBufferGroup with extensions.

The returned CMTaggedBufferGroupFormatDescription could be used to create a CMSampleBuffer wrapping the CMTaggedBufferGroup using CMSampleBufferCreateForTaggedBufferGroup. If you are going to call CMSampleBufferCreateForTaggedBufferGroup on a series of matching CMTaggedBufferGroups, it is more efficient to create the CMTaggedBufferGroupFormatDescription once and use it for all of the CMSampleBuffers. The caller owns the returned CMFormatDescription, and must release it when done with it. All input parameters are copied (the extensions are deep-copied).  The caller can deallocate them or re-use them after making this call.

## Parameters

- `allocator`: CFAllocator to be used when creating the CMFormatDescription. Pass kCFAllocatorDefault to use the default allocator.
- `taggedBufferGroup`: The tagged buffer group for which we are creating the format description.
- `extensions`: Dictionary of extension key/value pairs.  Keys are always CFStrings. Values are always property list objects (ie. CFData, CFString, CFArray, CFDictionary, CFDate, CFBoolean, or CFNumber). Can be NULL.
- `formatDescriptionOut`: Returned newly-created tagged buffer group CMFormatDescription


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffergroupformatdescriptioncreatefortaggedbuffergroupwithextensions)*