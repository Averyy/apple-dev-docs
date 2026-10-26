# init(title:tasks:groupName:createdDateComponents:modifiedDateComponents:identifier:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the task list object with the specified content.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTaskList is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
init(title: INSpeakableString, tasks: [INTask], groupName: INSpeakableString?, createdDateComponents: DateComponents?, modifiedDateComponents: DateComponents?, identifier: String?)
```

```objc
- (instancetype) initWithTitle:(INSpeakableString *) title tasks:(NSArray<INTask *> *) tasks groupName:(INSpeakableString *) groupName createdDateComponents:(NSDateComponents *) createdDateComponents modifiedDateComponents:(NSDateComponents *) modifiedDateComponents identifier:(NSString *) identifier;
```

#### Return Value

An initialized task list object or `nil` if the object could not be created.

## Parameters

- `title`: The title text that describes the task list.
- `tasks`: The tasks to include in the task list.
- `groupName`: The name of the group that contains the task list.
- `createdDateComponents`: The date on which the task was initially created.
- `modifiedDateComponents`: The last date on which the task was updated.
- `identifier`: The unique identifier that your app uses to identify the task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intasklist/init(title:tasks:groupname:createddatecomponents:modifieddatecomponents:identifier:))*