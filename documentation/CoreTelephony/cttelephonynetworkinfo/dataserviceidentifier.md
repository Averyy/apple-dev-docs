# dataServiceIdentifier

**Framework**: Core Telephony  
**Kind**: property

The identifier of the service that’s currently providing data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var dataServiceIdentifier: String? { get }
```

## See Also

- [var delegate: (any CTTelephonyNetworkInfoDelegate)?](cttelephonynetworkinfo/delegate.md)
  An object that the system notifies when the data service identifier changes.
- [protocol CTTelephonyNetworkInfoDelegate](cttelephonynetworkinfodelegate.md)
  The methods that the system invokes when data service changes occur.
- [var serviceCurrentRadioAccessTechnology: [String : String]?](cttelephonynetworkinfo/servicecurrentradioaccesstechnology.md)
  A dictionary containing the current radio access technology registered to each service.
- [Radio Access Technology Constants](radio-access-technology-constants.md)
  Constants that describe the current radio access technology.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/dataserviceidentifier)*