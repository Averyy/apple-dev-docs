# accountStatus(completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the system can access the user’s iCloud account.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func accountStatus(completionHandler: @escaping @Sendable (CKAccountStatus, (any Error)?) -> Void)
```

```swift
func accountStatus() async throws -> CKAccountStatus
```

```objc
- (void) accountStatusWithCompletionHandler:(void (^)(CKAccountStatus accountStatus, NSError *error)) completionHandler;
```

## Discussion

The closure has no return value and takes the following parameters:

- The status of the user’s iCloud account.
- An error that describes the failure, or `nil` if the system successfully determines the status.

This method determines the status of the user’s iCloud account asynchronously, passing the results to the closure that you provide. Call this method before accessing the private database to determine whether that database is available. While your app is running, use the [`CKAccountChanged`](../../Foundation/nsnotification/name-swift.struct/ckaccountchanged.md) notification to detect account changes, and call this method again to determine the status of the new account.

## Parameters

- `completionHandler`: The handler to execute when the call completes.

## See Also

### Determining the User’s iCloud Access Status
- [enum CKAccountStatus](../ckaccountstatus.md)
  Constants that indicate the availability of the user’s iCloud account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/accountstatus(completionhandler:))*