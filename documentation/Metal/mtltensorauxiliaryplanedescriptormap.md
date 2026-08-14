# MTLTensorAuxiliaryPlaneDescriptorMap

**Framework**: Metal  
**Kind**: class

A map of auxiliary plane descriptors keyed by plane type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class MTLTensorAuxiliaryPlaneDescriptorMap
```

#### Overview

Use this collection to associate [`MTLTensorPlaneType`](mtltensorplanetype.md) values with [`MTLTensorAuxiliaryPlaneDescriptor`](mtltensorauxiliaryplanedescriptor.md) configurations, then attach it to a [`MTLTensorDescriptor`](mtltensordescriptor.md) to create a multi-plane tensor.

## Topics

### Instance Methods
- [func descriptor(for: MTLTensorPlaneType) -> MTLTensorAuxiliaryPlaneDescriptor?](mtltensorauxiliaryplanedescriptormap/descriptor(for:).md)
  Returns the auxiliary plane descriptor for the given plane type, or `nil` if none has been set.
- [func reset()](mtltensorauxiliaryplanedescriptormap/reset.md)
  Empties the map of all its elements.
- [func setDescriptor(MTLTensorAuxiliaryPlaneDescriptor, for: MTLTensorPlaneType)](mtltensorauxiliaryplanedescriptormap/setdescriptor(_:for:).md)
  Sets the auxiliary plane descriptor for the given plane type.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptormap)*