# activeContext

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, strong, readonly, nullable) CLSContext * activeContext;
```

## Discussion

This value is `nil` if there is no currently active context.

To activate a context when a student begins working on the content that the context represents, call its [`becomeActive()`](../clscontext/becomeactive%28%29.md) method. To deactivate a context when the student finishes, call its [`resignActive()`](../clscontext/resignactive%28%29.md) function. Only one context may be active at a time. If you activate a context, the system automatically causes any previously active context to resign.

## See Also

### Accessing specific contexts and activities
- [var mainAppContext: CLSContext](./mainappcontext.md)
  The app’s top-level context.
- [var runningActivity: CLSActivity?](./runningactivity.md)
  The currently running activity within the currently active context.
- [func fetchActivity(for: URL, completion: (CLSActivity?, (any Error)?) -> Void)](./fetchactivity%28for,completion%29.md)
  Fetches an activity for a given document so you can record progress on the associated task.
- [func completeAllAssignedActivities(matching: [String])](./completeallassignedactivities%28matching%29.md)
  Marks all of the assigned and active activities for the given context path as complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsdatastore/activecontext)*