# shared

**Framework**: StoreKit  
**Kind**: property

Gets the App Store-signed app transaction information for the app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static var shared: VerificationResult<AppTransaction> { get async throws }
```

#### Discussion

Use this property to get a [`VerificationResult`](verificationresult.md) that contains the App Store-signed app transaction information for your app, including the first time the app launches. StoreKit automatically keeps the app transaction up-to-date.

This property throws an error if the [`AppTransaction`](apptransaction.md) isn’t available or if the user isn’t authenticated with the App Store. Getting an [`AppTransaction`](apptransaction.md) may require network connectivity.

The following example shows how to get the [`AppTransaction`](apptransaction.md).

```swift
do {
    let verificationResult = try await AppTransaction.shared

    switch verificationResult {
    case .verified(let appTransaction):
        // StoreKit verified that the user purchased this app and
        // the properties in the AppTransaction instance.
        // Add your code here.
    case .unverified(let appTransaction, let verificationError):
        // The app transaction didn't pass StoreKit's verification.        
        // Handle unverified app transaction information according
        // to your business model.
        // Add your code here.
    }
}
catch {
  // Handle errors.
}

```

If your app fails to get an [`AppTransaction`](apptransaction.md) by accessing the [`shared`](apptransaction/shared.md) property, see [`refresh()`](apptransaction/refresh().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/apptransaction/shared)*