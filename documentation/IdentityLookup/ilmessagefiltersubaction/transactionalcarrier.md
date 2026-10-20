# ILMessageFilterSubAction.transactionalCarrier

**Framework**: SMS and Call Reporting  
**Kind**: case  
**Role**: Case

Prevents the system from showing the message normally, filtered as a Carrier message.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
case transactionalCarrier
```

```c
ILMessageFilterSubActionTransactionalCarrier
```

## See Also

### Transactional Subactions
- [ILMessageFilterSubAction.none](./none.md)
  Allows the system to show the message unfiltered due to insufficient information to determine an action.
- [ILMessageFilterSubAction.transactionalOthers](./transactionalothers.md)
  Prevents the system from showing the message normally, filtered as an Others message.
- [ILMessageFilterSubAction.transactionalFinance](./transactionalfinance.md)
  Prevents the system from showing the message normally, filtered as a Finance message.
- [ILMessageFilterSubAction.transactionalOrders](./transactionalorders.md)
  Prevents the system from showing the message normally, filtered as an Orders (eCommerce) message.
- [ILMessageFilterSubAction.transactionalReminders](./transactionalreminders.md)
  Prevents the system from showing the message normally, filtered as a Reminder message.
- [ILMessageFilterSubAction.transactionalHealth](./transactionalhealth.md)
  Prevents the system from showing the message normally, filtered as a Health message.
- [ILMessageFilterSubAction.transactionalWeather](./transactionalweather.md)
  Prevents the system from showing the message normally, filtered as a Weather message.
- [ILMessageFilterSubAction.transactionalRewards](./transactionalrewards.md)
  Prevents the system from showing the message normally, filtered as a Rewards message.
- [ILMessageFilterSubAction.transactionalPublicServices](./transactionalpublicservices.md)
  Prevents the system from showing the message normally, filtered as a Government message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefiltersubaction/transactionalcarrier)*