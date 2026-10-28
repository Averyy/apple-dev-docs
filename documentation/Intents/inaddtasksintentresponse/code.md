# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code indicating whether you successfully handled the intent.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var code: INAddTasksIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INAddTasksIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INAddTasksIntentResponseCode code;
```

## Discussion

The value of this property is set automatically at initialization time and can’t be changed later.

## See Also

### Getting the Response Code
- [enum INAddTasksIntentResponseCode](../inaddtasksintentresponsecode.md)
  Constants indicating the state of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintentresponse/code)*