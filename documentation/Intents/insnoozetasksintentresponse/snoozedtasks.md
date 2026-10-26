# snoozedTasks

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

> **Deprecated**: INSnoozeTasksIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var snoozedTasks: [INTask]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<INTask *> * snoozedTasks;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<INTask *> * snoozedTasks;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintentresponse/snoozedtasks)*