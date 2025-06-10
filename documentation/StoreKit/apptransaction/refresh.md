# refresh()

**Framework**: StoreKit  
**Kind**: method

Gets the App Store-signed app transaction information from the App Store server.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func refresh() async throws -> VerificationResult<AppTransaction>
```

#### Return Value

Returns a [`VerificationResult`](verificationresult.md) with a single [`AppTransaction`](apptransaction.md).

#### Discussion

This method queries the App Store server to refresh the app transaction information. This method returns a [`VerificationResult`](verificationresult.md) that contains the App Store-signed app transaction information for your app.

> ❗ **Important**:  Calling [`refresh()`](apptransaction/refresh().md) displays a system prompt that asks users to authenticate with their App Store credentials. Call this function only in response to an explicit user action, like tapping or clicking a button.

Use this method to get an [`AppTransaction`](apptransaction.md) in the following cases:

- The [`shared`](apptransaction/shared.md) property throws an error.
- The [`shared`](apptransaction/shared.md) property returns an unverified ([`VerificationResult.unverified(_:_:)`](verificationresult/unverified(_:_:).md) ) result.

This method throws an error if the user cancels the authentication prompt, if there’s no network connectivity, or if the call fails to update the app transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/apptransaction/refresh())*