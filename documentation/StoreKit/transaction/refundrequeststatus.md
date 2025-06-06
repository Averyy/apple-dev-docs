# Transaction.RefundRequestStatus

**Framework**: StoreKit  
**Kind**: enum

The status codes for refund requests.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum RefundRequestStatus
```

#### Overview

The following methods throw the refund request status: [`beginRefundRequest(in:)`](transaction/beginrefundrequest(in:)-9k0pj.md),  [`beginRefundRequest(for:in:)`](transaction/beginrefundrequest(for:in:)-65tph.md), [`beginRefundRequest(in:)`](transaction/beginrefundrequest(in:)-63bvd.md), and [`beginRefundRequest(for:in:)`](transaction/beginrefundrequest(for:in:)-9mscy.md).

The refund request status reflects the status of the request, not the status of the refund itself.

## Topics

### Getting Refund Request Status
- [Transaction.RefundRequestStatus.userCancelled](transaction/refundrequeststatus/usercancelled.md)
  The user canceled submission of their refund request.
- [Transaction.RefundRequestStatus.success](transaction/refundrequeststatus/success.md)
  The App Store has received the refund request.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Testing refund requests](testing-refund-requests.md)
  Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.
- [func beginRefundRequest(in: UIWindowScene) async throws -> Transaction.RefundRequestStatus](transaction/beginrefundrequest(in:)-9k0pj.md)
  Presents the refund request sheet for the transaction in a window scene.
- [func beginRefundRequest(in: NSViewController) async throws -> Transaction.RefundRequestStatus](transaction/beginrefundrequest(in:)-63bvd.md)
  Presents the refund request sheet for the transaction in a view controller.
- [static func beginRefundRequest(for: UInt64, in: UIWindowScene) async throws -> Transaction.RefundRequestStatus](transaction/beginrefundrequest(for:in:)-65tph.md)
  Presents the refund request sheet for the specified transaction in a window scene.
- [static func beginRefundRequest(for: UInt64, in: NSViewController) async throws -> Transaction.RefundRequestStatus](transaction/beginrefundrequest(for:in:)-9mscy.md)
  Presents the refund request sheet for the specified transaction in a view controller.
- [Transaction.RefundRequestError](transaction/refundrequesterror.md)
  The error codes for refund requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/refundrequeststatus)*