# INSearchForNotebookItemsIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app to perform the search and view the results.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INSearchForNotebookItemsIntentResponseCodeFailureRequiringAppLaunch
```

#### Discussion

Use this response code when you cannot perform the search from your Intents extension but can do so from your app. Do not use this code for general errors or to force the user to launch your app.

## See Also

### Constants
- [INSearchForNotebookItemsIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INSearchForNotebookItemsIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INSearchForNotebookItemsIntentResponseCode.inProgress](./inprogress.md)
  You are in the process of searching for the results.
- [INSearchForNotebookItemsIntentResponseCode.success](./success.md)
  You successfully performed the search.
- [INSearchForNotebookItemsIntentResponseCode.failure](./failure.md)
  You were unable to perform the search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintentresponsecode/failurerequiringapplaunch)*