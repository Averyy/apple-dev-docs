# signatureMissingCampaignId

**Framework**: StoreKit Test  
**Kind**: property

The signature is missing the campaign identifier, in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
static var signatureMissingCampaignId: SKAdTestError.Code { get }
```

#### Discussion

Be sure to include the campaign identifier when you create and validate an ad impression in the testing environment.

## See Also

- [static var invalidCampaignId: SKAdTestError.Code](skadtesterror/invalidcampaignid.md)
  The campaign ID isn’t an integer between one and one hundred.
- [static var conflictingSource: SKAdTestError.Code](skadtesterror/conflictingsource.md)
  This error code is unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/signaturemissingcampaignid)*