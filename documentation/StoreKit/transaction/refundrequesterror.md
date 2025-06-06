# Transaction.RefundRequestError

**Framework**: StoreKit  
**Kind**: enum

The error codes for refund requests.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum RefundRequestError
```

#### Overview

The following methods throw refund request errors: [`beginRefundRequest(in:)`](transaction/beginrefundrequest(in:)-9k0pj.md), [`beginRefundRequest(for:in:)`](transaction/beginrefundrequest(for:in:)-65tph.md), [`beginRefundRequest(in:)`](transaction/beginrefundrequest(in:)-63bvd.md), and [`beginRefundRequest(for:in:)`](transaction/beginrefundrequest(for:in:)-9mscy.md).

## Topics

### Error Enumeration
- [Transaction.RefundRequestError.duplicateRequest](transaction/refundrequesterror/duplicaterequest.md)
  The App Store has already received a refund request for this in-app purchase.
- [Transaction.RefundRequestError.failed](transaction/refundrequesterror/failed.md)
  The refund request submission failed.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
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
- [Transaction.RefundRequestStatus](transaction/refundrequeststatus.md)
  The status codes for refund requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/refundrequesterror)*