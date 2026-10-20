# partialFaceExpressions

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The partial face expressions that the algorithm detects.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var partialFaceExpressions: [SRFaceMetricsExpression] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<SRFaceMetricsExpression *> * partialFaceExpressions;
```

## See Also

### Getting face analytics
- [var faceAnchor: ARFaceAnchor](./faceanchor.md)
  The anchor for the face that the sensor detects in front of the camera.
- [var wholeFaceExpressions: [SRFaceMetricsExpression]](./wholefaceexpressions.md)
  The whole face expressions that the algorithm detects.
- [class SRFaceMetricsExpression](../srfacemetricsexpression.md)
  An object that represents a facial expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfacemetrics/partialfaceexpressions)*