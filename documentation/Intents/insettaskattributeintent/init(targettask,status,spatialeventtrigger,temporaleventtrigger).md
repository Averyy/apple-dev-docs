# init(targetTask:status:spatialEventTrigger:temporalEventTrigger:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with information about the task and the changes that you want to make.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 6.0

> **Deprecated**: Use the designated initializer instead

## Declaration

```swift
convenience init(targetTask: INTask?, status: INTaskStatus, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?)
```

```objc
- (instancetype) initWithTargetTask:(INTask *) targetTask status:(INTaskStatus) status spatialEventTrigger:(INSpatialEventTrigger *) spatialEventTrigger temporalEventTrigger:(INTemporalEventTrigger *) temporalEventTrigger;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you do not create instances of this class yourself. Instead, SiriKit creates instances when the user asks to set the attributes of a task. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `targetTask`: The task that you want to modify.
- `status`: The new status for the task.
- `spatialEventTrigger`: The location-based trigger, if any, that you want to apply to the task.
- `temporalEventTrigger`: The time-based trigger, if any, that you want to apply to the task.

## See Also

### Initializing the Intent Object
- [init(targetTask: INTask?, taskTitle: INSpeakableString?, status: INTaskStatus, priority: INTaskPriority, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?)](./init%28targettask,tasktitle,status,priority,spatialeventtrigger,temporaleventtrigger%29.md)
  Initializes the intent object with information about the task and the changes that you want to make.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintent/init(targettask:status:spatialeventtrigger:temporaleventtrigger:))*