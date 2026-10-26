# subscript(_:)

**Framework**: Metal  
**Kind**: subscript  
**Role**: Instance Subscript

Returns the descriptor object for the specified sample buffer attachment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
subscript(attachmentIndex: Int) -> MTLComputePassSampleBufferAttachmentDescriptor! { get set }
```

```objc
- (MTLComputePassSampleBufferAttachmentDescriptor *) objectAtIndexedSubscript:(NSUInteger) attachmentIndex;
```

#### Return Value

The requested  [`MTLComputePassSampleBufferAttachmentDescriptor`](../mtlcomputepasssamplebufferattachmentdescriptor.md) object.

## Parameters

- `attachmentIndex`: An index for the sample buffer attachment to fetch.

## See Also

### Accessing a sample buffer attachment
- [- setObject:atIndexedSubscript:](./setobject_atindexedsubscript_.md)
  Sets the descriptor object for the specified sample buffer attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepasssamplebufferattachmentdescriptorarray/subscript(_:))*