# init(targetTaskList:taskTitles:spatialEventTrigger:temporalEventTrigger:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified task details.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 6.0

## Declaration

```swift
convenience init(targetTaskList: INTaskList?, taskTitles: [INSpeakableString]?, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?)
```

```objc
- (instancetype) initWithTargetTaskList:(INTaskList *) targetTaskList taskTitles:(NSArray<INSpeakableString *> *) taskTitles spatialEventTrigger:(INSpatialEventTrigger *) spatialEventTrigger temporalEventTrigger:(INTemporalEventTrigger *) temporalEventTrigger;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you do not create instances of this class yourself. Instead, SiriKit creates instances when the user asks to add tasks to a task list. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `targetTaskList`: The task list in which to create the new tasks.
- `taskTitles`: An array of strings, each of which represents a task to add to the task list.
- `spatialEventTrigger`: An [`INSpatialEventTrigger`](../inspatialeventtrigger.md) object that contains details of when reminders should be sent for the tasks. The trigger applies to all tasks being added.
- `temporalEventTrigger`: An [`INTemporalEventTrigger`](../intemporaleventtrigger.md) object that contains details of when reminders should be sent for the tasks. The trigger applies to all tasks being added.

## See Also

### Initializing the Intent Object
- [init(targetTaskList: INTaskList?, taskTitles: [INSpeakableString]?, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?, priority: INTaskPriority)](./init%28targettasklist,tasktitles,spatialeventtrigger,temporaleventtrigger,priority%29.md)
  Initializes the intent object with the specified task details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintent/init(targettasklist:tasktitles:spatialeventtrigger:temporaleventtrigger:))*