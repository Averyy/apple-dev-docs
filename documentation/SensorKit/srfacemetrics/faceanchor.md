# faceAnchor

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The anchor for the face that the sensor detects in front of the camera.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@NSCopying
var faceAnchor: ARFaceAnchor { get }
```

```objc
@property (nonatomic, copy, readonly) ARFaceAnchor * faceAnchor;
```

## See Also

### Getting face analytics
- [var partialFaceExpressions: [SRFaceMetricsExpression]](./partialfaceexpressions.md)
  The partial face expressions that the algorithm detects.
- [var wholeFaceExpressions: [SRFaceMetricsExpression]](./wholefaceexpressions.md)
  The whole face expressions that the algorithm detects.
- [class SRFaceMetricsExpression](../srfacemetricsexpression.md)
  An object that represents a facial expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfacemetrics/faceanchor)*