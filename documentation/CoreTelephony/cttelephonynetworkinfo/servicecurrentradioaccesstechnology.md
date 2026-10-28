# serviceCurrentRadioAccessTechnology

**Framework**: Core Telephony  
**Kind**: property  
**Role**: Instance Property

A dictionary containing the current radio access technology registered to each service.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var serviceCurrentRadioAccessTechnology: [String : String]? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) NSDictionary<NSString *,NSString *> * serviceCurrentRadioAccessTechnology;
```

## Discussion

The keys for the [`serviceCurrentRadioAccessTechnology`](./servicecurrentradioaccesstechnology.md) dictionary are [`NSString`](../../Foundation/nsstring.md) objects, each of which represents a service. The entry associated with a key is `nil` if the service is not registered on any network.

Although the actual value of a key isn’t important, you can also use it to get the carrier information associated with the service. To do so, pass the key to the [`serviceSubscriberCellularProviders`](./servicesubscribercellularproviders.md) dictionary.

## See Also

### Getting Information About the Cellular Service Provider
- [var dataServiceIdentifier: String?](./dataserviceidentifier.md)
  The identifier of the service that’s currently providing data.
- [var delegate: (any CTTelephonyNetworkInfoDelegate)?](./delegate.md)
  An object that the system notifies when the data service identifier changes.
- [protocol CTTelephonyNetworkInfoDelegate](../cttelephonynetworkinfodelegate.md)
  The methods that the system invokes when data service changes occur.
- [Radio Access Technology Constants](../radio-access-technology-constants.md)
  Constants that describe the current radio access technology.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/servicecurrentradioaccesstechnology)*