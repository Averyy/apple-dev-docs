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
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(MTLResourceStatePassSampleBufferAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

## Discussion

The method copies the `attachment` parameter’s contents into the attachment at the specified index..

## Parameters

- `attachment`: A sample buffer attachment descriptor. If you specify `nil`, the attachment descriptor resets its configuration to default values.
- `attachmentIndex`: The item in the array to replace.

## See Also

### Accessing a sample buffer attachment
- [subscript(Int) -> MTLResourceStatePassSampleBufferAttachmentDescriptor!](./subscript%28_%29.md)
  Returns the descriptor object for the specified sample buffer attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourcestatepasssamplebufferattachmentdescriptorarray/setobject:atindexedsubscript:)*