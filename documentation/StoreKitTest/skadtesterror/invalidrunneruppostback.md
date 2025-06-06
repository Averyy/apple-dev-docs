# invalidRunnerUpPostback

**Framework**: StoreKit Test  
**Kind**: property

A non-winning postback is defined with a version prior to version 3, in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
static var invalidRunnerUpPostback: SKAdTestError.Code { get }
```

#### Discussion

Check that all non-winning postback you create with [`init(version:adNetworkIdentifier:adCampaignIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:conversionValue:fidelityType:isRedownload:didWin:postbackURL:)`](skadtestpostback/init(version:adnetworkidentifier:adcampaignidentifier:appstoreitemidentifier:sourceappstoreitemidentifier:conversionvalue:fidelitytype:isredownload:didwin:postbackurl:).md) in [`SKAdTestPostback`](skadtestpostback.md) specify version 3 ([`version3_0`](skadtestpostbackversion/version3_0.md)) or later. Non-winning postbacks are available starting in version 3. For more information about versions, see [`SKAdNetwork release notes`](https://developer.apple.com/documentation/StoreKit/skadnetwork-release-notes).

## See Also

- [static var excessivePostbacks: SKAdTestError.Code](skadtesterror/excessivepostbacks.md)
  Too many postbacks submitted to the test session.
- [static var invalidConversionValue: SKAdTestError.Code](skadtesterror/invalidconversionvalue.md)
  The conversion value isn’t valid, in the testing environment.
- [static var invalidPostbackURL: SKAdTestError.Code](skadtesterror/invalidpostbackurl.md)
  The URL for the postback isn’t valid, in the testing environment.
- [static var invalidWinningPostbackCount: SKAdTestError.Code](skadtesterror/invalidwinningpostbackcount.md)
  The number of winning postbacks isn’t valid, in the testing environment.
- [static var malformedPostbacks: SKAdTestError.Code](skadtesterror/malformedpostbacks.md)
  The postback in the testing environment is malformed.
- [static var missingPostbacks: SKAdTestError.Code](skadtesterror/missingpostbacks.md)
  The testing environment doesn’t have any postbacks.
- [static var misplacedWinnerPostback: SKAdTestError.Code](skadtesterror/misplacedwinnerpostback.md)
  A winning postback wasn’t found in the first position, in the testing environment.
- [static var missingWinningPostback: SKAdTestError.Code](skadtesterror/missingwinningpostback.md)
  The testing environment is missing a winning postback.
- [static var noPendingPostbacks: SKAdTestError.Code](skadtesterror/nopendingpostbacks.md)
  The test session doesn’t have any pending postbacks to send.
- [static var unlinkedWinningPostbacks: SKAdTestError.Code](skadtesterror/unlinkedwinningpostbacks.md)
  The postbacks aren’t correctly related to one another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/invalidrunneruppostback)*