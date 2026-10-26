# tasks

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of tasks to snooze.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INSnoozeTasksIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var tasks: [INTask]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INTask *> * tasks;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INTask *> * tasks;
```

## See Also

### Getting the Task Information
- [var nextTriggerTime: INDateComponentsRange?](./nexttriggertime.md)
  The next time after the current time that triggers a task to snooze.
- [var all: Bool?](./all-spsb.md)
  A Boolean value that indicates whether to snooze all of the tasks.
- [all](./all-62ujw.md)
  A Boolean value that indicates whether to snooze all of the tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintent/tasks)*