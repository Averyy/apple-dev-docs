# MTLTensorAuxiliaryPlaneDescriptorMap

**Framework**: Metal  
**Kind**: class  
**Role**: Class

A map of auxiliary plane descriptors keyed by plane type.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class MTLTensorAuxiliaryPlaneDescriptorMap
```

```objc
@interface MTLTensorAuxiliaryPlaneDescriptorMap : NSObject
```

## Overview

Use this collection to associate [`MTLTensorPlaneType`](./mtltensorplanetype.md) values with [`MTLTensorAuxiliaryPlaneDescriptor`](./mtltensorauxiliaryplanedescriptor.md) configurations, then attach it to a [`MTLTensorDescriptor`](./mtltensordescriptor.md) to create a multi-plane tensor.

## Topics

### Instance Methods
- [func descriptor(for: MTLTensorPlaneType) -> MTLTensorAuxiliaryPlaneDescriptor?](./mtltensorauxiliaryplanedescriptormap/descriptor%28for%29.md)
  Returns the auxiliary plane descriptor for the given plane type, or `nil` if none has been set.
- [func reset()](./mtltensorauxiliaryplanedescriptormap/reset%28%29.md)
  Empties the map of all its elements.
- [func setDescriptor(MTLTensorAuxiliaryPlaneDescriptor, for: MTLTensorPlaneType)](./mtltensorauxiliaryplanedescriptormap/setdescriptor%28_,for%29.md)
  Sets the auxiliary plane descriptor for the given plane type.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptormap)*