# vectorFloat4Value

**Framework**: SpriteKit  
**Kind**: property

The receiver’s value as a vector of four floating point numbers.

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
var vectorFloat4Value: vector_float4 { get set }
```

#### Discussion

If the receiver’s original value is a floating-point number of a vector with a count less than four, the empty items in the vector are set to 0.

## See Also

- [var floatValue: Float](skattributevalue/floatvalue.md)
  The receiver’s floating point value.
- [var vectorFloat2Value: vector_float2](skattributevalue/vectorfloat2value.md)
  The receiver’s value as a vector of two floating-point numbers.
- [var vectorFloat3Value: vector_float3](skattributevalue/vectorfloat3value.md)
  The receiver’s value as a vector of three floating point numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skattributevalue/vectorfloat4value)*