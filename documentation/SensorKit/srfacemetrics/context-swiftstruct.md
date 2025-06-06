# SRFaceMetrics.Context

**Framework**: SensorKit  
**Kind**: struct

The context of the system during the camera session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct Context
```

## Topics

### Camera contexts
- [static var deviceUnlock: SRFaceMetrics.Context](srfacemetrics/context-swift.struct/deviceunlock.md)
  The camera session occurs while the user has the device unlocked.
- [static var messagingAppUsage: SRFaceMetrics.Context](srfacemetrics/context-swift.struct/messagingappusage.md)
  The camera session occurs while the user is in the app with messaging capability.
### Creating camera contexts
- [init(rawValue: UInt)](srfacemetrics/context-swift.struct/init(rawvalue:).md)
  Creates and returns a new structure with the specified value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var sessionIdentifier: String](srfacemetrics/sessionidentifier.md)
  An identifier for the camera session.
- [var context: SRFaceMetrics.Context](srfacemetrics/context-swift.property.md)
  The context of the system during the camera session.
- [var version: String](srfacemetrics/version.md)
  The version of the algorithm that the system uses to generate the face metrics and analytics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfacemetrics/context-swift.struct)*