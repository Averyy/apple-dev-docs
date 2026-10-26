# CTRadioAccessTechnologyDidChangeNotification

**Framework**: Core Telephony  
**Kind**: var  
**Role**: Global Variable

The name of the notification indicating that the radio access technology changed for one of the services.

**Availability**:
- iOS 7.0+ - Deprecated in 12.0
- iPadOS 7.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```c
extern NSString * const CTRadioAccessTechnologyDidChangeNotification;
```

#### Discussion

The notification’s [`object`](../Foundation/nsnotification/object.md) is an [`NSString`](../Foundation/nsstring.md) that represents the service identifier of the service whose radio access technology has changed. Use this string as the key in [`serviceCurrentRadioAccessTechnology`](./cttelephonynetworkinfo/servicecurrentradioaccesstechnology.md) to get the value of the new radio access technology for the service.

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
- [CTServiceRadioAccessTechnologyDidChangeNotification](./ctserviceradioaccesstechnologydidchangenotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctradioaccesstechnologydidchangenotification)*