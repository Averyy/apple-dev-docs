# unlinkedWinningPostbacks

**Framework**: StoreKit Test  
**Kind**: property

The postbacks aren’t correctly related to one another.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
static var unlinkedWinningPostbacks: SKAdTestError.Code { get }
```

#### Discussion

To create linked winning postbacks for testing multiple conversion windows, use the [`winningPostbacks(withVersion:adNetworkIdentifier:sourceIdentifier:appStoreItemIdentifier:sourceAppStoreItemIdentifier:sourceDomain:fidelityType:isRedownload:postbackURL:)`](skadtestpostback/winningpostbacks(withversion:adnetworkidentifier:sourceidentifier:appstoreitemidentifier:sourceappstoreitemidentifier:sourcedomain:fidelitytype:isredownload:postbackurl:).md) method.

## See Also

- [static var excessivePostbacks: SKAdTestError.Code](skadtesterror/excessivepostbacks.md)
  Too many postbacks submitted to the test session.
- [static var invalidConversionValue: SKAdTestError.Code](skadtesterror/invalidconversionvalue.md)
  The conversion value isn’t valid, in the testing environment.
- [static var invalidPostbackURL: SKAdTestError.Code](skadtesterror/invalidpostbackurl.md)
  The URL for the postback isn’t valid, in the testing environment.
- [static var invalidRunnerUpPostback: SKAdTestError.Code](skadtesterror/invalidrunneruppostback.md)
  A non-winning postback is defined with a version prior to version 3, in the testing environment.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/unlinkedwinningpostbacks)*