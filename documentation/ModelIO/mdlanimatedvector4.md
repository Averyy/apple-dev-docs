# MDLAnimatedVector4

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
class MDLAnimatedVector4
```

```objc
@interface MDLAnimatedVector4 : MDLAnimatedValue
```

## Topics

### Instance Properties
- [var double4Array: [SIMD4<Double>]](./mdlanimatedvector4/double4array.md)
- [var float4Array: [SIMD4<Float>]](./mdlanimatedvector4/float4array.md)
### Instance Methods
- [func double4Value(atTime: TimeInterval) -> vector_double4](./mdlanimatedvector4/double4value%28attime%29.md)
- [func float4Value(atTime: TimeInterval) -> vector_float4](./mdlanimatedvector4/float4value%28attime%29.md)
- [func reset(double4Array: [SIMD4<Double>], atTimes: [TimeInterval])](./mdlanimatedvector4/reset%28double4array,attimes%29.md)
- [func reset(float4Array: [SIMD4<Float>], atTimes: [TimeInterval])](./mdlanimatedvector4/reset%28float4array,attimes%29.md)
- [func setDouble4(vector_double4, atTime: TimeInterval)](./mdlanimatedvector4/setdouble4%28_,attime%29.md)
- [func setFloat4(vector_float4, atTime: TimeInterval)](./mdlanimatedvector4/setfloat4%28_,attime%29.md)
- [- getDouble4Array:maxCount:](./mdlanimatedvector4/getdouble4array_maxcount_.md)
- [- getFloat4Array:maxCount:](./mdlanimatedvector4/getfloat4array_maxcount_.md)
- [- resetWithDouble4Array:atTimes:count:](./mdlanimatedvector4/resetwithdouble4array_attimes_count_.md)
- [- resetWithFloat4Array:atTimes:count:](./mdlanimatedvector4/resetwithfloat4array_attimes_count_.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlanimatedvector4)*