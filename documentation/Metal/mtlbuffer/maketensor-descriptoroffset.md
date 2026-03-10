# makeTensor(descriptor:offset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a tensor that shares storage with this buffer.

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

The created [`MTLTensor`](mtltensor.md) instance, or `nil` if the function failed.

#### Discussion

`offset` must be 0 when [`usage`](mtltensordescriptor/usage.md) contains [`machineLearning`](mtltensorusage/machinelearning.md).

When [`dataType`](mtltensordescriptor/datatype.md) is a sub-byte [`MTLTensorDataType`](mtltensordatatype.md), `offset` must be aligned to 128 bytes. Although only required for sub-byte types, applying 128-byte alignment for all [`MTLTensorDataType`](mtltensordatatype.md) values improves performance.

See [`MTLTensorDescriptor`](mtltensordescriptor.md) for more information.

## Parameters

- `descriptor`: A description of the properties for the new tensor.
- `offset`: Offset into the buffer at which the data of the tensor begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffer/maketensor(descriptor:offset:))*