# INSetTaskAttributeIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
enum INSetTaskAttributeIntentResponseCode
```

```c
enum INSetTaskAttributeIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INSetTaskAttributeIntentResponseCode.unspecified](./insettaskattributeintentresponsecode/unspecified.md)
  The response didn’t specify a response code.
- [INSetTaskAttributeIntentResponseCode.ready](./insettaskattributeintentresponsecode/ready.md)
  You are ready to handle the intent.
- [INSetTaskAttributeIntentResponseCode.inProgress](./insettaskattributeintentresponsecode/inprogress.md)
  The modification of the task list is still in progress.
- [INSetTaskAttributeIntentResponseCode.success](./insettaskattributeintentresponsecode/success.md)
  You successfully modified the task attributes.
- [INSetTaskAttributeIntentResponseCode.failure](./insettaskattributeintentresponsecode/failure.md)
  You were unable to modify the task attributes.
- [INSetTaskAttributeIntentResponseCode.failureRequiringAppLaunch](./insettaskattributeintentresponsecode/failurerequiringapplaunch.md)
  The user must modify tasks from within your app.
### Initializers
- [init?(rawValue: Int)](./insettaskattributeintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INSetTaskAttributeIntentResponseCode](./insettaskattributeintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintentresponsecode)*