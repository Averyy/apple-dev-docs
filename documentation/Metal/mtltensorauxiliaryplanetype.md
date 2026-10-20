# MTLTensorAuxiliaryPlaneType

**Framework**: Metal  
**Kind**: class  
**Role**: Class

An auxiliary plane that a shader’s tensor argument requires.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class MTLTensorAuxiliaryPlaneType
```

```objc
@interface MTLTensorAuxiliaryPlaneType : NSObject
```

## Topics

### Instance Properties
- [var blockFactors: MTLTensorExtents](./mtltensorauxiliaryplanetype/blockfactors.md)
  The number of data plane elements that correspond to one element in this plane.
- [var dataType: MTLTensorDataType](./mtltensorauxiliaryplanetype/datatype.md)
  The data format of all elements in the plane.
- [var planeType: MTLTensorPlaneType](./mtltensorauxiliaryplanetype/planetype.md)
  The type of information this plane stores.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanetype)*