# adCampaignIdentifier

**Framework**: StoreKit Test  
**Kind**: property

A number that represents the advertising network’s campaign.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var adCampaignIdentifier: Int { get }
```

#### Discussion

Ad networks set their own campaign identifiers, which must be an integer between 1 and 100.

## See Also

- [var conversionValue: Int](skadtestpostback/conversionvalue.md)
  An unsigned 6-bit value that the app or ad network controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestpostback/adcampaignidentifier)*