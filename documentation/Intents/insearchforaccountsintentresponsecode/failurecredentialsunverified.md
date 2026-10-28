# INSearchForAccountsIntentResponseCode.failureCredentialsUnverified

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You were unable to perform the search because you could not verify the user’s credentials.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case failureCredentialsUnverified
```

```c
INSearchForAccountsIntentResponseCodeFailureCredentialsUnverified
```

## Discussion

Use this response code when you are unable to verify the credentials of the current user. You might use this response code if the user is currently logged out of your app or is unknown to you. You might also use it if the user does not have any configured accounts.

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
- [INSearchForAccountsIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to perform the search.
- [INSearchForAccountsIntentResponseCode.failureAccountNotFound](./failureaccountnotfound.md)
  The search yielded no results.
- [INSearchForAccountsIntentResponseCode.failureTermsAndConditionsAcceptanceRequired](./failuretermsandconditionsacceptancerequired.md)
  The search failed as the user must accept the terms and conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintentresponsecode/failurecredentialsunverified)*