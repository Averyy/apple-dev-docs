# SRFaceMetrics

**Framework**: SensorKit  
**Kind**: class

An object that represents metrics about the user’s face.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
class SRFaceMetrics
```

#### Overview

The [`faceMetrics`](srsensor/facemetrics.md) sensor provides this class as its [`sample`](srfetchresult/sample.md) type.

## Topics

### Getting session information
- [var sessionIdentifier: String](srfacemetrics/sessionidentifier.md)
  An identifier for the camera session.
- [var context: SRFaceMetrics.Context](srfacemetrics/context-swift.property.md)
  The context of the system during the camera session.
- [SRFaceMetrics.Context](srfacemetrics/context-swift.struct.md)
  The context of the system during the camera session.
- [var version: String](srfacemetrics/version.md)
  The version of the algorithm that the system uses to generate the face metrics and analytics.
### Getting face analytics
- [var faceAnchor: ARFaceAnchor](srfacemetrics/faceanchor.md)
  The anchor for the face that the sensor detects in front of the camera.
- [var partialFaceExpressions: [SRFaceMetricsExpression]](srfacemetrics/partialfaceexpressions.md)
  The partial face expressions that the algorithm detects.
- [var wholeFaceExpressions: [SRFaceMetricsExpression]](srfacemetrics/wholefaceexpressions.md)
  The whole face expressions that the algorithm detects.
- [class SRFaceMetricsExpression](srfacemetricsexpression.md)
  An object that represents a facial expression.

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var SR_ARKIT_SUPPORTED: Int32](sr_arkit_supported.md)
  A flag that indicates whether the ARKit framework is available in the SDK for the SensorKit framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfacemetrics)*