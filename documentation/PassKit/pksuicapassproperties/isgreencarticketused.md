# isGreenCarTicketUsed

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the customer has redeemed the Green Car ticket.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 3.1+

## Declaration

```swift
var isGreenCarTicketUsed: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isGreenCarTicketUsed) BOOL greenCarTicketUsed;
```

#### Discussion

A Green Car ticket is valid for a single use. This flag indicates the ticket has been used and is not eligible for a refund.

## See Also

### Getting pass status
- [var isBlocked: Bool](./isblocked.md)
  A Boolean value that indicates whether the pass issuer disabled the pass.
- [var isBlacklisted: Bool](./isblacklisted.md)
  A Boolean value that indicates whether the transit pass issuer disabled the pass.
- [var isInShinkansenStation: Bool](./isinshinkansenstation.md)
  A Boolean value that indicates whether the pass has tapped in at a Shinkansen Station and has not tapped out.
- [var isInStation: Bool](./isinstation.md)
  A Boolean value that indicates whether the transit pass has tapped in at a station and has not tapped out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksuicapassproperties/isgreencarticketused)*