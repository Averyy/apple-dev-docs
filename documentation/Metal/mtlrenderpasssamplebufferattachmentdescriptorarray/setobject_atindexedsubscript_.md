# setObject:atIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets the descriptor object for the specified sample buffer attachment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(MTLRenderPassSampleBufferAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

#### Discussion

The method copies the parameter contents into the attachment.

## Parameters

- `attachment`: A sample buffer attachment descriptor. Specify `nil` to resets the attachment to default values.
- `attachmentIndex`: The item in the array to replace.

## See Also

### Accessing a sample buffer attachment
- [subscript(Int) -> MTLRenderPassSampleBufferAttachmentDescriptor!](./subscript%28_%29.md)
  Returns the descriptor object for the specified sample buffer attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpasssamplebufferattachmentdescriptorarray/setobject:atindexedsubscript:)*