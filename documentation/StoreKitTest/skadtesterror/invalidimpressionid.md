# invalidImpressionId

**Framework**: StoreKit Test  
**Kind**: property

The impression ID isn’t a valid UUID string.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
static var invalidImpressionId: SKAdTestError.Code { get }
```

## See Also

- [static var invalidVersion: SKAdTestError.Code](skadtesterror/invalidversion.md)
  A postback contains an incorrect version number.
- [static var invalidSourceAppAdamId: SKAdTestError.Code](skadtesterror/invalidsourceappadamid.md)
  The app ID is less than zero.
- [static var invalidSourceDomain: SKAdTestError.Code](skadtesterror/invalidsourcedomain.md)
  The source domain isn’t in the correct format.
- [static var invalidSourceIdentifier: SKAdTestError.Code](skadtesterror/invalidsourceidentifier.md)
  The postback’s identifier isn’t two, three, or four digits.
- [static var unknownError: SKAdTestError.Code](skadtesterror/unknownerror.md)
  An unknown error occurred in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/invalidimpressionid)*