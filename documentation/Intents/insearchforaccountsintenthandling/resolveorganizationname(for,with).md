# resolveOrganizationName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the organization name to use during a search.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func resolveOrganizationName(for intent: INSearchForAccountsIntent, with completion: @escaping @Sendable (INSpeakableStringResolutionResult) -> Void)
```

```swift
optional func resolveOrganizationName(for intent: INSearchForAccountsIntent) async -> INSpeakableStringResolutionResult
```

```objc
- (void) resolveOrganizationNameForSearchForAccounts:(INSearchForAccountsIntent *) intent withCompletion:(void (^)(INSpeakableStringResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve any questions about the organization name used during a search. Use this method to examine the [`organizationName`](../insearchforaccountsintent/organizationname.md) property of the `intent` object. Return a resolution of success if you can perform the search using the specified organization name. If the property does not contain a value, return a resolution of success or not required based if you can use other information in the intent object to perform the search.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

## See Also

### Resolving the Intent Parameters
- [func resolveAccountNickname(for: INSearchForAccountsIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolveaccountnickname%28for,with%29.md)
  Resolves the account nickname to use during a search.
- [func resolveAccountType(for: INSearchForAccountsIntent, with: (INAccountTypeResolutionResult) -> Void)](./resolveaccounttype%28for,with%29.md)
  Resolves the account type to look for in a search.
- [func resolveRequestedBalanceType(for: INSearchForAccountsIntent, with: (INBalanceTypeResolutionResult) -> Void)](./resolverequestedbalancetype%28for,with%29.md)
  Resolves the balance type to look for in a search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintenthandling/resolveorganizationname(for:with:))*