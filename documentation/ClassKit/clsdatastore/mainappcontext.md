# mainAppContext

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

The app’s top-level context.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var mainAppContext: CLSContext { get }
```

```objc
@property (nonatomic, strong, readonly) CLSContext * mainAppContext;
```

#### Discussion

Every app has exactly one top-level context that acts as the root node in a hierarchy of contexts that you define. Its identifier is the app’s bundle identifier. You can neither create nor destroy this context.

## See Also

### Accessing specific contexts and activities
- [var activeContext: CLSContext?](./activecontext.md)
  The currently active context.
- [var runningActivity: CLSActivity?](./runningactivity.md)
  The currently running activity within the currently active context.
- [func fetchActivity(for: URL, completion: (CLSActivity?, (any Error)?) -> Void)](./fetchactivity%28for,completion%29.md)
  Fetches an activity for a given document so you can record progress on the associated task.
- [func completeAllAssignedActivities(matching: [String])](./completeallassignedactivities%28matching%29.md)
  Marks all of the assigned and active activities for the given context path as complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsdatastore/mainappcontext)*