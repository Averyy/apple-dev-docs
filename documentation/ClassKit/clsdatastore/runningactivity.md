# runningActivity

**Framework**: ClassKit  
**Kind**: property

The currently running activity within the currently active context.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var runningActivity: CLSActivity? { get }
```

## Mentions

- [Recording student progress](recording-student-progress.md)

#### Discussion

This value is `nil` if there is no currently running activity.

If your deployment target is iOS 11.4 or later, you can have more than one activity running concurrently. When you do this, the [`runningActivity`](clsdatastore/runningactivity.md) property holds the most recently started activity.

## See Also

- [var mainAppContext: CLSContext](clsdatastore/mainappcontext.md)
  The app’s top-level context.
- [var activeContext: CLSContext?](clsdatastore/activecontext.md)
  The currently active context.
- [func fetchActivity(for: URL, completion: (CLSActivity?, (any Error)?) -> Void)](clsdatastore/fetchactivity(for:completion:).md)
  Fetches an activity for a given document so you can record progress on the associated task.
- [func completeAllAssignedActivities(matching: [String])](clsdatastore/completeallassignedactivities(matching:).md)
  Marks all of the assigned and active activities for the given context path as complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsdatastore/runningactivity)*