# init(fineConversionValue:lockPostback:coarseConversionValue:conversionTypes:)

**Framework**: AdAttributionKit  
**Kind**: init

Creates a new postback update with the conversions values, conversion types, and lock indication you provide.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+

## Declaration

```swift
init(fineConversionValue: Int, lockPostback: Bool, coarseConversionValue: CoarseConversionValue? = nil, conversionTypes: [PostbackUpdate.ConversionType]? = nil)
```

## Parameters

- `fineConversionValue`: An integer that represents the fine conversion value.
- `lockPostback`: A Boolean value that indicates whether the system can lock the postback, reducing the system time   to deliver a signal.
- `coarseConversionValue`: An optional   enumeration value that represents the   coarse conversion value. Defaults to  .
- `conversionTypes`: An optional array of conversion types the system uses to determine which postbacks to update.   Defaults to   and the system updates all types of postbacks by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adattributionkit/postbackupdate/init(fineconversionvalue:lockpostback:coarseconversionvalue:conversiontypes:))*