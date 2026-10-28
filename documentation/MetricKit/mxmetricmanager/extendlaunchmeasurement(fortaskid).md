# extendLaunchMeasurement(forTaskID:)

**Framework**: MetricKit  
**Kind**: method  
**Role**: Type Method

Starts to measure an extended launch task with the given task identifier.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.0
- macOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`trackLaunchTask(id:onTrackingError:_:)`](../metricmanager/tracklaunchtask%28id,ontrackingerror,_%29-48k2s.md) or [`trackLaunchTask(id:onTrackingError:_:)`](../metricmanager/tracklaunchtask%28id,ontrackingerror,_%29-jnu1.md) instead.

## Declaration

```swift
class func extendLaunchMeasurement(forTaskID taskID: MXLaunchTaskID) throws
```

```objc
+ (BOOL) extendLaunchMeasurementForTaskID:(MXLaunchTaskID) taskID error:(NSError **) error;
```

## Discussion

Use this method on the main thread to measure an extended launch task. Your app needs to start the first task before or during [`scene(_:restoreInteractionStateWith:)`](../../UIKit/uiscenedelegate/scene%28_,restoreinteractionstatewith%29.md), or before the system calls [`sceneDidBecomeActive(_:)`](../../UIKit/uiscenedelegate/scenedidbecomeactive%28_%29.md) on the first scene to connect, and each task needs to overlap with others.

The maximum number of tasks is 16. The extended launch measurement finishes when all running tasks finish.

## Parameters

- `taskID`: The task identifier. Must be a unique, `non-null` string.

## See Also

### Measuring an extended launch
- [class func finishExtendedLaunchMeasurement(forTaskID: MXLaunchTaskID) throws](./finishextendedlaunchmeasurement%28fortaskid%29.md)
  Signals the end of an extended launch task.
- [struct MXLaunchTaskID](../mxlaunchtaskid.md)
  The task identifier to track launch measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager/extendlaunchmeasurement(fortaskid:))*