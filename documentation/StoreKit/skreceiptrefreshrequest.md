# SKReceiptRefreshRequest

**Framework**: StoreKit  
**Kind**: class

A request to the App Store to get the app receipt, which represents the customer’s transactions with your app.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
class SKReceiptRefreshRequest
```

## Mentions

- [Choosing a receipt validation technique](choosing-a-receipt-validation-technique.md)
- [Restoring purchased products](restoring-purchased-products.md)
- [Validating receipts with the App Store](validating-receipts-with-the-app-store.md)

#### Overview

> **Note**:  The receipt isn’t necessary if you use [`AppTransaction`](apptransaction.md) to validate the app download, or [`Transaction`](transaction.md) to validate in-app purchases. Only use the receipt if your app uses the [`Original API for In-App Purchase`](original-api-for-in-app-purchase.md), or needs the receipt to validate the app download because it can’t use [`AppTransaction`](apptransaction.md).

Use this API to request a new app receipt from the App Store if the receipt is invalid or missing from its expected location, [`appStoreReceiptURL`](https://developer.apple.com/documentation/Foundation/Bundle/appStoreReceiptURL). To request the receipt using the [`SKReceiptRefreshRequest`](skreceiptrefreshrequest.md) object, you initialize it, attach a [`delegate`](skrequest/delegate.md), and then call the request’s [`start()`](skrequest/start().md) method.

> ❗ **Important**:  The receipt refresh request displays a system prompt that asks users to authenticate with their App Store credentials. For a better user experience, initiate the request after an explicit user action, like tapping or clicking a button.

When the request completes successfully, your delegate receives an [`SKReceiptRefreshRequest`](skreceiptrefreshrequest.md) object in its [`requestDidFinish(_:)`](skrequestdelegate/requestdidfinish(_:).md) method. Locate the app receipt using the [`appStoreReceiptURL`](https://developer.apple.com/documentation/Foundation/Bundle/appStoreReceiptURL) property. For information about validating the receipt, see [`Choosing a receipt validation technique`](choosing-a-receipt-validation-technique.md).

If the request fails and calls your delegate’s [`request(_:didFailWithError:)`](skrequestdelegate/request(_:didfailwitherror:).md) method, your app needs to release the request and not attempt to call it a second time. Requests can fail when a user doesn’t authenticate or chooses to cancel the request. Without a validated receipt, assume the user doesn’t have access to premium content.

In the sandbox environment, you can initialize a receipt with any combination of properties for testing when you call [`init(receiptProperties:)`](skreceiptrefreshrequest/init(receiptproperties:).md).

##### Use Alternative Techniques

There are times when using [`SKReceiptRefreshRequest`](skreceiptrefreshrequest.md) isn’t necessary, so avoid doing so, such as in the following scenarios:

- If the receipt is valid, but may be missing transactions, use [`restoreCompletedTransactions()`](skpaymentqueue/restorecompletedtransactions().md) instead. For example, the receipt may be missing a transaction if a person purchases a new subscription on another device.
- In the sandbox environment, before the tester completes their first in-app purchase. Receipts are initially absent in the sandbox environment for iOS and iPadOS apps. For more information, see [`appStoreReceiptURL`](https://developer.apple.com/documentation/Foundation/Bundle/appStoreReceiptURL).

## Topics

### Initializing Receipt Refresh Requests
- [init(receiptProperties: [String : Any]?)](skreceiptrefreshrequest/init(receiptproperties:).md)
  Creates a receipt refresh request with optional properties.
### Receipt Properties and Keys
- [var receiptProperties: [String : Any]?](skreceiptrefreshrequest/receiptproperties.md)
  The properties of the receipt.
- [let SKReceiptPropertyIsExpired: String](skreceiptpropertyisexpired.md)
  A key with a value that indicates whether the receipt is in an expired state.
- [let SKReceiptPropertyIsRevoked: String](skreceiptpropertyisrevoked.md)
  A key with a value that indicates whether the receipt is in a revoked state.
- [let SKReceiptPropertyIsVolumePurchase: String](skreceiptpropertyisvolumepurchase.md)
  A key with a value that indicates whether the receipt is a Volume Purchase Plan receipt.

## Relationships

### Inherits From
- [SKRequest](skrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Choosing a receipt validation technique](choosing-a-receipt-validation-technique.md)
  Select the type of receipt validation, on the device or on your server, that works for your app.
- [Validating receipts with the App Store](validating-receipts-with-the-app-store.md)
  Verify transactions with the App Store on a secure server.
- [var appStoreReceiptURL: URL? { get }](../Foundation/Bundle/appStoreReceiptURL.md)
  The file URL for the bundle’s App Store receipt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest)*