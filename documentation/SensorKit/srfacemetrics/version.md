# version

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The version of the algorithm that the system uses to generate the face metrics and analytics.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var version: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * version;
```

## See Also

### Getting session information
- [var sessionIdentifier: String](./sessionidentifier.md)
  An identifier for the camera session.
- [var context: SRFaceMetrics.Context](./context-swift.property.md)
  The context of the system during the camera session.
- [SRFaceMetrics.Context](./context-swift.struct.md)
  The context of the system during the camera session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfacemetrics/version)*