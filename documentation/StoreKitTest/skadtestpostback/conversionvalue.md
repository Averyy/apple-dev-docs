# conversionValue

**Framework**: StoreKit Test  
**Kind**: property

An unsigned 6-bit value that the app or ad network controls.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var conversionValue: Int { get }
```

#### Discussion

A postback in SKAdNetwork 3 or earlier uses a single [`conversionValue`](skadtestpostback/conversionvalue.md). A postback in SKAdNetwork 4 or later may contain either a [`fineConversionValue`](skadtestpostback/fineconversionvalue.md) or a [`coarseConversionValue`](skadtestpostback/coarseconversionvalue.md).

## See Also

- [var adCampaignIdentifier: Int](skadtestpostback/adcampaignidentifier.md)
  A number that represents the advertising network’s campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/conversionvalue)*