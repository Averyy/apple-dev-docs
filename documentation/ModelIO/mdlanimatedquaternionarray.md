# MDLAnimatedQuaternionArray

**Framework**: Model I/O  
**Kind**: class  
**Role**: Class

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

```objc
@interface MDLAnimatedQuaternionArray : MDLAnimatedValue
```

## Topics

### Initializers
- [init(elementCount: Int)](./mdlanimatedquaternionarray/init%28elementcount%29.md)
### Instance Properties
- [var doubleQuaternionArray: [simd_quatd]](./mdlanimatedquaternionarray/doublequaternionarray.md)
- [var elementCount: Int](./mdlanimatedquaternionarray/elementcount.md)
- [var floatQuaternionArray: [simd_quatf]](./mdlanimatedquaternionarray/floatquaternionarray.md)
### Instance Methods
- [func doubleQuaternionArray(atTime: TimeInterval) -> [simd_quatd]](./mdlanimatedquaternionarray/doublequaternionarray%28attime%29.md)
- [func floatQuaternionArray(atTime: TimeInterval) -> [simd_quatf]](./mdlanimatedquaternionarray/floatquaternionarray%28attime%29.md)
- [func reset(doubleQuaternionArray: [simd_quatd], atTimes: [TimeInterval])](./mdlanimatedquaternionarray/reset%28doublequaternionarray,attimes%29.md)
- [func reset(floatQuaternionArray: [simd_quatf], atTimes: [TimeInterval])](./mdlanimatedquaternionarray/reset%28floatquaternionarray,attimes%29.md)
- [func set(doubleQuaternionArray: [simd_quatd], atTime: TimeInterval)](./mdlanimatedquaternionarray/set%28doublequaternionarray,attime%29.md)
- [func set(floatQuaternionArray: [simd_quatf], atTime: TimeInterval)](./mdlanimatedquaternionarray/set%28floatquaternionarray,attime%29.md)
- [- getDoubleQuaternionArray:maxCount:](./mdlanimatedquaternionarray/getdoublequaternionarray_maxcount_.md)
- [- getDoubleQuaternionArray:maxCount:atTime:](./mdlanimatedquaternionarray/getdoublequaternionarray_maxcount_attime_.md)
- [- getFloatQuaternionArray:maxCount:](./mdlanimatedquaternionarray/getfloatquaternionarray_maxcount_.md)
- [- getFloatQuaternionArray:maxCount:atTime:](./mdlanimatedquaternionarray/getfloatquaternionarray_maxcount_attime_.md)
- [- resetWithDoubleQuaternionArray:count:atTimes:count:](./mdlanimatedquaternionarray/resetwithdoublequaternionarray_count_attimes_count_.md)
- [- resetWithFloatQuaternionArray:count:atTimes:count:](./mdlanimatedquaternionarray/resetwithfloatquaternionarray_count_attimes_count_.md)
- [- setDoubleQuaternionArray:count:atTime:](./mdlanimatedquaternionarray/setdoublequaternionarray_count_attime_.md)
- [- setFloatQuaternionArray:count:atTime:](./mdlanimatedquaternionarray/setfloatquaternionarray_count_attime_.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlanimatedquaternionarray)*