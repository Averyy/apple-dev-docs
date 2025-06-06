# delegate

**Framework**: Core Telephony  
**Kind**: property

An object that the system notifies when the data service identifier changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
weak var delegate: (any CTTelephonyNetworkInfoDelegate)? { get set }
```

## See Also

- [var dataServiceIdentifier: String?](cttelephonynetworkinfo/dataserviceidentifier.md)
  The identifier of the service that’s currently providing data.
- [protocol CTTelephonyNetworkInfoDelegate](cttelephonynetworkinfodelegate.md)
  The methods that the system invokes when data service changes occur.
- [var serviceCurrentRadioAccessTechnology: [String : String]?](cttelephonynetworkinfo/servicecurrentradioaccesstechnology.md)
  A dictionary containing the current radio access technology registered to each service.
- [Radio Access Technology Constants](radio-access-technology-constants.md)
  Constants that describe the current radio access technology.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfo/delegate)*