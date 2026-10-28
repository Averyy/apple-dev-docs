# INTask

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An individual task the user needs to complete.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTask is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INTask
```

```objc
@interface INTask : NSObject
```

## Overview

Use task objects to represent tasks for the user to complete. Each task object contains a description of the task, its current completion state, and any trigger conditions to remind the user to complete the task.

## Topics

### Initializing a Task Object
- [init(title: INSpeakableString, status: INTaskStatus, taskType: INTaskType, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?, createdDateComponents: DateComponents?, modifiedDateComponents: DateComponents?, identifier: String?, priority: INTaskPriority)](./intask/init%28title,status,tasktype,spatialeventtrigger,temporaleventtrigger,createddatecomponents,modifieddatecomponents,identifier,priority%29.md)
  Initializes a task object with the specified content and triggers.
- [convenience init(title: INSpeakableString, status: INTaskStatus, taskType: INTaskType, spatialEventTrigger: INSpatialEventTrigger?, temporalEventTrigger: INTemporalEventTrigger?, createdDateComponents: DateComponents?, modifiedDateComponents: DateComponents?, identifier: String?)](./intask/init%28title,status,tasktype,spatialeventtrigger,temporaleventtrigger,createddatecomponents,modifieddatecomponents,identifier%29.md)
  Initializes a task object with the specified content and triggers.
### Getting the Task Content
- [var title: INSpeakableString](./intask/title.md)
  The text that describes the task.
### Getting the Task Completion Status
- [var status: INTaskStatus](./intask/status.md)
  The current completion state of the task.
- [enum INTaskStatus](./intaskstatus.md)
  Constants indicating the completion state of a task.
### Getting the Event Triggers
- [var temporalEventTrigger: INTemporalEventTrigger?](./intask/temporaleventtrigger.md)
  A time-based trigger that reminds the user to complete the task.
- [var spatialEventTrigger: INSpatialEventTrigger?](./intask/spatialeventtrigger.md)
  A location-based trigger that reminds the user to complete the task.
### Getting the Modification Dates
- [var createdDateComponents: DateComponents?](./intask/createddatecomponents.md)
  The initial creation date of the task.
- [var modifiedDateComponents: DateComponents?](./intask/modifieddatecomponents.md)
  The date on which the intent updated the task.
### Getting the Task Type
- [var taskType: INTaskType](./intask/tasktype.md)
  Information about the behavior of the task in your app.
- [enum INTaskType](./intasktype.md)
  Constants indicating how the task behaves.
### Identifying the Task
- [var identifier: String?](./intask/identifier.md)
  The unique identifier that your app uses to identify the task.
### Identifying the Task Priority
- [var priority: INTaskPriority](./intask/priority.md)
  The priority for the task.
### Initializers
- [init?(coder: NSCoder)](./intask/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Task Objects
- [class INTaskList](./intasklist.md)
  A collection of individual tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intask)*