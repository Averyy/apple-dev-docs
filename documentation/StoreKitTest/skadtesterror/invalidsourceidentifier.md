# invalidSourceIdentifier

**Framework**: StoreKit Test  
**Kind**: property

The postback’s identifier isn’t two, three, or four digits.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
static var invalidSourceIdentifier: SKAdTestError.Code { get }
```

#### Discussion

A valid postback includes two to four digits of the impression’s [`sourceIdentifier`](https://developer.apple.com/documentation/StoreKit/SKAdImpression/sourceIdentifier). For more information about the varying length of source identifiers, see [`Receiving postbacks in multiple conversion windows`](https://developer.apple.com/documentation/StoreKit/receiving-postbacks-in-multiple-conversion-windows).

## See Also

- [static var invalidVersion: SKAdTestError.Code](skadtesterror/invalidversion.md)
  A postback contains an incorrect version number.
- [static var invalidImpressionId: SKAdTestError.Code](skadtesterror/invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [static var invalidSourceAppAdamId: SKAdTestError.Code](skadtesterror/invalidsourceappadamid.md)
  The app ID is less than zero.
- [static var invalidSourceDomain: SKAdTestError.Code](skadtesterror/invalidsourcedomain.md)
  The source domain isn’t in the correct format.
- [static var unknownError: SKAdTestError.Code](skadtesterror/unknownerror.md)
  An unknown error occurred in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/invalidsourceidentifier)*