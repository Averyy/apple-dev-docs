# SKAdTestError.Code.invalidConversionValue

**Framework**: StoreKit Test  
**Kind**: case  
**Role**: Case

The conversion value isn’t valid, in the testing environment.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
case invalidConversionValue
```

```c
SKAdTestErrorCodeInvalidConversionValue
```

## Discussion

This error isn’t used. If your conversion value isn’t valid, the unit test shows the [`SKANError.Code.invalidConversionValue`](../../../StoreKit/skanerror-swift.struct/code/invalidconversionvalue.md) error instead, but only if your app calls [`updatePostbackConversionValue(_:completionHandler:)`](../../../StoreKit/skadnetwork/updatepostbackconversionvalue%28_,completionhandler%29.md).

## See Also

### Postback Errors
- [SKAdTestError.Code.excessivePostbacks](./excessivepostbacks.md)
  Too many postbacks submitted to the test session.
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
- [SKAdTestError.Code.noPendingPostbacks](./nopendingpostbacks.md)
  The test session doesn’t have any pending postbacks to send.
- [SKAdTestError.Code.unlinkedWinningPostbacks](./unlinkedwinningpostbacks.md)
  The postbacks aren’t correctly related to one another.
- [SKAdTestError.Code.excessivePostbacks](./excessivepostbacks.md)
  Too many postbacks submitted to the test session.
- [SKAdTestError.Code.invalidPostbackURL](./invalidpostbackurl.md)
  The URL for the postback isn’t valid, in the testing environment.
- [SKAdTestError.Code.invalidRunnerUpPostback](./invalidrunneruppostback.md)
  A non-winning postback is defined with a version prior to version 3, in the testing environment.
- [SKAdTestError.Code.invalidWinningPostbackCount](./invalidwinningpostbackcount.md)
  The number of winning postbacks isn’t valid, in the testing environment.
- [SKAdTestError.Code.malformedPostbacks](./malformedpostbacks.md)
  The postback in the testing environment is malformed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/code/invalidconversionvalue)*