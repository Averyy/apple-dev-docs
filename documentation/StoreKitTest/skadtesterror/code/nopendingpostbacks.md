# SKAdTestError.Code.noPendingPostbacks

**Framework**: StoreKit Test  
**Kind**: case  
**Role**: Case

The test session doesn’t have any pending postbacks to send.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
case noPendingPostbacks
```

```c
SKAdTestErrorCodeNoPendingPostbacks
```

## Discussion

This error occurs if you call [`flushPostbacks(responses:)`](../../skadtestsession/flushpostbacks%28responses%29.md) before adding a postback to the test session ([`SKAdTestSession`](../../skadtestsession.md)). To avoid this error, call [`SKAdTestPostback`](../../skadtestpostback.md) to create a test postback, and [`setPostbacks(_:)`](../../skadtestsession/setpostbacks%28_%29.md) to add the test postback to the test session before calling [`flushPostbacks(responses:)`](../../skadtestsession/flushpostbacks%28responses%29.md).

## See Also

### Postback Errors
- [SKAdTestError.Code.excessivePostbacks](./excessivepostbacks.md)
  Too many postbacks submitted to the test session.
- [SKAdTestError.Code.invalidConversionValue](./invalidconversionvalue.md)
  The conversion value isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidPostbackURL](./invalidpostbackurl.md)
  The URL for the postback isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidRunnerUpPostback](./invalidrunneruppostback.md)
  A non-winning postback is defined with a version prior to version 3, in the testing environment.
- [SKAdTestError.Code.invalidWinningPostbackCount](./invalidwinningpostbackcount.md)
  The number of winning postbacks isn’t valid, in the testing environment.
- [SKAdTestError.Code.malformedPostbacks](./malformedpostbacks.md)
  The postback in the testing environment is malformed.
- [SKAdTestError.Code.missingPostbacks](./missingpostbacks.md)
  The testing environment doesn’t have any postbacks.
- [SKAdTestError.Code.misplacedWinnerPostback](./misplacedwinnerpostback.md)
  A winning postback wasn’t found in the first position, in the testing environment.
- [SKAdTestError.Code.missingWinningPostback](./missingwinningpostback.md)
  The testing environment is missing a winning postback.
- [SKAdTestError.Code.unlinkedWinningPostbacks](./unlinkedwinningpostbacks.md)
  The postbacks aren’t correctly related to one another.
- [SKAdTestError.Code.excessivePostbacks](./excessivepostbacks.md)
  Too many postbacks submitted to the test session.
- [SKAdTestError.Code.invalidConversionValue](./invalidconversionvalue.md)
  The conversion value isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidPostbackURL](./invalidpostbackurl.md)
  The URL for the postback isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidRunnerUpPostback](./invalidrunneruppostback.md)
  A non-winning postback is defined with a version prior to version 3, in the testing environment.
- [SKAdTestError.Code.invalidWinningPostbackCount](./invalidwinningpostbackcount.md)
  The number of winning postbacks isn’t valid, in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/code/nopendingpostbacks)*