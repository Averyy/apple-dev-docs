# init(title:status:taskType:spatialEventTrigger:temporalEventTrigger:createdDateComponents:modifiedDateComponents:identifier:priority:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a task object with the specified content and triggers.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
init(title: INSpeakableString, status: INTaskStatus, taskType: INTaskType, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?, createdDateComponents: DateComponents?, modifiedDateComponents: DateComponents?, identifier: String?, priority: INTaskPriority)
```

```objc
- (instancetype) initWithTitle:(INSpeakableString *) title status:(INTaskStatus) status taskType:(INTaskType) taskType spatialEventTrigger:(INSpatialEventTrigger *) spatialEventTrigger temporalEventTrigger:(INTemporalEventTrigger *) temporalEventTrigger createdDateComponents:(NSDateComponents *) createdDateComponents modifiedDateComponents:(NSDateComponents *) modifiedDateComponents identifier:(NSString *) identifier priority:(INTaskPriority) priority;
```

## Return Value

An initialized task object or `nil` if the object could not be created.

## Parameters

- `title`: The title text that describes the task. This string is what the user enters for the task details.
- `status`: The current state of the task. Tasks can be completed or not completed.
- `taskType`: Information about how the task behaves in your app. Use this parameter to specify whether the task can be marked as completed.
- `spatialEventTrigger`: A location-based trigger that reminds the user to complete the task.
- `temporalEventTrigger`: A time-based trigger that reminds the user to complete the task.
- `createdDateComponents`: The date on which the task was initially created.
- `modifiedDateComponents`: The last date on which the task was updated.
- `identifier`: The unique identifier that your app uses to identify the task.
- `priority`: The priority for the task.

## See Also

### Initializing a Task Object
- [convenience init(title: INSpeakableString, status: INTaskStatus, taskType: INTaskType, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?, createdDateComponents: DateComponents?, modifiedDateComponents: DateComponents?, identifier: String?)](./init%28title,status,tasktype,spatialeventtrigger,temporaleventtrigger,createddatecomponents,modifieddatecomponents,identifier%29.md)
  Initializes a task object with the specified content and triggers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intask/init(title:status:tasktype:spatialeventtrigger:temporaleventtrigger:createddatecomponents:modifieddatecomponents:identifier:priority:))*