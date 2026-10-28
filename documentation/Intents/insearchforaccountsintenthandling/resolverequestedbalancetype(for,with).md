# resolveRequestedBalanceType(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the balance type to look for in a search.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func resolveRequestedBalanceType(for intent: INSearchForAccountsIntent, with completion: @escaping @Sendable (INBalanceTypeResolutionResult) -> Void)
```

```swift
optional func resolveRequestedBalanceType(for intent: INSearchForAccountsIntent) async -> INBalanceTypeResolutionResult
```

```objc
- (void) resolveRequestedBalanceTypeForSearchForAccounts:(INSearchForAccountsIntent *) intent withCompletion:(void (^)(INBalanceTypeResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve any questions about the balance type to look for in a search. Use this method to examine the [`requestedBalanceType`](../insearchforaccountsintent/requestedbalancetype.md) property of the `intent` object. Return a successful resolution if you can retrieve the specified balance information from the user’s account as part of your search. If you do not support the specified balance type, return a different balance type and ask for confirmation.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

## See Also

### Resolving the Intent Parameters
- [func resolveAccountNickname(for: INSearchForAccountsIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolveaccountnickname%28for,with%29.md)
  Resolves the account nickname to use during a search.
- [func resolveAccountType(for: INSearchForAccountsIntent, with: (INAccountTypeResolutionResult) -> Void)](./resolveaccounttype%28for,with%29.md)
  Resolves the account type to look for in a search.
- [func resolveOrganizationName(for: INSearchForAccountsIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolveorganizationname%28for,with%29.md)
  Resolves the organization name to use during a search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintenthandling/resolverequestedbalancetype(for:with:))*