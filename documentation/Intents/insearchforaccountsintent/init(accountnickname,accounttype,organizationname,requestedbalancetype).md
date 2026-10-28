# init(accountNickname:accountType:organizationName:requestedBalanceType:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified search parameters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(accountNickname: INSpeakableString?, accountType: INAccountType, organizationName: INSpeakableString?, requestedBalanceType: INBalanceType)
```

```objc
- (instancetype) initWithAccountNickname:(INSpeakableString *) accountNickname accountType:(INAccountType) accountType organizationName:(INSpeakableString *) organizationName requestedBalanceType:(INBalanceType) requestedBalanceType;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you do not create instances of this class yourself. Instead, SiriKit creates instances when the user asks for account information. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `accountNickname`: The nickname that the user assigned to the account in your app. Account nicknames make it easier for the user to refer to those accounts in Siri. For example, a user’s main checking account might be called “checking”.
- `accountType`: The type of the account. For a list of possible values, see [`INAccountType`](../inaccounttype.md).
- `organizationName`: The name of an organization attached to an account.
- `requestedBalanceType`: The type of balance requested by the user. Use this information to help identify the account to return. For a list of possible values, see [`INBalanceType`](../inbalancetype.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintent/init(accountnickname:accounttype:organizationname:requestedbalancetype:))*