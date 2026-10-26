# MDLAnimatedVector3

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
class MDLAnimatedVector3
```

```objc
@interface MDLAnimatedVector3 : MDLAnimatedValue
```

## Topics

### Instance Properties
- [var double3Array: [SIMD3<Double>]](./mdlanimatedvector3/double3array.md)
- [var float3Array: [SIMD3<Float>]](./mdlanimatedvector3/float3array.md)
### Instance Methods
- [func double3Value(atTime: TimeInterval) -> vector_double3](./mdlanimatedvector3/double3value%28attime%29.md)
- [func float3Value(atTime: TimeInterval) -> vector_float3](./mdlanimatedvector3/float3value%28attime%29.md)
- [func reset(double3Array: [SIMD3<Double>], atTimes: [TimeInterval])](./mdlanimatedvector3/reset%28double3array,attimes%29.md)
- [func reset(float3Array: [SIMD3<Float>], atTimes: [TimeInterval])](./mdlanimatedvector3/reset%28float3array,attimes%29.md)
- [func setDouble3(vector_double3, atTime: TimeInterval)](./mdlanimatedvector3/setdouble3%28_,attime%29.md)
- [func setFloat3(vector_float3, atTime: TimeInterval)](./mdlanimatedvector3/setfloat3%28_,attime%29.md)
- [- getDouble3Array:maxCount:](./mdlanimatedvector3/getdouble3array_maxcount_.md)
- [- getFloat3Array:maxCount:](./mdlanimatedvector3/getfloat3array_maxcount_.md)
- [- resetWithDouble3Array:atTimes:count:](./mdlanimatedvector3/resetwithdouble3array_attimes_count_.md)
- [- resetWithFloat3Array:atTimes:count:](./mdlanimatedvector3/resetwithfloat3array_attimes_count_.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlanimatedvector3)*