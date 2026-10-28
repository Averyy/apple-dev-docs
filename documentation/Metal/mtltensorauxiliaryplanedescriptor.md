# MTLTensorAuxiliaryPlaneDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

A configuration for an auxiliary plane in a multi-plane tensor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class MTLTensorAuxiliaryPlaneDescriptor
```

```objc
@interface MTLTensorAuxiliaryPlaneDescriptor : NSObject
```

## Overview

Use this descriptor to configure an auxiliary plane’s data type and block factors before attaching it to a [`MTLTensorDescriptor`](./mtltensordescriptor.md).

## Topics

### Instance Properties
- [var blockFactors: MTLTensorExtents](./mtltensorauxiliaryplanedescriptor/blockfactors.md)
  An extents instance that represents the number of data plane elements which correspond to one element in a plane you create with this descriptor.
- [var dataType: MTLTensorDataType](./mtltensorauxiliaryplanedescriptor/datatype.md)
  The data format of all elements in the plane.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptor)*