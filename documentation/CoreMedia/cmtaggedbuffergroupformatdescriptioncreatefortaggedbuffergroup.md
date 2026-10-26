# CMTaggedBufferGroupFormatDescriptionCreateForTaggedBufferGroup

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a new format description for a tagged buffer group.

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
extern OSStatus CMTaggedBufferGroupFormatDescriptionCreateForTaggedBufferGroup(CFAllocatorRef allocator, CMTaggedBufferGroupRef taggedBufferGroup, CMTaggedBufferGroupFormatDescriptionRef*formatDescriptionOut);
```

#### Return Value

Returns `0` on success and a value from Tagged Buffer Group Error Codes on failure.

## Parameters

- `allocator`: The allocator to use for the format description. Pass `kCFAllocatorDefault` to use the default global allocator.
- `taggedBufferGroup`: The tagged buffer group to inspect.
- `formatDescriptionOut`: The output destination for the new format description.

## See Also

### Inspecting Buffer Format
- [CMTaggedBufferGroupFormatDescriptionMatchesTaggedBufferGroup](./cmtaggedbuffergroupformatdescriptionmatchestaggedbuffergroup.md)
  Checks to see if a tagged buffer group’s format matches an existing format description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffergroupformatdescriptioncreatefortaggedbuffergroup)*