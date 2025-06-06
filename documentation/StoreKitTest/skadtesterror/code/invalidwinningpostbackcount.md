# SKAdTestError.Code.invalidWinningPostbackCount

**Framework**: StoreKit Test  
**Kind**: case

The number of winning postbacks isn’t valid, in the testing environment.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
case invalidWinningPostbackCount
```

#### Discussion

A valid session has one or three winning postbacks.

## See Also

- [SKAdTestError.Code.excessivePostbacks](skadtesterror/code/excessivepostbacks.md)
  Too many postbacks submitted to the test session.
- [SKAdTestError.Code.invalidConversionValue](skadtesterror/code/invalidconversionvalue.md)
  The conversion value isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidPostbackURL](skadtesterror/code/invalidpostbackurl.md)
  The URL for the postback isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidRunnerUpPostback](skadtesterror/code/invalidrunneruppostback.md)
  A non-winning postback is defined with a version prior to version 3, in the testing environment.
- [SKAdTestError.Code.malformedPostbacks](skadtesterror/code/malformedpostbacks.md)
  The postback in the testing environment is malformed.
- [SKAdTestError.Code.missingPostbacks](skadtesterror/code/missingpostbacks.md)
  The testing environment doesn’t have any postbacks.
- [SKAdTestError.Code.misplacedWinnerPostback](skadtesterror/code/misplacedwinnerpostback.md)
  A winning postback wasn’t found in the first position, in the testing environment.
- [SKAdTestError.Code.missingWinningPostback](skadtesterror/code/missingwinningpostback.md)
  The testing environment is missing a winning postback.
- [SKAdTestError.Code.noPendingPostbacks](skadtesterror/code/nopendingpostbacks.md)
  The test session doesn’t have any pending postbacks to send.
- [SKAdTestError.Code.unlinkedWinningPostbacks](skadtesterror/code/unlinkedwinningpostbacks.md)
  The postbacks aren’t correctly related to one another.
- [SKAdTestError.Code.excessivePostbacks](skadtesterror/code/excessivepostbacks.md)
  Too many postbacks submitted to the test session.
- [SKAdTestError.Code.invalidConversionValue](skadtesterror/code/invalidconversionvalue.md)
  The conversion value isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidPostbackURL](skadtesterror/code/invalidpostbackurl.md)
  The URL for the postback isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidRunnerUpPostback](skadtesterror/code/invalidrunneruppostback.md)
  A non-winning postback is defined with a version prior to version 3, in the testing environment.
- [SKAdTestError.Code.malformedPostbacks](skadtesterror/code/malformedpostbacks.md)
  The postback in the testing environment is malformed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/code/invalidwinningpostbackcount)*