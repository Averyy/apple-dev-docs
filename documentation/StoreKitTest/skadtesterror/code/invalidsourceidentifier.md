# SKAdTestError.Code.invalidSourceIdentifier

**Framework**: StoreKit Test  
**Kind**: case

The postback’s identifier isn’t two, three, or four digits.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
case invalidSourceIdentifier
```

#### Discussion

A valid postback includes two to four digits of the impression’s [`sourceIdentifier`](https://developer.apple.com/documentation/StoreKit/SKAdImpression/sourceIdentifier). For more information about the varying length of source identifiers, see [`Receiving postbacks in multiple conversion windows`](https://developer.apple.com/documentation/StoreKit/receiving-postbacks-in-multiple-conversion-windows).

## See Also

- [SKAdTestError.Code.invalidVersion](skadtesterror/code/invalidversion.md)
  A postback contains an incorrect version number.
- [SKAdTestError.Code.invalidImpressionId](skadtesterror/code/invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [SKAdTestError.Code.invalidSourceAppAdamId](skadtesterror/code/invalidsourceappadamid.md)
  The app ID is less than zero.
- [SKAdTestError.Code.invalidSourceDomain](skadtesterror/code/invalidsourcedomain.md)
  The source domain isn’t in the correct format.
- [SKAdTestError.Code.unknownError](skadtesterror/code/unknownerror.md)
  An unknown error occurred in the testing environment.
- [SKAdTestError.Code.invalidVersion](skadtesterror/code/invalidversion.md)
  A postback contains an incorrect version number.
- [SKAdTestError.Code.invalidImpressionId](skadtesterror/code/invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [SKAdTestError.Code.invalidSourceAppAdamId](skadtesterror/code/invalidsourceappadamid.md)
  The app ID is less than zero.
- [SKAdTestError.Code.invalidSourceDomain](skadtesterror/code/invalidsourcedomain.md)
  The source domain isn’t in the correct format.
- [SKAdTestError.Code.unknownError](skadtesterror/code/unknownerror.md)
  An unknown error occurred in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/code/invalidsourceidentifier)*