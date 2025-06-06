# activeContext

**Framework**: ClassKit  
**Kind**: property

The currently active context.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var activeContext: CLSContext? { get }
```

#### Discussion

This value is `nil` if there is no currently active context.

To activate a context when a student begins working on the content that the context represents, call its [`becomeActive()`](clscontext/becomeactive().md) method. To deactivate a context when the student finishes, call its [`resignActive()`](clscontext/resignactive().md) function. Only one context may be active at a time, so if you activate a context, the system automatically causes any previously active context to resign.

## See Also

- [var mainAppContext: CLSContext](clsdatastore/mainappcontext.md)
  The app’s top-level context.
- [var runningActivity: CLSActivity?](clsdatastore/runningactivity.md)
  The currently running activity within the currently active context.
- [func fetchActivity(for: URL, completion: (CLSActivity?, (any Error)?) -> Void)](clsdatastore/fetchactivity(for:completion:).md)
  Fetches an activity for a given document so you can record progress on the associated task.
- [func completeAllAssignedActivities(matching: [String])](clsdatastore/completeallassignedactivities(matching:).md)
  Marks all of the assigned and active activities for the given context path as complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsdatastore/activecontext)*