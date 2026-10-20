# SRFaceMetrics.Context

**Framework**: SensorKit  
**Kind**: struct  
**Role**: Structure

The context of the system during the camera session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct Context
```

```c
enum SRFaceMetricsContext : NSUInteger;
```

## Topics

### Camera contexts
- [static var deviceUnlock: SRFaceMetrics.Context](./context-swift.struct/deviceunlock.md)
  The camera session occurs while the user has the device unlocked.
- [static var messagingAppUsage: SRFaceMetrics.Context](./context-swift.struct/messagingappusage.md)
  The camera session occurs while the user is in the app with messaging capability.
### Creating camera contexts
- [init(rawValue: UInt)](./context-swift.struct/init%28rawvalue%29.md)
  Creates and returns a new structure with the specified value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Getting session information
- [var sessionIdentifier: String](./sessionidentifier.md)
  An identifier for the camera session.
- [var context: SRFaceMetrics.Context](./context-swift.property.md)
  The context of the system during the camera session.
- [var version: String](./version.md)
  The version of the algorithm that the system uses to generate the face metrics and analytics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfacemetrics/context-swift.struct)*