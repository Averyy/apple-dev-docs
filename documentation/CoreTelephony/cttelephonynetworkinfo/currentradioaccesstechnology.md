# currentRadioAccessTechnology

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

The current radio access technology registered with the device.

**Availability**:
- iOS 7.0+ - Deprecated in 12.0
- iPadOS 7.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`serviceCurrentRadioAccessTechnology`](./servicecurrentradioaccesstechnology.md) instead.

## Declaration

```swift
var currentRadioAccessTechnology: String? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) NSString * currentRadioAccessTechnology;
```

## Discussion

If the device isn’t registered on any network, this property is `nil`.

## See Also

### Deprecated
- [var subscriberCellularProvider: CTCarrier?](./subscribercellularprovider.md)
  Information about the user’s cellular service provider.
- [var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier) -> Void)?](./subscribercellularproviderdidupdatenotifier.md)
  A block dispatched when the user’s cellular service provider information changes.
- [var serviceSubscriberCellularProviders: [String : CTCarrier]?](./servicesubscribercellularproviders.md)
  A dictionary that contains carrier information about each service.
- [var serviceSubscriberCellularProvidersDidUpdateNotifier: ((String) -> Void)?](./servicesubscribercellularprovidersdidupdatenotifier.md)
  A block dispatched when there are updates to the user’s cellular provider information for any service.
- [static let CTRadioAccessTechnologyDidChange: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/ctradioaccesstechnologydidchange.md)
  The name of the notification indicating that the radio access technology changed for one of the services.
- [CTServiceRadioAccessTechnologyDidChangeNotification](../ctserviceradioaccesstechnologydidchangenotification.md)
- [CTRadioAccessTechnologyDidChangeNotification](../ctradioaccesstechnologydidchangenotification.md)
  The name of the notification indicating that the radio access technology changed for one of the services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/currentradioaccesstechnology)*