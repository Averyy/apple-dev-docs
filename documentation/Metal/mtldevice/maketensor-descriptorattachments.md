# makeTensor(descriptor:attachments:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a tensor with the specified descriptor and per-plane buffer backing storage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func makeTensor(descriptor: MTLTensorDescriptor, attachments: MTLTensorBufferAttachments) throws -> any MTLTensor
```

#### Return Value

A tensor, or `nil` if validation fails.

#### Discussion

This method validates the constraints documented on [`MTLTensorDescriptor`](mtltensordescriptor.md) and [`MTLTensorBufferAttachments`](mtltensorbufferattachments.md), and additionally requires that every plane configured in `descriptor` (data plane and all auxiliary planes) has a corresponding entry in `attachments`.

## Parameters

- `descriptor`: The tensor descriptor configuring the data plane and auxiliary planes.
- `attachments`: The per-plane buffer backing storage. Must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/maketensor(descriptor:attachments:))*