# INSearchForNotebookItemsIntentResponseCode

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

> **Deprecated**: INSearchForNotebookItemsIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
enum INSearchForNotebookItemsIntentResponseCode
```

```c
enum INSearchForNotebookItemsIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INSearchForNotebookItemsIntentResponseCode.unspecified](./insearchfornotebookitemsintentresponsecode/unspecified.md)
  The response didn’t specify a response code.
- [INSearchForNotebookItemsIntentResponseCode.ready](./insearchfornotebookitemsintentresponsecode/ready.md)
  You are ready to handle the intent.
- [INSearchForNotebookItemsIntentResponseCode.inProgress](./insearchfornotebookitemsintentresponsecode/inprogress.md)
  You are in the process of searching for the results.
- [INSearchForNotebookItemsIntentResponseCode.success](./insearchfornotebookitemsintentresponsecode/success.md)
  You successfully performed the search.
- [INSearchForNotebookItemsIntentResponseCode.failure](./insearchfornotebookitemsintentresponsecode/failure.md)
  You were unable to perform the search.
- [INSearchForNotebookItemsIntentResponseCode.failureRequiringAppLaunch](./insearchfornotebookitemsintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to perform the search and view the results.
### Initializers
- [init?(rawValue: Int)](./insearchfornotebookitemsintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INSearchForNotebookItemsIntentResponseCode](./insearchfornotebookitemsintentresponse/code.md)
  The code indicating whether your app successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintentresponsecode)*