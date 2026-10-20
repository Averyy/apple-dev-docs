# MDLAnimatedMatrix4x4

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
class MDLAnimatedMatrix4x4
```

```objc
@interface MDLAnimatedMatrix4x4 : MDLAnimatedValue
```

## Topics

### Instance Properties
- [var double4x4Array: [double4x4]](./mdlanimatedmatrix4x4/double4x4array.md)
- [var float4x4Array: [float4x4]](./mdlanimatedmatrix4x4/float4x4array.md)
### Instance Methods
- [func double4x4Value(atTime: TimeInterval) -> matrix_double4x4](./mdlanimatedmatrix4x4/double4x4value%28attime%29.md)
- [func float4x4Value(atTime: TimeInterval) -> matrix_float4x4](./mdlanimatedmatrix4x4/float4x4value%28attime%29.md)
- [func reset(double4Array: [double4x4], atTimes: [TimeInterval])](./mdlanimatedmatrix4x4/reset%28double4array,attimes%29.md)
- [func reset(float4x4Array: [float4x4], atTimes: [TimeInterval])](./mdlanimatedmatrix4x4/reset%28float4x4array,attimes%29.md)
- [func setDouble4x4(matrix_double4x4, atTime: TimeInterval)](./mdlanimatedmatrix4x4/setdouble4x4%28_,attime%29.md)
- [func setFloat4x4(matrix_float4x4, atTime: TimeInterval)](./mdlanimatedmatrix4x4/setfloat4x4%28_,attime%29.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlanimatedmatrix4x4)*