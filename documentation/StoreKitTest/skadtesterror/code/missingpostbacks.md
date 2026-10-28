# SKAdTestError.Code.missingPostbacks

**Framework**: StoreKit Test  
**Kind**: case  
**Role**: Case

The testing environment doesn’t have any postbacks.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
case missingPostbacks
```

```c
SKAdTestErrorCodeMissingPostbacks
```

## Discussion

Check that the `postbacks` array you provide when calling [`setPostbacks(_:)`](../../skadtestsession/setpostbacks%28_%29.md) isn’t empty.

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
- [SKAdTestError.Code.misplacedWinnerPostback](./misplacedwinnerpostback.md)
  A winning postback wasn’t found in the first position, in the testing environment.
- [SKAdTestError.Code.missingWinningPostback](./missingwinningpostback.md)
  The testing environment is missing a winning postback.
- [SKAdTestError.Code.noPendingPostbacks](./nopendingpostbacks.md)
  The test session doesn’t have any pending postbacks to send.
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

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/code/missingpostbacks)*