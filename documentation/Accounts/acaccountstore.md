# ACAccountStore

**Framework**: Accounts  
**Kind**: class  
**Role**: Class

The object you use to request, manage, and store the user’s account information.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
class ACAccountStore
```

```objc
@interface ACAccountStore : NSObject
```

#### Overview

The [`ACAccountStore`](./acaccountstore.md) class provides an interface for accessing, managing, and storing accounts. To create and retrieve accounts from the Accounts database, you must create an [`ACAccountStore`](./acaccountstore.md) object. Each [`ACAccount`](./acaccount.md) object belongs to a single account store object.

## Topics

### Requesting Access
- [func requestAccessToAccounts(with: ACAccountType!, options: [AnyHashable : Any]!, completion: ((Bool, (any Error)?) -> Void)!)](./acaccountstore/requestaccesstoaccounts%28with,options,completion%29.md)
  Obtains permission to access protected user properties.
- [typealias ACAccountStoreRequestAccessCompletionHandler](./acaccountstorerequestaccesscompletionhandler.md)
  Specifies a handler to call when access is granted or denied.
### Getting Accounts
- [var accounts: NSArray!](./acaccountstore/accounts.md)
  The accounts managed by this account store.
- [func account(withIdentifier: String!) -> ACAccount!](./acaccountstore/account%28withidentifier%29.md)
  Returns the account with the specified identifier.
- [func accounts(with: ACAccountType!) -> [Any]!](./acaccountstore/accounts%28with%29.md)
  Returns all accounts of the specified type.
### Getting Account Types
- [func accountType(withAccountTypeIdentifier: String!) -> ACAccountType!](./acaccountstore/accounttype%28withaccounttypeidentifier%29.md)
  Returns an account type that matches the specified identifier.
### Saving Accounts
- [func saveAccount(ACAccount!, withCompletionHandler: ((Bool, (any Error)?) -> Void)!)](./acaccountstore/saveaccount%28_,withcompletionhandler%29.md)
  Saves an account to the Accounts database.
- [typealias ACAccountStoreSaveCompletionHandler](./acaccountstoresavecompletionhandler.md)
  Specifies a handler to call when an Accounts database operation is complete.
### Renewing Account Credentials
- [func renewCredentials(for: ACAccount!, completion: ((ACAccountCredentialRenewResult, (any Error)?) -> Void)!)](./acaccountstore/renewcredentials%28for,completion%29.md)
  Renews account credentials when the credentials are no longer valid.
- [typealias ACAccountStoreCredentialRenewalHandler](./acaccountstorecredentialrenewalhandler.md)
  Specifies a handler to call when credentials are renewed.
- [enum ACAccountCredentialRenewResult](./acaccountcredentialrenewresult.md)
  Status codes of credential renewal requests.
### Removing Accounts
- [func removeAccount(ACAccount!, withCompletionHandler: ((Bool, (any Error)?) -> Void)!)](./acaccountstore/removeaccount%28_,withcompletionhandler%29.md)
  Removes an account from the account store.
- [typealias ACAccountStoreRemoveCompletionHandler](./acaccountstoreremovecompletionhandler.md)
  Specifies a handler to call when an account is removed from the store.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Account Management
- [class ACAccount](./acaccount.md)
  The information associated with one of the user’s accounts.
- [class ACAccountCredential](./acaccountcredential.md)
  A credential object that encapsulates the information needed to authenticate a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore)*