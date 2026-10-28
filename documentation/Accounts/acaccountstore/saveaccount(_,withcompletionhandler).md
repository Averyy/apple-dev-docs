# saveAccount(_:withCompletionHandler:)

**Framework**: Accounts  
**Kind**: method  
**Role**: Instance Method

Saves an account to the Accounts database.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
func saveAccount(_ account: ACAccount!, withCompletionHandler completionHandler: (@Sendable (Bool, (any Error)?) -> Void)!)
```

```swift
func saveAccount(_ account: ACAccount!) async throws -> Bool
```

```objc
- (void) saveAccount:(ACAccount *) account withCompletionHandler:(ACAccountStoreSaveCompletionHandler) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func saveAccount(_ account: ACAccount!) async throws -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

If the account type supports authentication and the account isn’t authenticated, the account server uses the account’s credentials to authenticate it. If the authentication is successful, the account is saved; otherwise it’s not saved.

## Parameters

- `account`: The account to save.
- `completionHandler`: The handler to call when the operation completes. The handler is called on an arbitrary queue.

## See Also

### Saving Accounts
- [typealias ACAccountStoreSaveCompletionHandler](../acaccountstoresavecompletionhandler.md)
  Specifies a handler to call when an Accounts database operation is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore/saveaccount(_:withcompletionhandler:))*