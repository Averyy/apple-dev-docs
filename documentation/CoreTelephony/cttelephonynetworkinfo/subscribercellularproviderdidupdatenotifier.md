# subscriberCellularProviderDidUpdateNotifier

**Framework**: Core Telephony  
**Kind**: property

A block dispatched when the user’s cellular service provider information changes.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier) -> Void)? { get set }
```

#### Discussion

This block executes on the default priority global dispatch queue when the user’s cellular provider information changes. This occurs, for example, if a user swaps the device’s SIM card with one from another provider, while your app is running.

To handle changes in cellular service provider information, define a block in your app and assign it to this property. Implement the block to support being called from any context.

## See Also

- [var currentRadioAccessTechnology: String?](cttelephonynetworkinfo/currentradioaccesstechnology.md)
  The current radio access technology registered with the device.
- [var subscriberCellularProvider: CTCarrier?](cttelephonynetworkinfo/subscribercellularprovider.md)
  Information about the user’s cellular service provider.
- [var serviceSubscriberCellularProviders: [String : CTCarrier]?](cttelephonynetworkinfo/servicesubscribercellularproviders.md)
  A dictionary that contains carrier information about each service.
- [var serviceSubscriberCellularProvidersDidUpdateNotifier: ((String) -> Void)?](cttelephonynetworkinfo/servicesubscribercellularprovidersdidupdatenotifier.md)
  A block dispatched when there are updates to the user’s cellular provider information for any service.
- [static let CTRadioAccessTechnologyDidChange: NSNotification.Name](../foundation/nsnotification/name/1616908-ctradioaccesstechnologydidchange.md)
  The name of the notification indicating that the radio access technology changed for one of the services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/subscribercellularproviderdidupdatenotifier)*