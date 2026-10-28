# init(targetTask:taskTitle:status:priority:spatialEventTrigger:temporalEventTrigger:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with information about the task and the changes that you want to make.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
init(targetTask: INTask?, taskTitle: INSpeakableString?, status: INTaskStatus, priority: INTaskPriority, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?)
```

```objc
- (instancetype) initWithTargetTask:(INTask *) targetTask taskTitle:(INSpeakableString *) taskTitle status:(INTaskStatus) status priority:(INTaskPriority) priority spatialEventTrigger:(INSpatialEventTrigger *) spatialEventTrigger temporalEventTrigger:(INTemporalEventTrigger *) temporalEventTrigger;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you do not create instances of this class yourself. Instead, SiriKit creates instances when the user asks to set the attributes of a task. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `targetTask`: The task that you want to modify.
- `taskTitle`: The title for the task.
- `status`: The new status for the task.
- `priority`: The priority for the task.
- `spatialEventTrigger`: The location-based trigger, if any, that you want to apply to the task.
- `temporalEventTrigger`: The time-based trigger, if any, that you want to apply to the task.

## See Also

### Initializing the Intent Object
- [convenience init(targetTask: INTask?, status: INTaskStatus, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?)](./init%28targettask,status,spatialeventtrigger,temporaleventtrigger%29.md)
  Initializes the intent object with information about the task and the changes that you want to make.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintent/init(targettask:tasktitle:status:priority:spatialeventtrigger:temporaleventtrigger:))*