# MTLVertexFormat.floatRG11B10

**Framework**: Metal  
**Kind**: case

A three-component vector with 11-bit floating-point values for red and green, and a 10-bit value for blue.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case floatRG11B10
```

#### Discussion

The 11-bit components for red and green each store five exponent bits and six mantissa bits. The 10-bit blue component stores five exponent bits and five mantissa bits.

## See Also

- [MTLVertexFormat.float](mtlvertexformat/float.md)
  A 32-bit floating-point value.
- [MTLVertexFormat.float2](mtlvertexformat/float2.md)
  A two-component vector with 32-bit floating-point values.
- [MTLVertexFormat.float3](mtlvertexformat/float3.md)
  A three-component vector with 32-bit floating-point values.
- [MTLVertexFormat.float4](mtlvertexformat/float4.md)
  A four-component vector with 32-bit floating-point values.
- [MTLVertexFormat.floatRGB9E5](mtlvertexformat/floatrgb9e5.md)
  A three-component vector with 9-bit floating-point values for red, green, and blue, and a 5-bit shared exponent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexformat/floatrg11b10)*