# PKTransitPassProperties

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

The properties of a transit pass.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 4.3+

## Declaration

```swift
class PKTransitPassProperties
```

## Topics

### Getting pass status
- [var expirationDate: Date?](pktransitpassproperties/expirationdate.md)
  The date that the transit card expires.
- [var isInStation: Bool](pktransitpassproperties/isinstation.md)
  A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.
- [var isBlocked: Bool](pktransitpassproperties/isblocked.md)
  A Boolean value that indicates the pass issuer disabled the pass.
- [var isBlacklisted: Bool](pktransitpassproperties/isblacklisted.md)
  A Boolean value that indicates the transit pass issuer disabled the pass.
### Getting balance information
- [var transitBalance: NSDecimalNumber](pktransitpassproperties/transitbalance.md)
  The current usable stored value on the transit card.
- [var transitBalanceCurrencyCode: String](pktransitpassproperties/transitbalancecurrencycode.md)
  The currency code associated with the balance on the pass.

## Relationships

### Inherits From
- [PKStoredValuePassProperties](pkstoredvaluepassproperties.md)
### Inherited By
- [PKSuicaPassProperties](pksuicapassproperties.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKSuicaPassProperties](pksuicapassproperties.md)
  The properties of a pass used as a ticket for the Suica transportation system.
- [class PKStoredValuePassProperties](pkstoredvaluepassproperties.md)
  An object that represents the properties of a pass that contains a balance used for specific transactions, such as a transit pass or loyalty card.
- [class PKStoredValuePassBalance](pkstoredvaluepassbalance.md)
  An object that represents a balance that’s available for transactions, such as points or money.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pktransitpassproperties)*