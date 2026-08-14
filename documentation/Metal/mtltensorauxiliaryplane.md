# MTLTensorAuxiliaryPlane

**Framework**: Metal  
**Kind**: protocol

A type that represents the configuration and storage of an auxiliary plane in a multi-plane tensor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol MTLTensorAuxiliaryPlane : NSObjectProtocol
```

## Topics

### Instance Properties
- [var blockFactors: MTLTensorExtents](mtltensorauxiliaryplane/blockfactors.md)
  The number of data plane elements that correspond to one element in this auxiliary plane.
- [var buffer: (any MTLBuffer)?](mtltensorauxiliaryplane/buffer.md)
  The buffer that provides the underlying storage for this plane, or `nil` if no buffer was provided at initialization.
- [var bufferOffset: Int](mtltensorauxiliaryplane/bufferoffset.md)
  The byte offset into [`buffer`](mtltensorauxiliaryplane/buffer.md) where this plane’s data begins, or `0` if no buffer was provided at initialization.
- [var dataType: MTLTensorDataType](mtltensorauxiliaryplane/datatype.md)
  The data format of all elements in the plane.
- [var planeType: MTLTensorPlaneType](mtltensorauxiliaryplane/planetype.md)
  The type of information this plane stores.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplane)*