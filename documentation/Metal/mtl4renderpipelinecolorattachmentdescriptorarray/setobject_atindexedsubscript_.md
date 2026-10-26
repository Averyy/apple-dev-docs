# setObject:atIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets an attachment at an index.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) setObject:(MTL4RenderPipelineColorAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

#### Discussion

This function offers ‘copy’ semantics.

You can safely set the color attachment at any legal index to nil. This has the effect of resetting that attachment descriptor’s state to its default values.

## Parameters

- `attachment`: The descriptor of the attachment to set.
- `attachmentIndex`: The index of the attachment within the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinecolorattachmentdescriptorarray/setobject:atindexedsubscript:)*