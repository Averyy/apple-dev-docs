# ACAccountStoreRequestAccessCompletionHandler

**Framework**: Accounts  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef void (^)(_Bool, NSError *) ACAccountStoreRequestAccessCompletionHandler;
```

## Discussion

The completion handler parameters are:

- **`granted`**: A Boolean value indicating whether access is granted. [`true`](../Swift/true.md) if access is granted; otherwise [`false`](../Swift/false.md).
- **`error`**: An error, if one occurred.

## See Also

### Requesting Access
- [func requestAccessToAccounts(with: ACAccountType!, options: [AnyHashable : Any]!, completion: ((Bool, (any Error)?) -> Void)!)](./acaccountstore/requestaccesstoaccounts%28with,options,completion%29.md)
  Obtains permission to access protected user properties.
- [- requestAccessToAccountsWithType:withCompletionHandler:](./acaccountstore/requestaccesstoaccountswithtype_withcompletionhandler_.md)
  Requests access to accounts of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstorerequestaccesscompletionhandler)*