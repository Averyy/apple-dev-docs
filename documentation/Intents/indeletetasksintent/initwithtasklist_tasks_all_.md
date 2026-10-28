# initWithTaskList:tasks:all:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Initializes the intent object with information about the task list and the tasks to delete from it.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```objc
- (instancetype) initWithTaskList:(INTaskList *) taskList tasks:(NSArray<INTask *> *) tasks all:(NSNumber *) all;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you don’t create instances of this class yourself. Instead, SiriKit creates instances when the user asks to set the attributes of a task. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `taskList`: The task list to delete tasks from.
- `tasks`: An array of tasks to delete.
- `all`: A Boolean value indicating whether to delete all of the tasks in the task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetasksintent/initwithtasklist:tasks:all:)*