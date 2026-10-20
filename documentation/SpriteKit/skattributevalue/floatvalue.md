# floatValue

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The receiver’s floating point value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var floatValue: Float { get set }
```

```objc
@property (nonatomic) float floatValue;
```

#### Discussion

If the receiver’s original value is a vector, [`floatValue`](./floatvalue.md) is the first element of the vector.

## See Also

### Instance Properties
- [var vectorFloat2Value: vector_float2](./vectorfloat2value.md)
  The receiver’s value as a vector of two floating-point numbers.
- [var vectorFloat3Value: vector_float3](./vectorfloat3value.md)
  The receiver’s value as a vector of three floating point numbers.
- [var vectorFloat4Value: vector_float4](./vectorfloat4value.md)
  The receiver’s value as a vector of four floating point numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skattributevalue/floatvalue)*