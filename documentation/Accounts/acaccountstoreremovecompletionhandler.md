# ACAccountStoreRemoveCompletionHandler

**Framework**: Accounts  
**Kind**: typealias  
**Role**: Type Alias

Specifies a handler to call when an account is removed from the store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.8+

## Declaration

```swift
typealias ACAccountStoreRemoveCompletionHandler = (Bool, (any Error)?) -> Void
```

```c
typedef void (^)(_Bool, NSError *) ACAccountStoreRemoveCompletionHandler;
```

#### Discussion

The completion handler parameters are:

- **`success`**: A Boolean value indicating whether the operation was successful. [`true`](../Swift/true.md) if successful, otherwise [`false`](../Swift/false.md).
- **`error`**: An error, if one occurred.

## See Also

### Removing Accounts
- [func removeAccount(ACAccount!, withCompletionHandler: ((Bool, (any Error)?) -> Void)!)](./acaccountstore/removeaccount%28_,withcompletionhandler%29.md)
  Removes an account from the account store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstoreremovecompletionhandler)*