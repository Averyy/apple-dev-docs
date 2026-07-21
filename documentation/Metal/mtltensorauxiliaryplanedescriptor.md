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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptor)*