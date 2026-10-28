# finishExtendedLaunchMeasurement(forTaskID:)

**Framework**: MetricKit  
**Kind**: method  
**Role**: Type Method

Signals the end of an extended launch task.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.0
- macOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`trackLaunchTask(id:onTrackingError:_:)`](../metricmanager/tracklaunchtask%28id,ontrackingerror,_%29-48k2s.md) or [`trackLaunchTask(id:onTrackingError:_:)`](../metricmanager/tracklaunchtask%28id,ontrackingerror,_%29-jnu1.md) instead.

## Declaration

```swift
class func finishExtendedLaunchMeasurement(forTaskID taskID: MXLaunchTaskID) throws
```

```objc
+ (BOOL) finishExtendedLaunchMeasurementForTaskID:(MXLaunchTaskID) taskID error:(NSError **) error;
```

## Discussion

Use this method on the main thread to end an extended launch task previously started with [`extendLaunchMeasurement(forTaskID:)`](./extendlaunchmeasurement%28fortaskid%29.md).

## Parameters

- `taskID`: The task identifier. Must be a unique, `non-null` string.

## See Also

### Measuring an extended launch
- [class func extendLaunchMeasurement(forTaskID: MXLaunchTaskID) throws](./extendlaunchmeasurement%28fortaskid%29.md)
  Starts to measure an extended launch task with the given task identifier.
- [struct MXLaunchTaskID](../mxlaunchtaskid.md)
  The task identifier to track launch measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager/finishextendedlaunchmeasurement(fortaskid:))*