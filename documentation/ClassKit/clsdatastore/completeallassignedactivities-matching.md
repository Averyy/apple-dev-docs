# completeAllAssignedActivities(matching:)

**Framework**: ClassKit  
**Kind**: method

Marks all of the assigned and active activities for the given context path as complete.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func completeAllAssignedActivities(matching contextPath: [String])
```

## Mentions

- [Recording student progress](recording-student-progress.md)

#### Discussion

Schoolwork displays a per-student Done indicator to teachers, along with statistics about task completion for the entire class. Students set this indicator in their own view of the Schoolwork app. Use the [`completeAllAssignedActivities(matching:)`](clsdatastore/completeallassignedactivities(matching:).md) method to set the Done status programmatically.

Because you’re taking an action on behalf of the student when you call this method, Schoolwork shows the student a momentary alert in your app’s interface at that time.

Call this method only when you know that the task is complete and the student can’t or won’t work it any further because the task’s allotted time elapsed or because the student submitted all the required information to the teacher. Alternatively, if you already have a submit button in your interface, you can call this method from that button’s handler.

If a teacher reassigns content and the student marks the item done without redoing the activity, ClassKit reports the previously recorded metrics for that assignment to the teacher.

## Parameters

- `contextPath`: An array of strings that trace a path of identifiers from   to a target context with activities you want to mark as complete. The   is the same identifier path you use for a call to the   method, but affects only the last context in the path.

## See Also

- [var mainAppContext: CLSContext](clsdatastore/mainappcontext.md)
  The app’s top-level context.
- [var activeContext: CLSContext?](clsdatastore/activecontext.md)
  The currently active context.
- [var runningActivity: CLSActivity?](clsdatastore/runningactivity.md)
  The currently running activity within the currently active context.
- [func fetchActivity(for: URL, completion: (CLSActivity?, (any Error)?) -> Void)](clsdatastore/fetchactivity(for:completion:).md)
  Fetches an activity for a given document so you can record progress on the associated task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsdatastore/completeallassignedactivities(matching:))*