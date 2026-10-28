# serviceSubscriberCellularProvidersDidUpdateNotifier

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

A block dispatched when there are updates to the user’s cellular provider information for any service.

**Availability**:
- iOS 12.0+ - Deprecated in 16.0
- iPadOS 12.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0

> **Deprecated**: Deprecated with no replacement

## Declaration

```swift
var serviceSubscriberCellularProvidersDidUpdateNotifier: ((String) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^serviceSubscriberCellularProvidersDidUpdateNotifier)(NSString *);
```

## Discussion

The block object executes on the default priority global dispatch queue when the user’s cellular provider information changes. This occurs, for example, if a user swaps the device’s SIM card with one from another provider, while your app is running.

To handle changes in cellular service provider information, define a block in your app and assign it to this property. Implement the block to support being called from any context. To get the new information, use the [`NSString`](../../Foundation/nsstring.md) (which contains the identifier of the service whose information has changed) as the key into [`serviceSubscriberCellularProviders`](./servicesubscribercellularproviders.md).

## See Also

### Deprecated
- [var currentRadioAccessTechnology: String?](./currentradioaccesstechnology.md)
  The current radio access technology registered with the device.
- [var subscriberCellularProvider: CTCarrier?](./subscribercellularprovider.md)
  Information about the user’s cellular service provider.
- [var subscriberCellularProviderDidUpdateNotifier: ((CTCarrier) -> Void)?](./subscribercellularproviderdidupdatenotifier.md)
  A block dispatched when the user’s cellular service provider information changes.
- [var serviceSubscriberCellularProviders: [String : CTCarrier]?](./servicesubscribercellularproviders.md)
  A dictionary that contains carrier information about each service.
- [static let CTRadioAccessTechnologyDidChange: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/ctradioaccesstechnologydidchange.md)
  The name of the notification indicating that the radio access technology changed for one of the services.
- [CTServiceRadioAccessTechnologyDidChangeNotification](../ctserviceradioaccesstechnologydidchangenotification.md)
- [CTRadioAccessTechnologyDidChangeNotification](../ctradioaccesstechnologydidchangenotification.md)
  The name of the notification indicating that the radio access technology changed for one of the services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/servicesubscribercellularprovidersdidupdatenotifier)*