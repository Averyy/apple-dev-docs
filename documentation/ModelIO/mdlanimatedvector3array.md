# MDLAnimatedVector3Array

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
class MDLAnimatedVector3Array
```

```objc
@interface MDLAnimatedVector3Array : MDLAnimatedValue
```

## Topics

### Initializers
- [init(elementCount: Int)](./mdlanimatedvector3array/init%28elementcount%29.md)
### Instance Properties
- [var double3Array: [SIMD3<Double>]](./mdlanimatedvector3array/double3array.md)
- [var elementCount: Int](./mdlanimatedvector3array/elementcount.md)
- [var float3Array: [SIMD3<Float>]](./mdlanimatedvector3array/float3array.md)
### Instance Methods
- [func double3Array(atTime: TimeInterval) -> [SIMD3<Double>]](./mdlanimatedvector3array/double3array%28attime%29.md)
- [func float3Array(atTime: TimeInterval) -> [SIMD3<Float>]](./mdlanimatedvector3array/float3array%28attime%29.md)
- [func reset(double3Array: [SIMD3<Double>], atTimes: [TimeInterval])](./mdlanimatedvector3array/reset%28double3array,attimes%29.md)
- [func reset(float3Array: [SIMD3<Float>], atTimes: [TimeInterval])](./mdlanimatedvector3array/reset%28float3array,attimes%29.md)
- [func set(double3Array: [SIMD3<Double>], atTime: TimeInterval)](./mdlanimatedvector3array/set%28double3array,attime%29.md)
- [func set(float3Array: [SIMD3<Float>], atTime: TimeInterval)](./mdlanimatedvector3array/set%28float3array,attime%29.md)
- [- getDouble3Array:maxCount:](./mdlanimatedvector3array/getdouble3array_maxcount_.md)
- [- getDouble3Array:maxCount:atTime:](./mdlanimatedvector3array/getdouble3array_maxcount_attime_.md)
- [- getFloat3Array:maxCount:](./mdlanimatedvector3array/getfloat3array_maxcount_.md)
- [- getFloat3Array:maxCount:atTime:](./mdlanimatedvector3array/getfloat3array_maxcount_attime_.md)
- [- resetWithDouble3Array:count:atTimes:count:](./mdlanimatedvector3array/resetwithdouble3array_count_attimes_count_.md)
- [- resetWithFloat3Array:count:atTimes:count:](./mdlanimatedvector3array/resetwithfloat3array_count_attimes_count_.md)
- [- setDouble3Array:count:atTime:](./mdlanimatedvector3array/setdouble3array_count_attime_.md)
- [- setFloat3Array:count:atTime:](./mdlanimatedvector3array/setfloat3array_count_attime_.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlanimatedvector3array)*