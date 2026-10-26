# INTaskList

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A collection of individual tasks.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTaskList is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class INTaskList
```

```objc
@interface INTaskList : NSObject
```

#### Overview

A task list stores tasks related that are in some way related to each other. For example, a user might create a “party prep” task list that contains the individual tasks to perform to get ready for a party. The title of a task list describes its purpose, and individual tasks within the list have their own descriptions and completion states. Tasks can also have triggers to indicate when the user receives reminders to complete the task.

## Topics

### Initializing a Task List Object
- [init(title: INSpeakableString, tasks: [INTask], groupName: INSpeakableString?, createdDateComponents: DateComponents?, modifiedDateComponents: DateComponents?, identifier: String?)](./intasklist/init%28title,tasks,groupname,createddatecomponents,modifieddatecomponents,identifier%29.md)
  Initializes the task list object with the specified content.
### Getting the Task Attributes
- [var title: INSpeakableString](./intasklist/title.md)
  The title text for the task list.
- [var tasks: [INTask]](./intasklist/tasks.md)
  The array of individual tasks to perform.
### Getting the Group Name
- [var groupName: INSpeakableString?](./intasklist/groupname.md)
  The user-visible name of the group that contains the task list.
### Getting the Modification Dates
- [var createdDateComponents: DateComponents?](./intasklist/createddatecomponents.md)
  The creation date of the task list.
- [var modifiedDateComponents: DateComponents?](./intasklist/modifieddatecomponents.md)
  The date on which the intent most recently modified the task list.
### Identifying the Task List
- [var identifier: String?](./intasklist/identifier.md)
  The unique identifier that you use to identify the task list internally.
### Initializers
- [init?(coder: NSCoder)](./intasklist/init%28coder%29.md)

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
- [class INTask](./intask.md)
  An individual task the user needs to complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intasklist)*