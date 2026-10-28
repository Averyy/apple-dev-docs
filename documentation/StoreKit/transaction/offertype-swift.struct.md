# Transaction.OfferType

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The types of offers that apply to a transaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct OfferType
```

## Overview

You don’t create offer types in [`Transaction.OfferType`](./offertype-swift.struct.md). The static values indicate the offer types that the system reports for a transaction.

## Topics

### Getting offer types
- [static let introductory: Transaction.OfferType](./offertype-swift.struct/introductory.md)
  An introductory offer for an auto-renewable subscription.
- [static let promotional: Transaction.OfferType](./offertype-swift.struct/promotional.md)
  A promotional offer for an auto-renewable subscription.
- [static let code: Transaction.OfferType](./offertype-swift.struct/code.md)
  An offer code.
- [static var winBack: Transaction.OfferType](./offertype-swift.struct/winback.md)
  A win-back offer for an auto-renewable subscription.
### Getting a localized description
- [var localizedDescription: String](./offertype-swift.struct/localizeddescription.md)
  The localized text that describes the offer type.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offertype-swift.struct)*