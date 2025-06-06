# PKStoredValuePassProperties

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that represents the properties of a pass that contains a balance used for specific transactions, such as a transit pass or loyalty card.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS ?+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class PKStoredValuePassProperties
```

## Topics

### Creating a stored-value pass properties object
- [convenience init?(for: PKPass)](pkstoredvaluepassproperties/init(for:).md)
  Creates a stored-value pass properties object for the specified pass.
### Reading the stored-value pass properties
- [var balances: [PKStoredValuePassBalance]](pkstoredvaluepassproperties/balances.md)
  The amount available for transactions for a service represented by a stored-value pass.
- [var expirationDate: Date?](pkstoredvaluepassproperties/expirationdate.md)
  The expiration date of a pass.
- [var isBlocked: Bool](pkstoredvaluepassproperties/isblocked.md)
  A Boolean value that indicates the pass issuer disabled a stored-value pass.
- [var isBlacklisted: Bool](pkstoredvaluepassproperties/isblacklisted.md)
  A Boolean value that indicates the pass issuer disabled a stored-value pass.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PKTransitPassProperties](pktransitpassproperties.md)
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
- [class PKStoredValuePassBalance](pkstoredvaluepassbalance.md)
  An object that represents a balance that’s available for transactions, such as points or money.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkstoredvaluepassproperties)*