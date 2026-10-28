# setObject:atIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Sets the descriptor for the specified color attachment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(MTLRenderPassColorAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

## Discussion

This method copies the color attachment information from the descriptor into the specified attachment in the array. Because the method copies the information, you can modify and reuse the descriptor without affecting a previously set attachment.

## Parameters

- `attachment`: A descriptor that contains color attachment information. Specify `nil` to reset the attachment to its default values.
- `attachmentIndex`: An index in the color attachment array.

## See Also

### Accessing the description of a color attachment
- [subscript(Int) -> MTLRenderPassColorAttachmentDescriptor!](./subscript%28_%29.md)
  Returns the descriptor object for the specified color attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptorarray/setobject:atindexedsubscript:)*