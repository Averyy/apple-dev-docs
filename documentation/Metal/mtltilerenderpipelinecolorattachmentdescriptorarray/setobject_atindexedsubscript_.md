# setObject:atIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets the render pipeline state for a specified color attachment.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(MTLTileRenderPipelineColorAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

#### Discussion

This method copies the pipeline state from the descriptor into the specified attachment in the array. Afterwards, you can modify and reuse the descriptior without affecting a previously set attachment.

## Parameters

- `attachment`: A descriptor that contains the render pipeline description for a color attachment. Specify `nil` to reset the entry to default values.
- `attachmentIndex`: An index in the color attachment array.

## See Also

### Instance methods
- [subscript(Int) -> MTLTileRenderPipelineColorAttachmentDescriptor](./subscript%28_%29.md)
  Returns the render pipeline state for the specified color attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltilerenderpipelinecolorattachmentdescriptorarray/setobject:atindexedsubscript:)*