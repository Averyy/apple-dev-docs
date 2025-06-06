# serviceSubscriberCellularProvidersDidUpdateNotifier

**Framework**: Core Telephony  
**Kind**: property

A block dispatched when there are updates to the user’s cellular provider information for any service.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var serviceSubscriberCellularProvidersDidUpdateNotifier: ((String) -> Void)? { get set }
```

#### Discussion

The block object executes on the default priority global dispatch queue when the user’s cellular provider information changes. This occurs, for example, if a user swaps the device’s SIM card with one from another provider, while your app is running.

To handle changes in cellular service provider information, define a block in your app and assign it to this property. Implement the block to support being called from any context. To get the new information, use the [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) (which contains the identifier of the service whose information has changed) as the key into [`serviceSubscriberCellularProviders`](cttelephonynetworkinfo/servicesubscribercellularproviders.md).

## See Also

- [var currentRadioAccessTechnology: String?](cttelephonynetworkinfo/currentradioaccesstechnology.md)
  The current radio access technology registered with the device.
- [var subscriberCellularProvider: CTCarrier?](cttelephonynetworkinfo/subscribercellularprovider.md)
  Information about the user’s cellular service provider.
- [var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier) -> Void)?](cttelephonynetworkinfo/subscribercellularproviderdidupdatenotifier.md)
  A block dispatched when the user’s cellular service provider information changes.
- [var serviceSubscriberCellularProviders: [String : CTCarrier]?](cttelephonynetworkinfo/servicesubscribercellularproviders.md)
  A dictionary that contains carrier information about each service.
- [static let CTRadioAccessTechnologyDidChange: NSNotification.Name](../foundation/nsnotification/name/1616908-ctradioaccesstechnologydidchange.md)
  The name of the notification indicating that the radio access technology changed for one of the services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/servicesubscribercellularprovidersdidupdatenotifier)*