# MXLaunchTaskID

**Framework**: MetricKit  
**Kind**: struct

The task identifier to track launch measurements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct MXLaunchTaskID
```

## Topics

### Creating a task identifier
- [init(String)](mxlaunchtaskid/init(_:).md)
  Creates a task identifer from a string.
- [init(rawValue: String)](mxlaunchtaskid/init(rawvalue:).md)
  Creates a task identifer from a string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class func extendLaunchMeasurement(forTaskID: MXLaunchTaskID) throws](mxmetricmanager/extendlaunchmeasurement(fortaskid:).md)
  Starts to measure an extended launch task with the given task identifier.
- [class func finishExtendedLaunchMeasurement(forTaskID: MXLaunchTaskID) throws](mxmetricmanager/finishextendedlaunchmeasurement(fortaskid:).md)
  Signals the end of an extended launch task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxlaunchtaskid)*