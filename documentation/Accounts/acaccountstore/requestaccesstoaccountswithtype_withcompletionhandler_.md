# requestAccessToAccountsWithType:withCompletionHandler:

**Framework**: Accounts  
**Kind**: method  
**Role**: Instance Method

Requests access to accounts of the specified type.

**Availability**:
- iOS 6.0+ - Deprecated in 6.0
- iPadOS 6.0+ - Deprecated in 6.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`requestAccessToAccounts(with:options:completion:)`](./requestaccesstoaccounts%28with,options,completion%29.md) instead.

## Declaration

```objc
- (void) requestAccessToAccountsWithType:(ACAccountType *) accountType withCompletionHandler:(ACAccountStoreRequestAccessCompletionHandler) handler;
```

#### Discussion

This method displays a dialog to the user confirming whether the application has access to the account. If access is granted, the application has access to protected properties of and operations on all accounts of the specified type.

## Parameters

- `accountType`: The account type.
- `handler`: The handler to call when access is granted or denied. The handler is called on an arbitrary queue.

## See Also

### Requesting Access
- [func requestAccessToAccounts(with: ACAccountType!, options: [AnyHashable : Any]!, completion: ((Bool, (any Error)?) -> Void)!)](./requestaccesstoaccounts%28with,options,completion%29.md)
  Obtains permission to access protected user properties.
- [typealias ACAccountStoreRequestAccessCompletionHandler](../acaccountstorerequestaccesscompletionhandler.md)
  Specifies a handler to call when access is granted or denied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore/requestaccesstoaccountswithtype:withcompletionhandler:)*