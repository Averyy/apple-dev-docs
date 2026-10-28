# INSearchForAccountsIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The search is still in progress.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case inProgress
```

```c
INSearchForAccountsIntentResponseCodeInProgress
```

## Discussion

Return this code if the search is running but you are unable to return the results after a few seconds of having your handler called. You might use this code when performing the search requires communicating with your server and you have not yet received a confirmation from that server.

When handling an intent, you might want to first configure a timer to fire if your server does not return within a few seconds. Use your timer’s handler block to provide the in-progress response back to Siri.

## See Also

### Constants
- [INSearchForAccountsIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INSearchForAccountsIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintentresponsecode/inprogress)*