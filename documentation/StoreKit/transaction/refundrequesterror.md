# Transaction.RefundRequestError

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

The error codes for refund requests.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum RefundRequestError
```

#### Overview

The following methods throw refund request errors: [`beginRefundRequest(in:)`](./beginrefundrequest%28in%29-9k0pj.md), [`beginRefundRequest(for:in:)`](./beginrefundrequest%28for,in%29-65tph.md), [`beginRefundRequest(in:)`](./beginrefundrequest%28in%29-63bvd.md), and [`beginRefundRequest(for:in:)`](./beginrefundrequest%28for,in%29-9mscy.md).

## Topics

### Error Enumeration
- [Transaction.RefundRequestError.duplicateRequest](./refundrequesterror/duplicaterequest.md)
  The App Store has already received a refund request for this Apple In-App Purchase.
- [Transaction.RefundRequestError.failed](./refundrequesterror/failed.md)
  The refund request submission failed.
### Enumeration Cases
- [Transaction.RefundRequestError.ineligible](./refundrequesterror/ineligible.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Requesting refunds
- [Testing refund requests](../testing-refund-requests.md)
  Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.
- [func beginRefundRequest(in: UIWindowScene) async throws -> Transaction.RefundRequestStatus](./beginrefundrequest%28in%29-9k0pj.md)
  Presents the refund request sheet for the transaction in a window scene.
- [func beginRefundRequest(in: NSViewController) async throws -> Transaction.RefundRequestStatus](./beginrefundrequest%28in%29-63bvd.md)
  Presents the refund request sheet for the transaction in a view controller.
- [static func beginRefundRequest(for: UInt64, in: UIWindowScene) async throws -> Transaction.RefundRequestStatus](./beginrefundrequest%28for,in%29-65tph.md)
  Presents the refund request sheet for the specified transaction in a window scene.
- [static func beginRefundRequest(for: UInt64, in: NSViewController) async throws -> Transaction.RefundRequestStatus](./beginrefundrequest%28for,in%29-9mscy.md)
  Presents the refund request sheet for the specified transaction in a view controller.
- [Transaction.RefundRequestStatus](./refundrequeststatus.md)
  The status codes for refund requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/refundrequesterror)*