# requestAccessToAccounts(with:options:completion:)

**Framework**: Accounts  
**Kind**: method  
**Role**: Instance Method

Obtains permission to access protected user properties.

**Availability**:
- iOS 6.0+ - Deprecated in 15.0
- iPadOS 6.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.8+ - Deprecated in 12.0

> **Deprecated**: Use appropriate non-Apple SDK corresponding to the type of account you want to reference instead

## Declaration

```swift
func requestAccessToAccounts(with accountType: ACAccountType!, options: [AnyHashable : Any]! = [:], completion: (@Sendable (Bool, (any Error)?) -> Void)!)
```

```swift
func requestAccessToAccounts(with accountType: ACAccountType!, options: [AnyHashable : Any]! = [:]) async throws -> Bool
```

```objc
- (void) requestAccessToAccountsWithType:(ACAccountType *) accountType options:(NSDictionary *) options completion:(ACAccountStoreRequestAccessCompletionHandler) completion;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func requestAccessToAccounts(with accountType: ACAccountType!, options: [AnyHashable : Any]! = [:]) async throws -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

Certain account types (such as Facebook) require an options dictionary. This method throws an `NSInvalidArgumentException` if the options dictionary isn’t provided for such account types. Conversely, if the account type doesn’t require an options dictionary, the `options` parameter must be `nil`.

## Parameters

- `accountType`: The account type.
- `options`: A dictionary of options, if options are required by the account type; otherwise, `nil`.
- `completion`: The handler to call when the request has completed. The handler is called on an arbitrary queue.

## See Also

### Requesting Access
- [typealias ACAccountStoreRequestAccessCompletionHandler](../acaccountstorerequestaccesscompletionhandler.md)
  Specifies a handler to call when access is granted or denied.
- [- requestAccessToAccountsWithType:withCompletionHandler:](./requestaccesstoaccountswithtype_withcompletionhandler_.md)
  Requests access to accounts of the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accounts/acaccountstore/requestaccesstoaccounts(with:options:completion:))*