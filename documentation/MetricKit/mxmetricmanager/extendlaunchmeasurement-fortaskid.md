# extendLaunchMeasurement(forTaskID:)

**Framework**: MetricKit  
**Kind**: method

Starts to measure an extended launch task with the given task identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func extendLaunchMeasurement(forTaskID taskID: MXLaunchTaskID) throws
```

#### Discussion

Use this method on the main thread to measure an extended launch task. Your app needs to start the first task before or during [`scene(_:restoreInteractionStateWith:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/scene(_:restoreInteractionStateWith:)), or before the system calls [`sceneDidBecomeActive(_:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/sceneDidBecomeActive(_:)) on the first scene to connect, and each task needs to overlap with others.

The maximum number of tasks is 16. The extended launch measurement finishes when all running tasks finish.

## Parameters

- `taskID`: The task identifier. Must be a unique,   string.

## See Also

- [class func finishExtendedLaunchMeasurement(forTaskID: MXLaunchTaskID) throws](mxmetricmanager/finishextendedlaunchmeasurement(fortaskid:).md)
  Signals the end of an extended launch task.
- [struct MXLaunchTaskID](mxlaunchtaskid.md)
  The task identifier to track launch measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager/extendlaunchmeasurement(fortaskid:))*