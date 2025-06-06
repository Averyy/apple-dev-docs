# stop()

**Framework**: ClassKit  
**Kind**: method

Tells an activity to stop or pause recording duration and progress for a task.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func stop()
```

## Mentions

- [Recording student progress](recording-student-progress.md)
- [Recording additional metrics about a completed task](recording-additional-metrics-about-a-completed-task.md)

#### Discussion

If your app uses this method to pause recording, such as when the user taps the pause button in a game, you can resume later with another call to [`start()`](clsactivity/start().md) on the same activity when the user resumes the task associated with the activity. But if the user makes a new attempt at the task, for example by starting a game level over, and your app creates a new activity with a call to [`createNewActivity()`](clscontext/createnewactivity().md), then the framework stops the old one permanently and makes it inaccessible to your app thereafter.

## See Also

- [func start()](clsactivity/start.md)
  Tells an activity to start recording duration and progress for a task.
- [var isStarted: Bool](clsactivity/isstarted.md)
  A Boolean that indicates whether an activity is running.
- [var duration: TimeInterval](clsactivity/duration.md)
  The cumulative time in seconds that an activity has been active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsactivity/stop())*