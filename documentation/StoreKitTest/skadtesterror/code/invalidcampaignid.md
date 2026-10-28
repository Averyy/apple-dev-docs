# SKAdTestError.Code.invalidCampaignId

**Framework**: StoreKit Test  
**Kind**: case  
**Role**: Case

The campaign ID isn’t an integer between one and one hundred.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
case invalidCampaignId
```

```c
SKAdTestErrorCodeInvalidCampaignId
```

## Discussion

A campaign ID is an integer that is greater than or equal to one and less than or equal to one hundred.

## See Also

### Older Errors
- [SKAdTestError.Code.signatureMissingCampaignId](./signaturemissingcampaignid.md)
  The signature is missing the campaign identifier, in the testing environment.
- [SKAdTestError.Code.conflictingSource](./conflictingsource.md)
  This error code is unused.
- [SKAdTestError.Code.signatureMissingCampaignId](./signaturemissingcampaignid.md)
  The signature is missing the campaign identifier, in the testing environment.
- [SKAdTestError.Code.conflictingSource](./conflictingsource.md)
  This error code is unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/code/invalidcampaignid)*