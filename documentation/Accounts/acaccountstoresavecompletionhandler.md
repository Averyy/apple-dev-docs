# ACAccountStoreSaveCompletionHandler

**Framework**: Accounts  
**Kind**: typealias

Specifies a handler to call when an Accounts database operation is complete.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.8+

## Declaration

```swift
typealias ACAccountStoreSaveCompletionHandler = (Bool, (any Error)?) -> Void
```

#### Discussion

The completion handler parameters are:

## See Also

- [func saveAccount(ACAccount!, withCompletionHandler: ((Bool, (any Error)?) -> Void)!)](acaccountstore/saveaccount(_:withcompletionhandler:).md)
  Saves an account to the Accounts database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstoresavecompletionhandler)*