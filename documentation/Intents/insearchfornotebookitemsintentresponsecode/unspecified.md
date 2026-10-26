# INSearchForNotebookItemsIntentResponseCode.unspecified

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The response didn’t specify a response code.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case unspecified
```

```c
INSearchForNotebookItemsIntentResponseCodeUnspecified
```

#### Discussion

Don’t return this response code when handling the intent; doing so causes the device to display an error.

## See Also

### Constants
- [INSearchForNotebookItemsIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INSearchForNotebookItemsIntentResponseCode.inProgress](./inprogress.md)
  You are in the process of searching for the results.
- [INSearchForNotebookItemsIntentResponseCode.success](./success.md)
  You successfully performed the search.
- [INSearchForNotebookItemsIntentResponseCode.failure](./failure.md)
  You were unable to perform the search.
- [INSearchForNotebookItemsIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to perform the search and view the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintentresponsecode/unspecified)*