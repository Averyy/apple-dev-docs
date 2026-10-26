# all

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to snooze all of the tasks.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * all;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * all;
```

## See Also

### Getting the Task Information
- [var nextTriggerTime: INDateComponentsRange?](./nexttriggertime.md)
  The next time after the current time that triggers a task to snooze.
- [var tasks: [INTask]?](./tasks.md)
  An array of tasks to snooze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintent/all-62ujw)*