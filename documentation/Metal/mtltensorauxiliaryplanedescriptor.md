# MTLTensorAuxiliaryPlaneDescriptor

**Framework**: Metal  
**Kind**: class

A configuration for an auxiliary plane in a multi-plane tensor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class MTLTensorAuxiliaryPlaneDescriptor
```

#### Overview

Use this descriptor to configure an auxiliary plane’s data type and block factors before attaching it to a [`MTLTensorDescriptor`](mtltensordescriptor.md).

## Topics

### Instance Properties
- [var blockFactors: MTLTensorExtents](mtltensorauxiliaryplanedescriptor/blockfactors.md)
  An extents instance that represents the number of data plane elements which correspond to one element in a plane you create with this descriptor.
- [var dataType: MTLTensorDataType](mtltensorauxiliaryplanedescriptor/datatype.md)
  The data format of all elements in the plane.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptor)*