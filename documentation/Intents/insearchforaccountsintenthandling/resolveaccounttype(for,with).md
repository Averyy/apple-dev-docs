# resolveAccountType(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the account type to look for in a search.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func resolveAccountType(for intent: INSearchForAccountsIntent, with completion: @escaping @Sendable (INAccountTypeResolutionResult) -> Void)
```

```swift
optional func resolveAccountType(for intent: INSearchForAccountsIntent) async -> INAccountTypeResolutionResult
```

```objc
- (void) resolveAccountTypeForSearchForAccounts:(INSearchForAccountsIntent *) intent withCompletion:(void (^)(INAccountTypeResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this question to resolve any questions about the account type to look for in a search. Use this method to examine the [`accountType`](../insearchforaccountsintent/accounttype.md) property of the intent object. Return a successful resolution if you can search for accounts of the specified type.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

## See Also

### Resolving the Intent Parameters
- [func resolveAccountNickname(for: INSearchForAccountsIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolveaccountnickname%28for,with%29.md)
  Resolves the account nickname to use during a search.
- [func resolveOrganizationName(for: INSearchForAccountsIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolveorganizationname%28for,with%29.md)
  Resolves the organization name to use during a search.
- [func resolveRequestedBalanceType(for: INSearchForAccountsIntent, with: (INBalanceTypeResolutionResult) -> Void)](./resolverequestedbalancetype%28for,with%29.md)
  Resolves the balance type to look for in a search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintenthandling/resolveaccounttype(for:with:))*