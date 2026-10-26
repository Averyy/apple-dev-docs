# INTaskStatus

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the completion state of a task.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTaskStatus is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
enum INTaskStatus
```

```c
enum INTaskStatus : NSInteger;
```

## Topics

### Constants
- [INTaskStatus.unknown](./intaskstatus/unknown.md)
  A constant indicating to search for tasks whose status is unknown.
- [INTaskStatus.notCompleted](./intaskstatus/notcompleted.md)
  A constant indicating to search for tasks whose status is not complete.
- [INTaskStatus.completed](./intaskstatus/completed.md)
  A constant indicating to search for tasks whose status is complete.
### Initializers
- [init?(rawValue: Int)](./intaskstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Searching for Tasks by Their Status
- [var status: INTaskStatus](./insearchfornotebookitemsintent/status.md)
  The completion state to look for when searching for tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intaskstatus)*