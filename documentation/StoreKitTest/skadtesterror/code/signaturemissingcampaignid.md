# SKAdTestError.Code.signatureMissingCampaignId

**Framework**: StoreKit Test  
**Kind**: case

The signature is missing the campaign identifier, in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
case signatureMissingCampaignId
```

#### Discussion

Be sure to include the campaign identifier when you create and validate an ad impression in the testing environment.

## See Also

- [SKAdTestError.Code.invalidCampaignId](skadtesterror/code/invalidcampaignid.md)
  The campaign ID isn’t an integer between one and one hundred.
- [SKAdTestError.Code.conflictingSource](skadtesterror/code/conflictingsource.md)
  This error code is unused.
- [SKAdTestError.Code.invalidCampaignId](skadtesterror/code/invalidcampaignid.md)
  The campaign ID isn’t an integer between one and one hundred.
- [SKAdTestError.Code.conflictingSource](skadtesterror/code/conflictingsource.md)
  This error code is unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/code/signaturemissingcampaignid)*