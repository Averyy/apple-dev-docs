# serviceSubscriberCellularProviders

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

A dictionary that contains carrier information about each service.

**Availability**:
- iOS 12.0+ - Deprecated in 16.0
- iPadOS 12.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0

> **Deprecated**: Deprecated with no replacement

## Declaration

```swift
var serviceSubscriberCellularProviders: [String : CTCarrier]? { get }
```

```objc
@property (retain, readonly, nullable) NSDictionary<NSString *,CTCarrier *> * serviceSubscriberCellularProviders;
```

## Discussion

The keys for the [`serviceSubscriberCellularProviders`](./servicesubscribercellularproviders.md) dictionary are [`NSString`](../../Foundation/nsstring.md) objects, each of which represents a service. Each entry in the dictionary is a [`CTCarrier`](../ctcarrier.md) object, which contains information about the subscriber’s home cellular service provider.

> **Note**:  In this context, the “home” provider is the one with which the user has a cellular plan, as opposed to a roaming provider.

Although the actual value of a key isn’t important, you can also use it to get the current radio access technology associated with the service. To do so, pass the key to the [`serviceCurrentRadioAccessTechnology`](./servicecurrentradioaccesstechnology.md) dictionary.

## See Also

### Deprecated
- [var currentRadioAccessTechnology: String?](./currentradioaccesstechnology.md)
  The current radio access technology registered with the device.
- [var subscriberCellularProvider: CTCarrier?](./subscribercellularprovider.md)
  Information about the user’s cellular service provider.
- [var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier) -> Void)?](./subscribercellularproviderdidupdatenotifier.md)
  A block dispatched when the user’s cellular service provider information changes.
- [var serviceSubscriberCellularProvidersDidUpdateNotifier: ((String) -> Void)?](./servicesubscribercellularprovidersdidupdatenotifier.md)
  A block dispatched when there are updates to the user’s cellular provider information for any service.
- [static let CTRadioAccessTechnologyDidChange: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/ctradioaccesstechnologydidchange.md)
  The name of the notification indicating that the radio access technology changed for one of the services.
- [CTServiceRadioAccessTechnologyDidChangeNotification](../ctserviceradioaccesstechnologydidchangenotification.md)
- [CTRadioAccessTechnologyDidChangeNotification](../ctradioaccesstechnologydidchangenotification.md)
  The name of the notification indicating that the radio access technology changed for one of the services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/servicesubscribercellularproviders)*