# CTServiceRadioAccessTechnologyDidChangeNotification

**Framework**: Core Telephony  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```c
extern NSString * const CTServiceRadioAccessTechnologyDidChangeNotification;
```

## See Also

### Deprecated
- [var currentRadioAccessTechnology: String?](./cttelephonynetworkinfo/currentradioaccesstechnology.md)
  The current radio access technology registered with the device.
- [var subscriberCellularProvider: CTCarrier?](./cttelephonynetworkinfo/subscribercellularprovider.md)
  Information about the user’s cellular service provider.
- [var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier) -> Void)?](./cttelephonynetworkinfo/subscribercellularproviderdidupdatenotifier.md)
  A block dispatched when the user’s cellular service provider information changes.
- [var serviceSubscriberCellularProviders: [String : CTCarrier]?](./cttelephonynetworkinfo/servicesubscribercellularproviders.md)
  A dictionary that contains carrier information about each service.
- [var serviceSubscriberCellularProvidersDidUpdateNotifier: ((String) -> Void)?](./cttelephonynetworkinfo/servicesubscribercellularprovidersdidupdatenotifier.md)
  A block dispatched when there are updates to the user’s cellular provider information for any service.
- [CTRadioAccessTechnologyDidChangeNotification](./ctradioaccesstechnologydidchangenotification.md)
  The name of the notification indicating that the radio access technology changed for one of the services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctserviceradioaccesstechnologydidchangenotification)*