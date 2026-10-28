# ACAccountStoreSaveCompletionHandler

**Framework**: Accounts  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef void (^)(_Bool, NSError *) ACAccountStoreSaveCompletionHandler;
```

## Discussion

The completion handler parameters are:

- **`success`**: A Boolean value indicating whether the operation is successful. [`true`](../Swift/true.md) if the operation is successful; otherwise [`false`](../Swift/false.md).
- **`error`**: An error, if one occurred.

## See Also

### Saving Accounts
- [func saveAccount(ACAccount!, withCompletionHandler: ((Bool, (any Error)?) -> Void)!)](./acaccountstore/saveaccount%28_,withcompletionhandler%29.md)
  Saves an account to the Accounts database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstoresavecompletionhandler)*