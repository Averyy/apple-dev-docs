# beginRefundRequest(for:in:)

**Framework**: StoreKit  
**Kind**: method

Presents the refund request sheet for the specified transaction in a view controller.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+

## Declaration

```swift
static func beginRefundRequest(for transactionID: UInt64, in controller: NSViewController) async throws -> Transaction.RefundRequestStatus
```

## Mentions

- [Testing refund requests](testing-refund-requests.md)

#### Return Value

[`Transaction.RefundRequestStatus`](transaction/refundrequeststatus.md)

#### Discussion

Call this function from account settings or a help menu to enable customers to request a refund for an in-app purchase within your app. When you call this function, the system displays a refund sheet with the customer’s purchase details and a list of reason codes for the customer to choose from. For design guidance, see [`Human Interface Guidelines > In-app purchase > Providing help with in-app purchases`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/in-app-purchase/overview/introduction/#providing-help-with-in-app-purchases).

When a customer requests a refund for consumable in-app purchases through your app, the App Stores sends a `CONSUMPTION_REQUEST` [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType) to your server. If the customer provided consent, respond by sending consumption data to the App Store using the [`Send Consumption Information`](https://developer.apple.com/documentation/AppStoreServerAPI/Send-Consumption-Information) endpoint. If not, don’t respond to the `CONSUMPTION_REQUEST` notification.

The App Store takes up to 48 hours to either approve or deny a refund.

For information about setting up your server to receive notifications, see [`Enabling App Store Server Notifications`](enabling-app-store-server-notifications.md).

> **Note**:  If your app uses SwiftUI, use [`refundRequestSheet(for:isPresented:onDismiss:)`](https://developer.apple.com/documentation/SwiftUI/View/refundRequestSheet(for:isPresented:onDismiss:)) instead. For example usage, see [`Food Truck: Building a SwiftUI multiplatform app`](https://developer.apple.com/documentation/swiftui/food_truck_building_a_swiftui_multiplatform_app).

 If your app uses SwiftUI, use [`refundRequestSheet(for:isPresented:onDismiss:)`](https://developer.apple.com/documentation/SwiftUI/View/refundRequestSheet(for:isPresented:onDismiss:)) instead. For example usage, see [`Food Truck: Building a SwiftUI multiplatform app`](https://developer.apple.com/documentation/swiftui/food_truck_building_a_swiftui_multiplatform_app).

##### Test Refund Requests

The sandbox environment and StoreKit Testing in Xcode both support testing refund requests. For more information, see [`Testing refund requests`](testing-refund-requests.md).

## Parameters

- `transactionID`: The identifier of the transaction the user is requesting a refund for.
- `controller`: The   that the system displays the sheet on.

## See Also

- [Testing refund requests](testing-refund-requests.md)
  Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.
- [func beginRefundRequest(in: UIWindowScene) async throws -> Transaction.RefundRequestStatus](transaction/beginrefundrequest(in:)-9k0pj.md)
  Presents the refund request sheet for the transaction in a window scene.
- [func beginRefundRequest(in: NSViewController) async throws -> Transaction.RefundRequestStatus](transaction/beginrefundrequest(in:)-63bvd.md)
  Presents the refund request sheet for the transaction in a view controller.
- [static func beginRefundRequest(for: UInt64, in: UIWindowScene) async throws -> Transaction.RefundRequestStatus](transaction/beginrefundrequest(for:in:)-65tph.md)
  Presents the refund request sheet for the specified transaction in a window scene.
- [Transaction.RefundRequestError](transaction/refundrequesterror.md)
  The error codes for refund requests.
- [Transaction.RefundRequestStatus](transaction/refundrequeststatus.md)
  The status codes for refund requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/beginrefundrequest(for:in:)-9mscy)*