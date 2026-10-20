# removeAccount(_:withCompletionHandler:)

**Framework**: Accounts  
**Kind**: method  
**Role**: Instance Method

Removes an account from the account store.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
func removeAccount(_ account: ACAccount!, withCompletionHandler completionHandler: (@Sendable (Bool, (any Error)?) -> Void)!)
```

```swift
func removeAccount(_ account: ACAccount!) async throws -> Bool
```

```objc
- (void) removeAccount:(ACAccount *) account withCompletionHandler:(ACAccountStoreRemoveCompletionHandler) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func removeAccount(_ account: ACAccount!) async throws -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

This call will fail if you don’t have sufficient rights to remove the account.

## Parameters

- `account`: The account to remove.
- `completionHandler`: The handler to call when the removal has completed.

## See Also

### Removing Accounts
- [typealias ACAccountStoreRemoveCompletionHandler](../acaccountstoreremovecompletionhandler.md)
  Specifies a handler to call when an account is removed from the store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore/removeaccount(_:withcompletionhandler:))*