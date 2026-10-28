# INSearchForAccountsIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app to perform the search.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INSearchForAccountsIntentResponseCodeFailureRequiringAppLaunch
```

## Discussion

Use this response code when you cannot perform the search from your Intents extension but can perform it from your app. Do not use this code for general errors or to force the user to launch your app.

## See Also

### Constants
- [INSearchForAccountsIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INSearchForAccountsIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INSearchForAccountsIntentResponseCode.inProgress](./inprogress.md)
  The search is still in progress.
- [INSearchForAccountsIntentResponseCode.success](./success.md)
  You successfully retrieved the search results.
- [INSearchForAccountsIntentResponseCode.failure](./failure.md)
  You were unable to retrieve the search results.
- [INSearchForAccountsIntentResponseCode.failureNotEligible](./failurenoteligible.md)
  The request failed because a user was not eligible to perform the transaction.
- [INSearchForAccountsIntentResponseCode.failureCredentialsUnverified](./failurecredentialsunverified.md)
  You were unable to perform the search because you could not verify the user’s credentials.
- [INSearchForAccountsIntentResponseCode.failureAccountNotFound](./failureaccountnotfound.md)
  The search yielded no results.
- [INSearchForAccountsIntentResponseCode.failureTermsAndConditionsAcceptanceRequired](./failuretermsandconditionsacceptancerequired.md)
  The search failed as the user must accept the terms and conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintentresponsecode/failurerequiringapplaunch)*