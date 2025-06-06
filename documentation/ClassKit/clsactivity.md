# CLSActivity

**Framework**: ClassKit  
**Kind**: class

A representation of user interaction with a context.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CLSActivity
```

## Mentions

- [Recording student progress](recording-student-progress.md)

#### Overview

An activity represents a student’s attempt to complete the task corresponding to a [`CLSContext`](clscontext.md) instance. For example, if a context represents a quiz, the associated activity represents the student’s attempt to take the quiz. As such, an activity is always associated with a context. In fact, you never initialize an activity in isolation or store a reference to it. Rather, you ask a context to create the activity and retrieve it from the context.

##### Starting and Stopping Activities

You start the activity with a call to the [`start()`](clsactivity/start().md) method when the user begins the task, and stop it with a call to the [`stop()`](clsactivity/stop().md) method when the user finishes. You can also use the [`stop()`](clsactivity/stop().md) method to stop it temporarily if the user pauses the task, in which case you can start it again later with another call to [`start()`](clsactivity/start().md) when the user resumes. The activity keeps track of the total time spent in the running state, which you can read via the [`duration`](clsactivity/duration.md) property.

Whether you implement activity pausing depends on how the parts of your app work. For example, you might pause a game activity when the user presses the pause button to reflect that the user has stepped away from the activity, but is likely to return soon to complete the task. On the other hand, you might not provide a way to pause a quiz activity because you require that it be completed without interruption, once started. If you do pause, you can start and stop an activity as many times as you want, but when you create a new activity (representing a new attempt at a task), you can no longer access the older activity from your app.

##### Recording Progress

You can also assign [`progress`](clsactivity/progress.md) to an activity. How you define progress depends on the task being measured. For example, progress through a quiz can be recorded as the fraction of questions answered, while progress through a game level might be calculated as the fraction of obstacles overcome.

To record additional metrics, you attach [`CLSActivityItem`](clsactivityitem.md) instances to an activity. For example, you can add both a score and a count of hints used to a quiz activity. If one of these items should be featured prominently, you can make it the [`primaryActivityItem`](clsactivity/primaryactivityitem.md).

## Topics

### Starting and stopping an activity
- [func start()](clsactivity/start.md)
  Tells an activity to start recording duration and progress for a task.
- [func stop()](clsactivity/stop.md)
  Tells an activity to stop or pause recording duration and progress for a task.
- [var isStarted: Bool](clsactivity/isstarted.md)
  A Boolean that indicates whether an activity is running.
- [var duration: TimeInterval](clsactivity/duration.md)
  The cumulative time in seconds that an activity has been active.
### Measuring progress
- [var progress: Double](clsactivity/progress.md)
  A measure of progress through the task, given as a fraction in the range [0, 1].
- [func addProgressRange(fromStart: Double, toEnd: Double)](clsactivity/addprogressrange(fromstart:toend:).md)
  Adds a progress range to a given activity.
### Managing activity items
- [func addAdditionalActivityItem(CLSActivityItem)](clsactivity/addadditionalactivityitem(_:).md)
  Adds an activity item to an activity.
- [var primaryActivityItem: CLSActivityItem?](clsactivity/primaryactivityitem.md)
  Adds an activity item to an activity and sets it as the primary activity item.
- [var additionalActivityItems: [CLSActivityItem]](clsactivity/additionalactivityitems.md)
  The list of activity items associated with an activity.
- [func removeAllActivityItems()](clsactivity/removeallactivityitems.md)
  Deletes all activity items associated with the current activity.

## Relationships

### Inherits From
- [CLSObject](clsobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Recording student progress](recording-student-progress.md)
  Create an activity to record student progress through an assignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsactivity)*