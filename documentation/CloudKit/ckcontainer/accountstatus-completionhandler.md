# accountStatus(completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Determines whether the system can access the user’s iCloud account.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func accountStatus() async throws -> CKAccountStatus
```

#### Discussion

The closure has no return value and takes the following parameters:

- The status of the user’s iCloud account.
- An error that describes the failure, or `nil` if the system successfully determines the status.

This method determines the status of the user’s iCloud account asynchronously, passing the results to the closure that you provide. Call this method before accessing the private database to determine whether that database is available. While your app is running, use the [`CKAccountChanged`](https://developer.apple.com/documentation/foundation/nsnotification/name/1399172-ckaccountchanged) notification to detect account changes, and call this method again to determine the status of the new account.

## Parameters

- `completionHandler`: The handler to execute when the call completes.

## See Also

- [enum CKAccountStatus](ckaccountstatus.md)
  Constants that indicate the availability of the user’s iCloud account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/accountstatus(completionhandler:))*