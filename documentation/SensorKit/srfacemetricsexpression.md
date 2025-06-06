# SRFaceMetricsExpression

**Framework**: SensorKit  
**Kind**: class

An object that represents a facial expression.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
class SRFaceMetricsExpression
```

#### Overview

Use the [`identifier`](srfacemetricsexpression/identifier.md) property to determine the facial expression.

## Topics

### Getting the expression identifier and analysis
- [var value: Double](srfacemetricsexpression/value.md)
  The current position of the expression.
- [var identifier: String](srfacemetricsexpression/identifier.md)
  An identifier for the facial expression.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var faceAnchor: ARFaceAnchor](srfacemetrics/faceanchor.md)
  The anchor for the face that the sensor detects in front of the camera.
- [var partialFaceExpressions: [SRFaceMetricsExpression]](srfacemetrics/partialfaceexpressions.md)
  The partial face expressions that the algorithm detects.
- [var wholeFaceExpressions: [SRFaceMetricsExpression]](srfacemetrics/wholefaceexpressions.md)
  The whole face expressions that the algorithm detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfacemetricsexpression)*