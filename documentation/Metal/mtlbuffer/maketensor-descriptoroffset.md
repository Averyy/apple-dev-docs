# makeTensor(descriptor:offset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a single-plane tensor with the specified descriptor that shares storage with this buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeTensor(descriptor: MTLTensorDescriptor, offset: Int) throws -> any MTLTensor
```

#### Return Value

A tensor, or `nil` if validation fails.

#### Discussion

This method validates the constraints documented on [`MTLTensorDescriptor`](mtltensordescriptor.md), and additionally requires:

- `offset` is 0 when [`usage`](mtltensordescriptor/usage.md) contains [`machineLearning`](mtltensorusage/machinelearning.md).
- `offset` is aligned to 128 bytes if the data plane uses a format [`MTLTensorDataType`](mtltensordatatype.md).
- `offset` is aligned to the size of the data type in bytes otherwise.

This method doesn’t create tensors that contain auxiliary planes. Use [`makeTensor(descriptor:attachments:)`](mtldevice/maketensor(descriptor:attachments:).md) instead to create a multi-plane tensor with per-plane buffer backing storage.

## Parameters

- `descriptor`: The tensor descriptor configuring the data plane.
- `offset`: The byte offset into the buffer where tensor data begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer/maketensor(descriptor:offset:))*