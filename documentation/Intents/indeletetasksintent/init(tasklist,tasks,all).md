# init(taskList:tasks:all:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates the intent object with information about the task list and the tasks to delete from it.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.0+ - Deprecated in 15.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@nonobjc
convenience init(taskList: INTaskList? = nil, tasks: [INTask]? = nil, all: Bool? = nil)
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Typically, you don’t create instances of this class yourself. Instead, SiriKit creates instances when the user asks to set the attributes of a task. However, you can use this method during testing to create intent objects that validate your intent handling code paths.

## Parameters

- `taskList`: The task list from which to delete tasks.
- `tasks`: An array of tasks to delete.
- `all`: A Boolean value that indicates whether to delete all of the tasks in the task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetasksintent/init(tasklist:tasks:all:))*