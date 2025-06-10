# AppTransaction

**Framework**: StoreKit  
**Kind**: struct

Information that represents the customer’s purchase of the app, cryptographically signed by the App Store.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct AppTransaction
```

## Mentions

- [Choosing a receipt validation technique](choosing-a-receipt-validation-technique.md)
- [Supporting business model changes by using the app transaction](supporting-business-model-changes-by-using-the-app-transaction.md)
- [Validating receipts with the App Store](validating-receipts-with-the-app-store.md)

#### Overview

> **Note**:  Session 10007:  [`What’s new with in-app purchase`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10007/)

## Topics

### Getting the signed app transaction
- [static var shared: VerificationResult<AppTransaction>](apptransaction/shared.md)
  Gets the App Store-signed app transaction information for the app.
### Getting the app transaction identifier
- [var appTransactionID: String](apptransaction/apptransactionid.md)
  The unique identifier of the app download transaction.
### Getting the environment
- [let environment: AppStore.Environment](apptransaction/environment.md)
  The server environment that signs the app transaction.
- [AppStore.Environment](appstore/environment.md)
  Constants that represent the App Store server environment.
### Getting app and version information
- [let bundleID: String](apptransaction/bundleid.md)
  The bundle identifier that the app transaction applies to.
- [let appVersion: String](apptransaction/appversion.md)
  The app version that the app transaction applies to.
- [let originalAppVersion: String](apptransaction/originalappversion.md)
  The app version that the customer originally purchased from the App Store.
- [let appID: UInt64?](apptransaction/appid.md)
  The unique identifier the App Store uses to identify the app.
- [let appVersionID: UInt64?](apptransaction/appversionid.md)
  The number that the App Store uses to uniquely identify the version of the app.
### Getting the original platform
- [let originalPlatform: AppStore.Platform](apptransaction/originalplatform.md)
  The platform on which the customer originally purchased the app.
- [AppStore.Platform](appstore/platform.md)
  Values that represent Apple platforms.
### Getting purchase dates
- [let originalPurchaseDate: Date](apptransaction/originalpurchasedate.md)
  The date the customer originally purchased the app from the App Store.
- [let preorderDate: Date?](apptransaction/preorderdate.md)
  The date the customer placed an order for the app before it’s available in the App Store.
### Verifying the app transaction
- [let deviceVerification: Data](apptransaction/deviceverification.md)
  The device verification value to use to verify whether the app transaction belongs to the device.
- [let deviceVerificationNonce: UUID](apptransaction/deviceverificationnonce.md)
  The UUID used to compute the device verification value.
- [let signedDate: Date](apptransaction/signeddate.md)
  The date that the App Store signed the JWS app transaction.
### Getting app transaction information in JSON format
- [var jsonRepresentation: Data](apptransaction/jsonrepresentation.md)
  The JSON representation of the app transaction information.
### Getting app transaction from the server
- [static func refresh() async throws -> VerificationResult<AppTransaction>](apptransaction/refresh.md)
  Gets the App Store-signed app transaction information from the App Store server.
### Deprecated
- [var originalPlatformStringRepresentation: String](apptransaction/originalplatformstringrepresentation.md)
  The string representation of the platform on which the customer originally purchased the app.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Supporting business model changes by using the app transaction](supporting-business-model-changes-by-using-the-app-transaction.md)
  Access the app transaction to learn when a customer first purchased an app, to determine the app features they’re entitled to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/apptransaction)*