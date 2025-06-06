# currentActivity

**Framework**: ClassKit  
**Kind**: property

The activity available for recording progress.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var currentActivity: CLSActivity? { get }
```

## Mentions

- [Recording student progress](recording-student-progress.md)

#### Discussion

You add an activity to a context by calling the [`createNewActivity()`](clscontext/createnewactivity().md) method when the user makes a new attempt at a task. You then use the context’s [`currentActivity`](clscontext/currentactivity.md) property to access the newly created activity. If the context has an existing activity from a previous attempt, it ceases to be available to your app as a result of creating a new one. However, the network still retains its data for reporting purposes.

Don’t store a reference to the current activity. Always use the [`currentActivity`](clscontext/currentactivity.md) property to get it. The object returned to you might change from time to time because of network synchronization, even when the underlying task is the same.

## See Also

- [func createNewActivity() -> CLSActivity](clscontext/createnewactivity.md)
  Creates and returns a new activity instance for the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/currentactivity)*