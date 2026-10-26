# setObject:atIndexedSubscript:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Copies the properties of a blit pass sample buffer attachment descriptor instance to the properties of one of the array’s instances.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(MTLBlitPassSampleBufferAttachmentDescriptor *) attachment atIndexedSubscript:(NSUInteger) attachmentIndex;
```

#### Discussion

The array has at

## Parameters

- `attachment`: An [`MTLBlitPassSampleBufferAttachmentDescriptor`](../mtlblitpasssamplebufferattachmentdescriptor.md) instance that the method assigns its properties values to the properties of the array’s instance at `attachmentIndex`.

  You can reset the property configuration of the array’s instance at `attachmentIndex` to its default values by passing `nil`.
- `attachmentIndex`: An index into the array’s copies of attachment descriptor instances.

## See Also

### Accessing a sample buffer attachment descriptor
- [subscript(Int) -> MTLBlitPassSampleBufferAttachmentDescriptor!](./subscript%28_%29.md)
  Accesses one of the array’s blit pass sample buffer attachment descriptor instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitpasssamplebufferattachmentdescriptorarray/setobject:atindexedsubscript:)*