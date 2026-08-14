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

- [var SR_ARKIT_SUPPORTED: Int32](sr_arkit_supported.md)
  A flag that indicates whether the ARKit framework is available in the SDK for the SensorKit framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfacemetrics)*