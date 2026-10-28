# DataDetector.Match.SemanticDetails.PaymentIdentifier

**Framework**: DataDetection  
**Kind**: struct  
**Role**: Structure

A match that the data detector determines represents a payment identifier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct PaymentIdentifier
```

## Discussion

The [`identifier`](./paymentidentifier/identifier.md) property is an identifier suitable to initiate a payment transaction. The [`type`](./paymentidentifier/type.md) is the type of payment system.

## Topics

- [let identifier: String](./paymentidentifier/identifier.md)
  An identifier suitable to initiate a payment transaction.
- [let type: DataDetector.Match.SemanticDetails.PaymentIdentifier.PaymentSystem](./paymentidentifier/type.md)
  The type of payment system.
### Enumerations
- [DataDetector.Match.SemanticDetails.PaymentIdentifier.PaymentSystem](./paymentidentifier/paymentsystem.md)
  Values that describe payment system types.

## Relationships

### Conforms To
- [Copyable](../../../../Swift/copyable.md)
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Escapable](../../../../Swift/escapable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails/paymentidentifier)*