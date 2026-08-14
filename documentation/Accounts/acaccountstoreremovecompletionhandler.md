# ACAccountStoreRemoveCompletionHandler

**Framework**: Accounts  
**Kind**: typealias

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

#### Discussion

The completion handler parameters are:

- **`success`**: A Boolean value indicating whether the operation was successful. [`true`](https://developer.apple.com/documentation/swift/true) if successful, otherwise [`false`](https://developer.apple.com/documentation/swift/false).
- **`error`**: An error, if one occurred.

## See Also

- [func removeAccount(ACAccount!, withCompletionHandler: ((Bool, (any Error)?) -> Void)!)](acaccountstore/removeaccount(_:withcompletionhandler:).md)
  Removes an account from the account store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstoreremovecompletionhandler)*