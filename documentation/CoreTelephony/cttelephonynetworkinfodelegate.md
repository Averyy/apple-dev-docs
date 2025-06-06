# CTTelephonyNetworkInfoDelegate

**Framework**: Core Telephony  
**Kind**: protocol

The methods that the system invokes when data service changes occur.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol CTTelephonyNetworkInfoDelegate : NSObjectProtocol
```

## Topics

### Responding to Data Service Changes
- [func dataServiceIdentifierDidChange(String)](cttelephonynetworkinfodelegate/dataserviceidentifierdidchange(_:).md)
  Informs the delegate when the identifier changes for the service that’s currently providing data.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var dataServiceIdentifier: String?](cttelephonynetworkinfo/dataserviceidentifier.md)
  The identifier of the service that’s currently providing data.
- [var delegate: (any CTTelephonyNetworkInfoDelegate)?](cttelephonynetworkinfo/delegate.md)
  An object that the system notifies when the data service identifier changes.
- [var serviceCurrentRadioAccessTechnology: [String : String]?](cttelephonynetworkinfo/servicecurrentradioaccesstechnology.md)
  A dictionary containing the current radio access technology registered to each service.
- [Radio Access Technology Constants](radio-access-technology-constants.md)
  Constants that describe the current radio access technology.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfodelegate)*