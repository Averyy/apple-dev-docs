# setObject:atIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets the render pipeline state for a specified color attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(MTLRenderPipelineColorAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

#### Discussion

This method copies the pipeline state from the descriptor into the specified attachment in the array. The descriptor passed into this method can be modified and reused without affecting a previously set attachment.

If this method is called with `nil` for `attachment` for any legal index, its attachment descriptor state is set to the default values.

## Parameters

- `attachment`: A descriptor that contains the render pipeline description for a color attachment.
- `attachmentIndex`: An index in the color attachment array.

## See Also

### Accessing render pipeline state for a color attachment
- [subscript(Int) -> MTLRenderPipelineColorAttachmentDescriptor!](./subscript%28_%29.md)
  Returns the render pipeline state for the specified color attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptorarray/setobject:atindexedsubscript:)*