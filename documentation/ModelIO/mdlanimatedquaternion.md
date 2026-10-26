# MDLAnimatedQuaternion

**Framework**: Model I/O  
**Kind**: class  
**Role**: Class

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

```objc
@interface MDLAnimatedQuaternion : MDLAnimatedValue
```

## Topics

### Instance Properties
- [var doubleQuaternionArray: [simd_quatd]](./mdlanimatedquaternion/doublequaternionarray.md)
- [var floatQuaternionArray: [simd_quatf]](./mdlanimatedquaternion/floatquaternionarray.md)
### Instance Methods
- [func doubleQuaternionValue(atTime: TimeInterval) -> simd_quatd](./mdlanimatedquaternion/doublequaternionvalue%28attime%29.md)
- [func floatQuaternionValue(atTime: TimeInterval) -> simd_quatf](./mdlanimatedquaternion/floatquaternionvalue%28attime%29.md)
- [func reset(doubleQuaternionArray: [simd_quatd], atTimes: [TimeInterval])](./mdlanimatedquaternion/reset%28doublequaternionarray,attimes%29.md)
- [func reset(floatQuaternionArray: [simd_quatf], atTimes: [TimeInterval])](./mdlanimatedquaternion/reset%28floatquaternionarray,attimes%29.md)
- [func setDoubleQuaternion(simd_quatd, atTime: TimeInterval)](./mdlanimatedquaternion/setdoublequaternion%28_,attime%29.md)
- [func setFloatQuaternion(simd_quatf, atTime: TimeInterval)](./mdlanimatedquaternion/setfloatquaternion%28_,attime%29.md)
- [- getDoubleQuaternionArray:maxCount:](./mdlanimatedquaternion/getdoublequaternionarray_maxcount_.md)
- [- getFloatQuaternionArray:maxCount:](./mdlanimatedquaternion/getfloatquaternionarray_maxcount_.md)
- [- resetWithDoubleQuaternionArray:atTimes:count:](./mdlanimatedquaternion/resetwithdoublequaternionarray_attimes_count_.md)
- [- resetWithFloatQuaternionArray:atTimes:count:](./mdlanimatedquaternion/resetwithfloatquaternionarray_attimes_count_.md)

## Relationships

### Inherits From
- [MDLAnimatedValue](./mdlanimatedvalue.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlanimatedquaternion)*