# MDLTransformOp

**Framework**: Model I/O  
**Kind**: protocol

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol MDLTransformOp
```

## Topics

### Instance Properties
- [var name: String](mdltransformop/name.md)
### Instance Methods
- [func double4x4(atTime: TimeInterval) -> matrix_double4x4](mdltransformop/double4x4(attime:).md)
- [func float4x4(atTime: TimeInterval) -> matrix_float4x4](mdltransformop/float4x4(attime:).md)
- [func isInverseOp() -> Bool](mdltransformop/isinverseop.md)

## Relationships

### Conforming Types
- [MDLTransformMatrixOp](mdltransformmatrixop.md)
- [MDLTransformOrientOp](mdltransformorientop.md)
- [MDLTransformRotateOp](mdltransformrotateop.md)
- [MDLTransformRotateXOp](mdltransformrotatexop.md)
- [MDLTransformRotateYOp](mdltransformrotateyop.md)
- [MDLTransformRotateZOp](mdltransformrotatezop.md)
- [MDLTransformScaleOp](mdltransformscaleop.md)
- [MDLTransformTranslateOp](mdltransformtranslateop.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransformop)*