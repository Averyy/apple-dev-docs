# initWithTasks:nextTriggerTime:all:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Initializes the intent object with information about the tasks to snooze and when to snooze them.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```objc
- (instancetype) initWithTasks:(NSArray<INTask *> *) tasks nextTriggerTime:(INDateComponentsRange *) nextTriggerTime all:(NSNumber *) all;
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you don’t create instances of this class yourself. Instead, SiriKit creates instances when the user asks to set the attributes of a task. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `tasks`: An array of tasks to snooze.
- `nextTriggerTime`: The next time to trigger a snooze.
- `all`: A Boolean value indicating whether to snooze all of the tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintent/initwithtasks:nexttriggertime:all:)*