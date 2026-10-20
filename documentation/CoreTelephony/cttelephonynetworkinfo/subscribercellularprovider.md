# subscriberCellularProvider

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

Information about the user’s cellular service provider.

**Availability**:
- iOS 4.0+ - Deprecated in 12.0
- iPadOS 4.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`serviceSubscriberCellularProviders`](./servicesubscribercellularproviders.md) instead.

## Declaration

```swift
var subscriberCellularProvider: CTCarrier? { get }
```

```objc
@property (retain, readonly, nullable) CTCarrier * subscriberCellularProvider;
```

#### Discussion

A [`CTCarrier`](../ctcarrier.md) object that contains information about the user’s home cellular service provider. The home provider is the provider with whom the user has an account. This information is available immediately after you allocate and initialize the [`CTTelephonyNetworkInfo`](../cttelephonynetworkinfo.md) object.

## See Also

### Deprecated
- [var currentRadioAccessTechnology: String?](./currentradioaccesstechnology.md)
  The current radio access technology registered with the device.
- [var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier) -> Void)?](./subscribercellularproviderdidupdatenotifier.md)
  A block dispatched when the user’s cellular service provider information changes.
- [var serviceSubscriberCellularProviders: [String : CTCarrier]?](./servicesubscribercellularproviders.md)
  A dictionary that contains carrier information about each service.
- [var serviceSubscriberCellularProvidersDidUpdateNotifier: ((String) -> Void)?](./servicesubscribercellularprovidersdidupdatenotifier.md)
  A block dispatched when there are updates to the user’s cellular provider information for any service.
- [static let CTRadioAccessTechnologyDidChange: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/ctradioaccesstechnologydidchange.md)
  The name of the notification indicating that the radio access technology changed for one of the services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/subscribercellularprovider)*