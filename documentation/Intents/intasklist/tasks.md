# tasks

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The array of individual tasks to perform.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTaskList is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var tasks: [INTask] { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSArray<INTask *> * tasks;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSArray<INTask *> * tasks;
```

## Discussion

A task list contains one or more [`INTask`](../intask.md) objects representing the individual tasks. Each task has its own descriptive information and trigger conditions.

## See Also

### Getting the Task Attributes
- [var title: INSpeakableString](./title.md)
  The title text for the task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intasklist/tasks)*