# monocularFrustumMatrix(convention:viewIndex:increaseTangents:depthRange:)

**Framework**: Compositor Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 26.0+
- visionOS 2.0+ - Deprecated in 26.0 (renamed: monocularFrustumMatrixForDrawableTarget)

## Declaration

```swift
func monocularFrustumMatrix(convention: AxisDirectionConvention = .rightUpBack, viewIndex: Int, increaseTangents: SIMD4<Float>, depthRange: SIMD2<Float>) -> matrix_float4x4
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/monocularfrustummatrix(convention:viewindex:increasetangents:depthrange:))*