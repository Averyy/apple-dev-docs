# dataServiceIdentifierDidChange(_:)

**Framework**: Core Telephony  
**Kind**: method

Informs the delegate when the identifier changes for the service that’s currently providing data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func dataServiceIdentifierDidChange(_ identifier: String)
```

## Parameters

- `identifier`: The identifier of the service that’s currently providing data. Use this identifier as the key in   to get the value of the new radio access technology for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/cttelephonynetworkinfodelegate/dataserviceidentifierdidchange(_:))*