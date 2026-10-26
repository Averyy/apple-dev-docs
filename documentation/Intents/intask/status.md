# status

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The current completion state of the task.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTask is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var status: INTaskStatus { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INTaskStatus status;
```

*macOS*

```objc
@property (atomic, assign, readonly) INTaskStatus status;
```

## See Also

### Getting the Task Completion Status
- [enum INTaskStatus](../intaskstatus.md)
  Constants indicating the completion state of a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intask/status)*