# SRFaceMetricsExpression

**Framework**: SensorKit  
**Kind**: class  
**Role**: Class

An object that represents a facial expression.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
class SRFaceMetricsExpression
```

```objc
@interface SRFaceMetricsExpression : NSObject
```

## Overview

Use the [`identifier`](./srfacemetricsexpression/identifier.md) property to determine the facial expression.

## Topics

### Getting the expression identifier and analysis
- [var value: Double](./srfacemetricsexpression/value.md)
  The current position of the expression.
- [var identifier: String](./srfacemetricsexpression/identifier.md)
  An identifier for the facial expression.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting face analytics
- [var faceAnchor: ARFaceAnchor](./srfacemetrics/faceanchor.md)
  The anchor for the face that the sensor detects in front of the camera.
- [var partialFaceExpressions: [SRFaceMetricsExpression]](./srfacemetrics/partialfaceexpressions.md)
  The partial face expressions that the algorithm detects.
- [var wholeFaceExpressions: [SRFaceMetricsExpression]](./srfacemetrics/wholefaceexpressions.md)
  The whole face expressions that the algorithm detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfacemetricsexpression)*