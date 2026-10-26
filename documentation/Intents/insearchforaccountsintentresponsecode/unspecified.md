# INSearchForAccountsIntentResponseCode.unspecified

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The response didn’t specify a response code.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case unspecified
```

```c
INSearchForAccountsIntentResponseCodeUnspecified
```

#### Discussion

Don’t return this response code when handling the intent; doing so causes the device to display an error.

## See Also

### Constants
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
- [INSearchForAccountsIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to perform the search.
- [INSearchForAccountsIntentResponseCode.failureCredentialsUnverified](./failurecredentialsunverified.md)
  You were unable to perform the search because you could not verify the user’s credentials.
- [INSearchForAccountsIntentResponseCode.failureAccountNotFound](./failureaccountnotfound.md)
  The search yielded no results.
- [INSearchForAccountsIntentResponseCode.failureTermsAndConditionsAcceptanceRequired](./failuretermsandconditionsacceptancerequired.md)
  The search failed as the user must accept the terms and conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintentresponsecode/unspecified)*