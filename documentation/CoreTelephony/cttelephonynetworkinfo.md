# CTTelephonyNetworkInfo

**Framework**: Core Telephony  
**Kind**: class

An object that provides notifications of changes to the user’s cellular service provider.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CTTelephonyNetworkInfo
```

#### Overview

Your app should be able to handle changes to the user’s cellular service provider. For example, the user could swap the device’s SIM card with one from another provider while your app is running.

This class also gives you access to the [`CTCarrier`](ctcarrier.md) object, which contains information about the user’s home cellular service provider.

## Topics

### Getting Information About the Cellular Service Provider
- [var dataServiceIdentifier: String?](cttelephonynetworkinfo/dataserviceidentifier.md)
  The identifier of the service that’s currently providing data.
- [var delegate: (any CTTelephonyNetworkInfoDelegate)?](cttelephonynetworkinfo/delegate.md)
  An object that the system notifies when the data service identifier changes.
- [protocol CTTelephonyNetworkInfoDelegate](cttelephonynetworkinfodelegate.md)
  The methods that the system invokes when data service changes occur.
- [var serviceCurrentRadioAccessTechnology: [String : String]?](cttelephonynetworkinfo/servicecurrentradioaccesstechnology.md)
  A dictionary containing the current radio access technology registered to each service.
- [Radio Access Technology Constants](radio-access-technology-constants.md)
  Constants that describe the current radio access technology.
### Deprecated
- [var currentRadioAccessTechnology: String?](cttelephonynetworkinfo/currentradioaccesstechnology.md)
  The current radio access technology registered with the device.
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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo)*