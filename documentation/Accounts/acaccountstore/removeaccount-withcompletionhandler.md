# removeAccount(_:withCompletionHandler:)

**Framework**: Accounts  
**Kind**: method

Removes an account from the account store.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func removeAccount(_ account: ACAccount!) async throws -> Bool
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func removeAccount(_ account: ACAccount!) async throws -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This call will fail if you don’t have sufficient rights to remove the account.

## Parameters

- `account`: The account to remove.
- `completionHandler`: The handler to call when the removal has completed.

## See Also

- [typealias ACAccountStoreRemoveCompletionHandler](acaccountstoreremovecompletionhandler.md)
  Specifies a handler to call when an account is removed from the store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore/removeaccount(_:withcompletionhandler:))*