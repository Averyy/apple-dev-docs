# ACAccountStoreRequestAccessCompletionHandler

**Framework**: Accounts  
**Kind**: typealias

Specifies a handler to call when access is granted or denied.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.8+

## Declaration

```swift
typealias ACAccountStoreRequestAccessCompletionHandler = (Bool, (any Error)?) -> Void
```

#### Discussion

The completion handler parameters are:

## See Also

- [func requestAccessToAccounts(with: ACAccountType!, options: [AnyHashable : Any]!, completion: ACAccountStoreRequestAccessCompletionHandler!)](acaccountstore/requestaccesstoaccounts(with:options:completion:).md)
  Obtains permission to access protected user properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstorerequestaccesscompletionhandler)*