# sessionIdentifier

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

An identifier for the camera session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var sessionIdentifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * sessionIdentifier;
```

## See Also

### Getting session information
- [var context: SRFaceMetrics.Context](./context-swift.property.md)
  The context of the system during the camera session.
- [SRFaceMetrics.Context](./context-swift.struct.md)
  The context of the system during the camera session.
- [var version: String](./version.md)
  The version of the algorithm that the system uses to generate the face metrics and analytics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfacemetrics/sessionidentifier)*