# makeTensor(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a tensor with the specified descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeTensor(descriptor: MTLTensorDescriptor) throws -> any MTLTensor
```

#### Return Value

A tensor, or `nil` if validation fails.

#### Discussion

This method validates the constraints documented on [`MTLTensorDescriptor`](mtltensordescriptor.md).

## Parameters

- `descriptor`: The tensor descriptor configuring the data plane and auxiliary planes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/maketensor(descriptor:))*