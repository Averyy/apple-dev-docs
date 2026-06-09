# setDescriptor(_:for:)

**Framework**: Metal  
**Kind**: method

Sets the auxiliary plane descriptor for the given plane type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func setDescriptor(_ descriptor: MTLTensorAuxiliaryPlaneDescriptor, for plane: MTLTensorPlaneType)
```

#### Discussion

[`MTLTensorPlaneType.data`](mtltensorplanetype/data.md) is not a valid plane type for this method. The data plane is always present, and you configure it directly on [`MTLTensorDescriptor`](mtltensordescriptor.md).

[`MTLTensorPlaneType.scales`](mtltensorplanetype/scales.md) auxiliary planes only support [`MTLTensorDataType.float8ue8m0`](mtltensordatatype/float8ue8m0.md) as a data type.

## Parameters

- `descriptor`: The descriptor configuring the auxiliary plane.
- `plane`: The plane type to associate the descriptor with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptormap/setdescriptor(_:for:))*