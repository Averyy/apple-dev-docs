# ILMessageFilterSubAction.none

**Framework**: SMS and Call Reporting  
**Kind**: case

Allows the system to show the message unfiltered due to insufficient information to determine an action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
case none
```

#### Discussion

In a query response, setting this value allows the system to show the message unfiltered.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitylookup/ilmessagefiltersubaction/none)*