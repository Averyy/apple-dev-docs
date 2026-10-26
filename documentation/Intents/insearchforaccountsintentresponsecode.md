# INSearchForAccountsIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum INSearchForAccountsIntentResponseCode
```

```c
enum INSearchForAccountsIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INSearchForAccountsIntentResponseCode.unspecified](./insearchforaccountsintentresponsecode/unspecified.md)
  The response didn’t specify a response code.
- [INSearchForAccountsIntentResponseCode.ready](./insearchforaccountsintentresponsecode/ready.md)
  You are ready to handle the intent.
- [INSearchForAccountsIntentResponseCode.inProgress](./insearchforaccountsintentresponsecode/inprogress.md)
  The search is still in progress.
- [INSearchForAccountsIntentResponseCode.success](./insearchforaccountsintentresponsecode/success.md)
  You successfully retrieved the search results.
- [INSearchForAccountsIntentResponseCode.failure](./insearchforaccountsintentresponsecode/failure.md)
  You were unable to retrieve the search results.
- [INSearchForAccountsIntentResponseCode.failureNotEligible](./insearchforaccountsintentresponsecode/failurenoteligible.md)
  The request failed because a user was not eligible to perform the transaction.
- [INSearchForAccountsIntentResponseCode.failureRequiringAppLaunch](./insearchforaccountsintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to perform the search.
- [INSearchForAccountsIntentResponseCode.failureCredentialsUnverified](./insearchforaccountsintentresponsecode/failurecredentialsunverified.md)
  You were unable to perform the search because you could not verify the user’s credentials.
- [INSearchForAccountsIntentResponseCode.failureAccountNotFound](./insearchforaccountsintentresponsecode/failureaccountnotfound.md)
  The search yielded no results.
- [INSearchForAccountsIntentResponseCode.failureTermsAndConditionsAcceptanceRequired](./insearchforaccountsintentresponsecode/failuretermsandconditionsacceptancerequired.md)
  The search failed as the user must accept the terms and conditions.
### Initializers
- [init?(rawValue: Int)](./insearchforaccountsintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INSearchForAccountsIntentResponseCode](./insearchforaccountsintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintentresponsecode)*