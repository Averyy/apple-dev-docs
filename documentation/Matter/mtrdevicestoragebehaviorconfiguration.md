# MTRDeviceStorageBehaviorConfiguration

**Framework**: Matter  
**Kind**: class

Class that configures how MTRDevice objects persist their attributes to storage, so as to not overwhelm the underlying storage system.

**Availability**:
- iOS 17.6+
- iPadOS 17.6+
- Mac Catalyst 17.6+
- macOS 14.6+
- tvOS 17.6+
- visionOS 1.0+
- watchOS 10.6+

## Declaration

```swift
class MTRDeviceStorageBehaviorConfiguration
```

## Topics

### Initializers
- [convenience init(reportToPersistenceDelayTime: TimeInterval, reportToPersistenceDelayTimeMax: TimeInterval, recentReportTimesMaxCount: Int, timeBetweenReportsTooShortThreshold: TimeInterval, timeBetweenReportsTooShortMinThreshold: TimeInterval, reportToPersistenceDelayMaxMultiplier: Double, deviceReportingExcessivelyIntervalThreshold: TimeInterval)](mtrdevicestoragebehaviorconfiguration/init(reporttopersistencedelaytime:reporttopersistencedelaytimemax:recentreporttimesmaxcount:timebetweenreportstooshortthreshold:timebetweenreportstooshortminthreshold:reporttopersistencedelaymaxmultiplier:devicereportingexcessivelyintervalt-6xgqf.md)
  Create configuration with specified values. See description below for details, and the list of properties below for valid ranges of these values.
### Instance Properties
- [var deviceReportingExcessivelyIntervalThreshold: TimeInterval](mtrdevicestoragebehaviorconfiguration/devicereportingexcessivelyintervalthreshold.md)
- [var disableStorageBehaviorOptimization: Bool](mtrdevicestoragebehaviorconfiguration/disablestoragebehavioroptimization.md)
  If disableStorageBehaviorOptimization is set to YES, then all the waiting mechanism as described above is disabled.
- [var recentReportTimesMaxCount: Int](mtrdevicestoragebehaviorconfiguration/recentreporttimesmaxcount.md)
- [var reportToPersistenceDelayMaxMultiplier: Double](mtrdevicestoragebehaviorconfiguration/reporttopersistencedelaymaxmultiplier.md)
- [var reportToPersistenceDelayTime: TimeInterval](mtrdevicestoragebehaviorconfiguration/reporttopersistencedelaytime.md)
  If any of these properties are set to be out of the documented limits, these default values will be used to replace all of them:
- [var reportToPersistenceDelayTimeMax: TimeInterval](mtrdevicestoragebehaviorconfiguration/reporttopersistencedelaytimemax.md)
- [var timeBetweenReportsTooShortMinThreshold: TimeInterval](mtrdevicestoragebehaviorconfiguration/timebetweenreportstooshortminthreshold.md)
- [var timeBetweenReportsTooShortThreshold: TimeInterval](mtrdevicestoragebehaviorconfiguration/timebetweenreportstooshortthreshold.md)
### Type Methods
- [class func withDefaultStorageBehavior() -> Self](mtrdevicestoragebehaviorconfiguration/withdefaultstoragebehavior.md)
  Create configuration with a default set of values. See description below for details.
- [class func withStorageBehaviorOptimizationDisabled() -> Self](mtrdevicestoragebehaviorconfiguration/withstoragebehavioroptimizationdisabled.md)
  Create configuration that disables storage behavior optimizations.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrdevicestoragebehaviorconfiguration)*