# PKSuicaPassProperties

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

The properties of a pass used as a ticket for the Suica transportation system.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 3.1+

## Declaration

```swift
class PKSuicaPassProperties
```

#### Overview

The Suica pass is a card used for transportation in Japan.

## Topics

### Initializing suica pass properties
- [convenience init?(for: PKPass)](pksuicapassproperties/init(for:).md)
  Instantiates a Suica pass properties object that contains the properties supported in the specified pass.
### Getting pass status
- [var isBlocked: Bool](pksuicapassproperties/isblocked.md)
  A Boolean value that indicates whether the pass issuer disabled the pass.
- [var isBlacklisted: Bool](pksuicapassproperties/isblacklisted.md)
  A Boolean value that indicates whether the transit pass issuer disabled the pass.
- [var isGreenCarTicketUsed: Bool](pksuicapassproperties/isgreencarticketused.md)
  A Boolean value that indicates whether the customer has redeemed the Green Car ticket.
- [var isInShinkansenStation: Bool](pksuicapassproperties/isinshinkansenstation.md)
  A Boolean value that indicates whether the pass has tapped in at a Shinkansen Station and has not tapped out.
- [var isInStation: Bool](pksuicapassproperties/isinstation.md)
  A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.
### Getting suica balance information
- [var transitBalance: NSDecimalNumber](pksuicapassproperties/transitbalance.md)
  The current usable stored value on the transit card.
- [var transitBalanceCurrencyCode: String](pksuicapassproperties/transitbalancecurrencycode.md)
  The currency code associated with the balance on the pass.
- [var isBalanceAllowedForCommute: Bool](pksuicapassproperties/isbalanceallowedforcommute.md)
  A Boolean value that indicates how the balance can be used.
- [var isLowBalanceGateNotificationEnabled: Bool](pksuicapassproperties/islowbalancegatenotificationenabled.md)
  A Boolean value that determines whether the terminal provides feedback if the balance is low after a deduction.

## Relationships

### Inherits From
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
- [class PKStoredValuePassProperties](pkstoredvaluepassproperties.md)
  An object that represents the properties of a pass that contains a balance used for specific transactions, such as a transit pass or loyalty card.
- [class PKStoredValuePassBalance](pkstoredvaluepassbalance.md)
  An object that represents a balance that’s available for transactions, such as points or money.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksuicapassproperties)*