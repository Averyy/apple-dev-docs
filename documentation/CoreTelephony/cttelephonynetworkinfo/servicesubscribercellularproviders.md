# serviceSubscriberCellularProviders

**Framework**: Core Telephony  
**Kind**: property

A dictionary that contains carrier information about each service.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var serviceSubscriberCellularProviders: [String : CTCarrier]? { get }
```

#### Discussion

The keys for the [`serviceSubscriberCellularProviders`](cttelephonynetworkinfo/servicesubscribercellularproviders.md) dictionary are [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects, each of which represents a service. Each entry in the dictionary is a [`CTCarrier`](ctcarrier.md) object, which contains information about the subscriber’s home cellular service provider.

> **Note**:  In this context, the “home” provider is the one with which the user has a cellular plan, as opposed to a roaming provider.

 In this context, the “home” provider is the one with which the user has a cellular plan, as opposed to a roaming provider.

Although the actual value of a key isn’t important, you can also use it to get the current radio access technology associated with the service. To do so, pass the key to the [`serviceCurrentRadioAccessTechnology`](cttelephonynetworkinfo/servicecurrentradioaccesstechnology.md) dictionary.

## See Also

- [var currentRadioAccessTechnology: String?](cttelephonynetworkinfo/currentradioaccesstechnology.md)
  The current radio access technology registered with the device.
- [var subscriberCellularProvider: CTCarrier?](cttelephonynetworkinfo/subscribercellularprovider.md)
  Information about the user’s cellular service provider.
- [var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier) -> Void)?](cttelephonynetworkinfo/subscribercellularproviderdidupdatenotifier.md)
  A block dispatched when the user’s cellular service provider information changes.
- [var serviceSubscriberCellularProvidersDidUpdateNotifier: ((String) -> Void)?](cttelephonynetworkinfo/servicesubscribercellularprovidersdidupdatenotifier.md)
  A block dispatched when there are updates to the user’s cellular provider information for any service.
- [static let CTRadioAccessTechnologyDidChange: NSNotification.Name](../foundation/nsnotification/name/1616908-ctradioaccesstechnologydidchange.md)
  The name of the notification indicating that the radio access technology changed for one of the services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/servicesubscribercellularproviders)*