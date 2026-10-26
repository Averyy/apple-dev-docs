# title

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The title text for the task list.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTaskList is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
@NSCopying
var title: INSpeakableString { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INSpeakableString * title;
```

*macOS*

```objc
@property (atomic, copy, readonly) INSpeakableString * title;
```

#### Discussion

The title text describes the purpose of the tasks.

## See Also

### Getting the Task Attributes
- [var tasks: [INTask]](./tasks.md)
  The array of individual tasks to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intasklist/title)*