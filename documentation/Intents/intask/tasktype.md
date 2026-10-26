# taskType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Information about the behavior of the task in your app.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTask is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var taskType: INTaskType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INTaskType taskType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INTaskType taskType;
```

## See Also

### Getting the Task Type
- [enum INTaskType](../intasktype.md)
  Constants indicating how the task behaves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intask/tasktype)*