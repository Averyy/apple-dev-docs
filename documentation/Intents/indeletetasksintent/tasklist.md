# taskList

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The task list from which to delete tasks.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@NSCopying
var taskList: INTaskList? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INTaskList * taskList;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INTaskList * taskList;
```

## See Also

### Getting the Task Information
- [var tasks: [INTask]?](./tasks.md)
  The tasks to delete from a task list.
- [var all: Bool?](./all-8gg59.md)
  A Boolean value that indicates whether to delete all the tasks from a task list.
- [all](./all-1dt4g.md)
  A Boolean value that indicates whether to delete all the tasks from a task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetasksintent/tasklist)*