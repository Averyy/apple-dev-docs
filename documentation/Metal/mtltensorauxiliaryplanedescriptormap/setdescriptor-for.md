# setDescriptor(_:for:)

**Framework**: Metal  
**Kind**: method

Sets the auxiliary plane descriptor for the given plane type.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func setDescriptor(_ descriptor: MTLTensorAuxiliaryPlaneDescriptor, for plane: MTLTensorPlaneType)
```

#### Discussion

[`MTLTensorPlaneType.data`](mtltensorplanetype/data.md) is not a valid plane type for this method. The data plane is always present, and you configure it directly on [`MTLTensorDescriptor`](mtltensordescriptor.md).

[`MTLTensorPlaneType.scales`](mtltensorplanetype/scales.md) auxiliary planes only support [`MTLTensorDataType.metalFloat8ue8m0`](mtltensordatatype/metalfloat8ue8m0.md) as a data type.

## Parameters

- `descriptor`: The descriptor configuring the auxiliary plane.
- `plane`: The plane type to associate the descriptor with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptormap/setdescriptor(_:for:))*