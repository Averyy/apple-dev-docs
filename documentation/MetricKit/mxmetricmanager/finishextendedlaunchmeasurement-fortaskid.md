# finishExtendedLaunchMeasurement(forTaskID:)

**Framework**: MetricKit  
**Kind**: method

Signals the end of an extended launch task.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func finishExtendedLaunchMeasurement(forTaskID taskID: MXLaunchTaskID) throws
```

#### Discussion

Use this method on the main thread to end an extended launch task previously started with [`extendLaunchMeasurement(forTaskID:)`](mxmetricmanager/extendlaunchmeasurement(fortaskid:).md).

## Parameters

- `taskID`: The task identifier. Must be a unique,   string.

## See Also

- [class func extendLaunchMeasurement(forTaskID: MXLaunchTaskID) throws](mxmetricmanager/extendlaunchmeasurement(fortaskid:).md)
  Starts to measure an extended launch task with the given task identifier.
- [struct MXLaunchTaskID](mxlaunchtaskid.md)
  The task identifier to track launch measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager/finishextendedlaunchmeasurement(fortaskid:))*