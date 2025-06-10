# currentRadioAccessTechnology

**Framework**: Core Telephony  
**Kind**: property

The current radio access technology registered with the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var currentRadioAccessTechnology: String? { get }
```

#### Discussion

If the device isn’t registered on any network, this property is `nil`.

## See Also

- [var subscriberCellularProvider: CTCarrier?](cttelephonynetworkinfo/subscribercellularprovider.md)
  Information about the user’s cellular service provider.
- [var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier) -> Void)?](cttelephonynetworkinfo/subscribercellularproviderdidupdatenotifier.md)
  A block dispatched when the user’s cellular service provider information changes.
- [var serviceSubscriberCellularProviders: [String : CTCarrier]?](cttelephonynetworkinfo/servicesubscribercellularproviders.md)
  A dictionary that contains carrier information about each service.
- [var serviceSubscriberCellularProvidersDidUpdateNotifier: ((String) -> Void)?](cttelephonynetworkinfo/servicesubscribercellularprovidersdidupdatenotifier.md)
  A block dispatched when there are updates to the user’s cellular provider information for any service.
- [static let CTRadioAccessTechnologyDidChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/CTRadioAccessTechnologyDidChange.md)
  The name of the notification indicating that the radio access technology changed for one of the services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/currentradioaccesstechnology)*