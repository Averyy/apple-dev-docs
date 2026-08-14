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
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var faceAnchor: ARFaceAnchor](srfacemetrics/faceanchor.md)
  The anchor for the face that the sensor detects in front of the camera.
- [var partialFaceExpressions: [SRFaceMetricsExpression]](srfacemetrics/partialfaceexpressions.md)
  The partial face expressions that the algorithm detects.
- [var wholeFaceExpressions: [SRFaceMetricsExpression]](srfacemetrics/wholefaceexpressions.md)
  The whole face expressions that the algorithm detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfacemetricsexpression)*