# CMTaggedBufferGroupFormatDescriptionMatchesTaggedBufferGroup

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Checks to see if a tagged buffer group’s format matches an existing format description.

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
extern Boolean CMTaggedBufferGroupFormatDescriptionMatchesTaggedBufferGroup(CMTaggedBufferGroupFormatDescriptionRef desc, CMTaggedBufferGroupRef taggedBufferGroup);
```

#### Return Value

Returns `YES` when the format description of `taggedBufferGroup` is equal to the description `desc`.

## Parameters

- `desc`: A tagged buffer format description, created by [`CMTaggedBufferGroupFormatDescriptionCreateForTaggedBufferGroup`](./cmtaggedbuffergroupformatdescriptioncreatefortaggedbuffergroup.md).
- `taggedBufferGroup`: The tagged buffer group to inspect the format of.

## See Also

### Inspecting Buffer Format
- [CMTaggedBufferGroupFormatDescriptionCreateForTaggedBufferGroup](./cmtaggedbuffergroupformatdescriptioncreatefortaggedbuffergroup.md)
  Creates a new format description for a tagged buffer group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtaggedbuffergroupformatdescriptionmatchestaggedbuffergroup)*