# INSearchForNotebookItemsIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You successfully performed the search.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case success
```

```c
INSearchForNotebookItemsIntentResponseCodeSuccess
```

#### Discussion

Use this code after performing the search. Put the results of the search in your response object.

## See Also

### Constants
- [INSearchForNotebookItemsIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INSearchForNotebookItemsIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INSearchForNotebookItemsIntentResponseCode.inProgress](./inprogress.md)
  You are in the process of searching for the results.
- [INSearchForNotebookItemsIntentResponseCode.failure](./failure.md)
  You were unable to perform the search.
- [INSearchForNotebookItemsIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to perform the search and view the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintentresponsecode/success)*