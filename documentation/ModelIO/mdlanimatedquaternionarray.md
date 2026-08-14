# MDLAnimatedQuaternionArray

**Framework**: Model I/O  
**Kind**: class

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MDLAnimatedQuaternionArray
```

## Topics

### Initializers
- [init(elementCount: Int)](mdlanimatedquaternionarray/init(elementcount:).md)
### Instance Properties
- [var doubleQuaternionArray: [simd_quatd]](mdlanimatedquaternionarray/doublequaternionarray.md)
- [var elementCount: Int](mdlanimatedquaternionarray/elementcount.md)
- [var floatQuaternionArray: [simd_quatf]](mdlanimatedquaternionarray/floatquaternionarray.md)
### Instance Methods
- [func doubleQuaternionArray(atTime: TimeInterval) -> [simd_quatd]](mdlanimatedquaternionarray/doublequaternionarray(attime:).md)
- [func floatQuaternionArray(atTime: TimeInterval) -> [simd_quatf]](mdlanimatedquaternionarray/floatquaternionarray(attime:).md)
- [func reset(doubleQuaternionArray: [simd_quatd], atTimes: [TimeInterval])](mdlanimatedquaternionarray/reset(doublequaternionarray:attimes:).md)
- [func reset(floatQuaternionArray: [simd_quatf], atTimes: [TimeInterval])](mdlanimatedquaternionarray/reset(floatquaternionarray:attimes:).md)
- [func set(doubleQuaternionArray: [simd_quatd], atTime: TimeInterval)](mdlanimatedquaternionarray/set(doublequaternionarray:attime:).md)
- [func set(floatQuaternionArray: [simd_quatf], atTime: TimeInterval)](mdlanimatedquaternionarray/set(floatquaternionarray:attime:).md)

## Relationships

### Inherits From
- [MDLAnimatedValue](mdlanimatedvalue.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlanimatedquaternionarray)*