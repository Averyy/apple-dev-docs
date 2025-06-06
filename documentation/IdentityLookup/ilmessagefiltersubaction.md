# ILMessageFilterSubAction

**Framework**: SMS and Call Reporting  
**Kind**: enum

Responds to a received message with a filter subaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum ILMessageFilterSubAction
```

## Topics

### Transactional Subactions
- [ILMessageFilterSubAction.none](ilmessagefiltersubaction/none.md)
  Allows the system to show the message unfiltered due to insufficient information to determine an action.
- [ILMessageFilterSubAction.transactionalOthers](ilmessagefiltersubaction/transactionalothers.md)
  Prevents the system from showing the message normally, filtered as an Others message.
- [ILMessageFilterSubAction.transactionalFinance](ilmessagefiltersubaction/transactionalfinance.md)
  Prevents the system from showing the message normally, filtered as a Finance message.
- [ILMessageFilterSubAction.transactionalOrders](ilmessagefiltersubaction/transactionalorders.md)
  Prevents the system from showing the message normally, filtered as an Orders (eCommerce) message.
- [ILMessageFilterSubAction.transactionalReminders](ilmessagefiltersubaction/transactionalreminders.md)
  Prevents the system from showing the message normally, filtered as a Reminder message.
- [ILMessageFilterSubAction.transactionalHealth](ilmessagefiltersubaction/transactionalhealth.md)
  Prevents the system from showing the message normally, filtered as a Health message.
- [ILMessageFilterSubAction.transactionalWeather](ilmessagefiltersubaction/transactionalweather.md)
  Prevents the system from showing the message normally, filtered as a Weather message.
- [ILMessageFilterSubAction.transactionalCarrier](ilmessagefiltersubaction/transactionalcarrier.md)
  Prevents the system from showing the message normally, filtered as a Carrier message.
- [ILMessageFilterSubAction.transactionalRewards](ilmessagefiltersubaction/transactionalrewards.md)
  Prevents the system from showing the message normally, filtered as a Rewards message.
- [ILMessageFilterSubAction.transactionalPublicServices](ilmessagefiltersubaction/transactionalpublicservices.md)
  Prevents the system from showing the message normally, filtered as a Government message.
### Promotional Subactions
- [ILMessageFilterSubAction.promotionalOthers](ilmessagefiltersubaction/promotionalothers.md)
  Prevents the system from showing the message normally, filtered as an Others message.
- [ILMessageFilterSubAction.promotionalOffers](ilmessagefiltersubaction/promotionaloffers.md)
  Prevents the system from showing the message normally, filtered as an Offers message.
- [ILMessageFilterSubAction.promotionalCoupons](ilmessagefiltersubaction/promotionalcoupons.md)
  Prevents the system from showing the message normally, filtered as an Coupons message.
### Initializers
- [init?(rawValue: Int)](ilmessagefiltersubaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class ILMessageFilterCapabilitiesQueryResponse](ilmessagefiltercapabilitiesqueryresponse.md)
  A response to a message filter capabilities query request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefiltersubaction)*