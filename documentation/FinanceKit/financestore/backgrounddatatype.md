# FinanceStore.BackgroundDataType

**Framework**: FinanceKit  
**Kind**: enum

The types of data in the finance store supported by background delivery.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
enum BackgroundDataType
```

#### Overview

When the finance store has changes to these types of data, any extensions registered for background delivery updates of them will be notified in accordance with their update frequency.

## Topics

### Operators
- [static func == (FinanceStore.BackgroundDataType, FinanceStore.BackgroundDataType) -> Bool](financestore/backgrounddatatype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [FinanceStore.BackgroundDataType.accountBalances](financestore/backgrounddatatype/accountbalances.md)
  Receive updates for changes to `AccountBalance`.
- [FinanceStore.BackgroundDataType.accounts](financestore/backgrounddatatype/accounts.md)
  Receive updates for changes to `Account`.
- [FinanceStore.BackgroundDataType.transactions](financestore/backgrounddatatype/transactions.md)
  Receive updates for changes to `Transaction`.
### Initializers
- [init(from: any Decoder) throws](financestore/backgrounddatatype/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](financestore/backgrounddatatype/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](financestore/backgrounddatatype/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](financestore/backgrounddatatype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](financestore/backgrounddatatype/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/backgrounddatatype)*