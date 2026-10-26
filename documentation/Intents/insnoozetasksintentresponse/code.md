# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code that indicates whether you successfully handled the intent.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INSnoozeTasksIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var code: INSnoozeTasksIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INSnoozeTasksIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INSnoozeTasksIntentResponseCode code;
```

#### Discussion

This property’s value is set automatically at initialization time and can’t be changed later.

## See Also

### Getting the Response Code
- [enum INSnoozeTasksIntentResponseCode](../insnoozetasksintentresponsecode.md)
  Constants that indicate the response state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintentresponse/code)*