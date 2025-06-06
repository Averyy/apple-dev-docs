# PKStoredValuePassBalance

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that represents a balance that’s available for transactions, such as points or money.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS ?+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class PKStoredValuePassBalance
```

#### Overview

> ❗ **Important**:  A stored balance of type of [`cash`](pkstoredvaluepassbalance/balancetype-swift.struct/cash.md) requires a valid currency code.

 A stored balance of type of [`cash`](pkstoredvaluepassbalance/balancetype-swift.struct/cash.md) requires a valid currency code.

## Topics

### Getting the pass status
- [var expiryDate: Date?](pkstoredvaluepassbalance/expirydate.md)
  The date that the balance expires.
- [var amount: Decimal](pkstoredvaluepassbalance/amount-2nwf5.md)
  The current balance of a stored-value pass in money or points.
- [var balanceType: PKStoredValuePassBalance.BalanceType](pkstoredvaluepassbalance/balancetype-swift.property.md)
  The type of value that the balance represents, such as money or points.
- [var currencyCode: String?](pkstoredvaluepassbalance/currencycode.md)
  The ISO 4217 currency code of the balance.
- [PKStoredValuePassBalance.BalanceType](pkstoredvaluepassbalance/balancetype-swift.struct.md)
  The type of value that the balance represents, such as money or points.
### Comparing pass balance objects
- [static func == (PKStoredValuePassBalance, PKStoredValuePassBalance) -> Bool](pkstoredvaluepassbalance/==(_:_:).md)
  Returns a Boolean value that indicates whether two pass balance objects contain the same values.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKTransitPassProperties](pktransitpassproperties.md)
  The properties of a transit pass.
- [class PKSuicaPassProperties](pksuicapassproperties.md)
  The properties of a pass used as a ticket for the Suica transportation system.
- [class PKStoredValuePassProperties](pkstoredvaluepassproperties.md)
  An object that represents the properties of a pass that contains a balance used for specific transactions, such as a transit pass or loyalty card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkstoredvaluepassbalance)*