# DataDetector.Match.SemanticDetails.MoneyAmount

**Framework**: DataDetection  
**Kind**: struct  
**Role**: Structure

A match that the data detector determines represents an amount of money.

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
struct MoneyAmount
```

#### Discussion

The framework returns [`currency`](./moneyamount/currency.md) as the match’s currency, though it may be a best guess. The [`amount`](./moneyamount/amount.md) is the amount of money in the specified currency.

## Topics

### Properties that describe elements of the amount
- [let amount: Decimal](./moneyamount/amount.md)
  A value that represents the amount of money in the specified currency.
- [let currency: Locale.Currency](./moneyamount/currency.md)
  A value that represents the currency the data detectors were able to match, though it may be a best guess.

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

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails/moneyamount)*