# invalidCampaignId

**Framework**: StoreKit Test  
**Kind**: property

The campaign ID isn’t an integer between one and one hundred.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
static var invalidCampaignId: SKAdTestError.Code { get }
```

#### Discussion

A campaign ID is an integer that is greater than or equal to one and less than or equal to one hundred.

## See Also

- [static var signatureMissingCampaignId: SKAdTestError.Code](skadtesterror/signaturemissingcampaignid.md)
  The signature is missing the campaign identifier, in the testing environment.
- [static var conflictingSource: SKAdTestError.Code](skadtesterror/conflictingsource.md)
  This error code is unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/invalidcampaignid)*