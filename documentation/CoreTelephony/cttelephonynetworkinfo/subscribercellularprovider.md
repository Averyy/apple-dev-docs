# subscriberCellularProvider

**Framework**: Core Telephony  
**Kind**: property

Information about the user’s cellular service provider.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var subscriberCellularProvider: CTCarrier? { get }
```

#### Discussion

A [`CTCarrier`](ctcarrier.md) object that contains information about the user’s home cellular service provider. The home provider is the provider with whom the user has an account. This information is available immediately after you allocate and initialize the [`CTTelephonyNetworkInfo`](cttelephonynetworkinfo.md) object.

## See Also

- [var currentRadioAccessTechnology: String?](cttelephonynetworkinfo/currentradioaccesstechnology.md)
  The current radio access technology registered with the device.
- [var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier) -> Void)?](cttelephonynetworkinfo/subscribercellularproviderdidupdatenotifier.md)
  A block dispatched when the user’s cellular service provider information changes.
- [var serviceSubscriberCellularProviders: [String : CTCarrier]?](cttelephonynetworkinfo/servicesubscribercellularproviders.md)
  A dictionary that contains carrier information about each service.
- [var serviceSubscriberCellularProvidersDidUpdateNotifier: ((String) -> Void)?](cttelephonynetworkinfo/servicesubscribercellularprovidersdidupdatenotifier.md)
  A block dispatched when there are updates to the user’s cellular provider information for any service.
- [static let CTRadioAccessTechnologyDidChange: NSNotification.Name](../foundation/nsnotification/name/1616908-ctradioaccesstechnologydidchange.md)
  The name of the notification indicating that the radio access technology changed for one of the services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/subscribercellularprovider)*