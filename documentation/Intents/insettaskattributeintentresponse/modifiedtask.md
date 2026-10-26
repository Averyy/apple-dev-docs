# modifiedTask

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The modified task.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
@NSCopying
var modifiedTask: INTask? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INTask * modifiedTask;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INTask * modifiedTask;
```

#### Discussion

Use this property to specify the details of the task. Start with the original task details and apply any attribute changes made at the request of the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintentresponse/modifiedtask)*