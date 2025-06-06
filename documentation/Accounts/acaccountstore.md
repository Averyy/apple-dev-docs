# ACAccountStore

**Framework**: Accounts  
**Kind**: class

The object you use to request, manage, and store the user’s account information.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
class ACAccountStore
```

#### Overview

The [`ACAccountStore`](acaccountstore.md) class provides an interface for accessing, managing, and storing accounts. To create and retrieve accounts from the Accounts database, you must create an [`ACAccountStore`](acaccountstore.md) object. Each [`ACAccount`](acaccount.md) object belongs to a single account store object.

## Topics

### Requesting Access
- [func requestAccessToAccounts(with: ACAccountType!, options: [AnyHashable : Any]!, completion: ACAccountStoreRequestAccessCompletionHandler!)](acaccountstore/requestaccesstoaccounts(with:options:completion:).md)
  Obtains permission to access protected user properties.
- [typealias ACAccountStoreRequestAccessCompletionHandler](acaccountstorerequestaccesscompletionhandler.md)
  Specifies a handler to call when access is granted or denied.
### Getting Accounts
- [var accounts: NSArray!](acaccountstore/accounts.md)
  The accounts managed by this account store.
- [func account(withIdentifier: String!) -> ACAccount!](acaccountstore/account(withidentifier:).md)
  Returns the account with the specified identifier.
- [func accounts(with: ACAccountType!) -> [Any]!](acaccountstore/accounts(with:).md)
  Returns all accounts of the specified type.
### Getting Account Types
- [func accountType(withAccountTypeIdentifier: String!) -> ACAccountType!](acaccountstore/accounttype(withaccounttypeidentifier:).md)
  Returns an account type that matches the specified identifier.
### Saving Accounts
- [func saveAccount(ACAccount!, withCompletionHandler: ACAccountStoreSaveCompletionHandler!)](acaccountstore/saveaccount(_:withcompletionhandler:).md)
  Saves an account to the Accounts database.
- [typealias ACAccountStoreSaveCompletionHandler](acaccountstoresavecompletionhandler.md)
  Specifies a handler to call when an Accounts database operation is complete.
### Renewing Account Credentials
- [func renewCredentials(for: ACAccount!, completion: ACAccountStoreCredentialRenewalHandler!)](acaccountstore/renewcredentials(for:completion:).md)
  Renews account credentials when the credentials are no longer valid.
- [typealias ACAccountStoreCredentialRenewalHandler](acaccountstorecredentialrenewalhandler.md)
  Specifies a handler to call when credentials are renewed.
- [enum ACAccountCredentialRenewResult](acaccountcredentialrenewresult.md)
  Status codes of credential renewal requests.
### Removing Accounts
- [func removeAccount(ACAccount!, withCompletionHandler: ACAccountStoreRemoveCompletionHandler!)](acaccountstore/removeaccount(_:withcompletionhandler:).md)
  Removes an account from the account store.
- [typealias ACAccountStoreRemoveCompletionHandler](acaccountstoreremovecompletionhandler.md)
  Specifies a handler to call when an account is removed from the store.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ACAccount](acaccount.md)
  The information associated with one of the user’s accounts.
- [class ACAccountCredential](acaccountcredential.md)
  A credential object that encapsulates the information needed to authenticate a user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore)*