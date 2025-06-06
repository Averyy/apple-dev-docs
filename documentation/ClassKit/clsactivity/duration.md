# duration

**Framework**: ClassKit  
**Kind**: property

The cumulative time in seconds that an activity has been active.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var duration: TimeInterval { get }
```

#### Discussion

When you create a new activity to represent a new attempt at a task by calling the [`createNewActivity()`](clscontext/createnewactivity().md) method, the duration initializes to zero. After you call the [`start()`](clsactivity/start().md) method, it begins counting seconds. When you call the [`stop()`](clsactivity/stop().md) method, the duration counter stops. It resumes counting (without resetting) if you make a new call to the [`start()`](clsactivity/start().md) method, enabling you to effectively pause an activity. But once you create a new activity, the duration on the old one stops permanently, and is no longer accessible to your app.

## See Also

- [func start()](clsactivity/start.md)
  Tells an activity to start recording duration and progress for a task.
- [func stop()](clsactivity/stop.md)
  Tells an activity to stop or pause recording duration and progress for a task.
- [var isStarted: Bool](clsactivity/isstarted.md)
  A Boolean that indicates whether an activity is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsactivity/duration)*