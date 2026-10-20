# noPendingPostbacks

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Type Property

The test session doesn’t have any pending postbacks to send.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
static var noPendingPostbacks: SKAdTestError.Code { get }
```

#### Discussion

This error occurs if you call [`flushPostbacks(responses:)`](../skadtestsession/flushpostbacks%28responses%29.md) before adding a postback to the test session ([`SKAdTestSession`](../skadtestsession.md)). To avoid this error, call [`SKAdTestPostback`](../skadtestpostback.md) to create a test postback, and [`setPostbacks(_:)`](../skadtestsession/setpostbacks%28_%29.md) to add the test postback to the test session before calling [`flushPostbacks(responses:)`](../skadtestsession/flushpostbacks%28responses%29.md).

## See Also

### Getting Postback Errors
- [static var excessivePostbacks: SKAdTestError.Code](./excessivepostbacks.md)
  Too many postbacks submitted to the test session.
- [static var invalidConversionValue: SKAdTestError.Code](./invalidconversionvalue.md)
  The conversion value isn’t valid, in the testing environment.
- [static var invalidPostbackURL: SKAdTestError.Code](./invalidpostbackurl.md)
  The URL for the postback isn’t valid, in the testing environment.
- [static var invalidRunnerUpPostback: SKAdTestError.Code](./invalidrunneruppostback.md)
  A non-winning postback is defined with a version prior to version 3, in the testing environment.
- [static var invalidWinningPostbackCount: SKAdTestError.Code](./invalidwinningpostbackcount.md)
  The number of winning postbacks isn’t valid, in the testing environment.
- [static var malformedPostbacks: SKAdTestError.Code](./malformedpostbacks.md)
  The postback in the testing environment is malformed.
- [static var missingPostbacks: SKAdTestError.Code](./missingpostbacks.md)
  The testing environment doesn’t have any postbacks.
- [static var misplacedWinnerPostback: SKAdTestError.Code](./misplacedwinnerpostback.md)
  A winning postback wasn’t found in the first position, in the testing environment.
- [static var missingWinningPostback: SKAdTestError.Code](./missingwinningpostback.md)
  The testing environment is missing a winning postback.
- [static var unlinkedWinningPostbacks: SKAdTestError.Code](./unlinkedwinningpostbacks.md)
  The postbacks aren’t correctly related to one another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/nopendingpostbacks)*