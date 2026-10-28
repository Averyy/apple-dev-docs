# conversionValue

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

An unsigned 6-bit value that the app or ad network controls.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var conversionValue: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger conversionValue;
```

## Discussion

A postback in SKAdNetwork 3 or earlier uses a single [`conversionValue`](./conversionvalue.md). A postback in SKAdNetwork 4 or later may contain either a [`fineConversionValue`](./fineconversionvalue.md) or a [`coarseConversionValue`](./coarseconversionvalue.md).

## See Also

### Getting information in earlier versions
- [var adCampaignIdentifier: Int](./adcampaignidentifier.md)
  A number that represents the advertising network’s campaign.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/conversionvalue)*