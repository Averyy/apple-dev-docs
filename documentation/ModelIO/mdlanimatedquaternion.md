# MDLAnimatedQuaternion

**Framework**: Model I/O  
**Kind**: class

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MDLAnimatedQuaternion
```

## Topics

### Instance Properties
- [var doubleQuaternionArray: [simd_quatd]](mdlanimatedquaternion/doublequaternionarray.md)
- [var floatQuaternionArray: [simd_quatf]](mdlanimatedquaternion/floatquaternionarray.md)
### Instance Methods
- [func doubleQuaternionValue(atTime: TimeInterval) -> simd_quatd](mdlanimatedquaternion/doublequaternionvalue(attime:).md)
- [func floatQuaternionValue(atTime: TimeInterval) -> simd_quatf](mdlanimatedquaternion/floatquaternionvalue(attime:).md)
- [func reset(doubleQuaternionArray: [simd_quatd], atTimes: [TimeInterval])](mdlanimatedquaternion/reset(doublequaternionarray:attimes:).md)
- [func reset(floatQuaternionArray: [simd_quatf], atTimes: [TimeInterval])](mdlanimatedquaternion/reset(floatquaternionarray:attimes:).md)
- [func setDoubleQuaternion(simd_quatd, atTime: TimeInterval)](mdlanimatedquaternion/setdoublequaternion(_:attime:).md)
- [func setFloatQuaternion(simd_quatf, atTime: TimeInterval)](mdlanimatedquaternion/setfloatquaternion(_:attime:).md)

## Relationships

### Inherits From
- [MDLAnimatedValue](mdlanimatedvalue.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlanimatedquaternion)*