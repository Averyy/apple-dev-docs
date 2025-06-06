# invalidSourceDomain

**Framework**: StoreKit Test  
**Kind**: property

The source domain isn’t in the correct format.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
static var invalidSourceDomain: SKAdTestError.Code { get }
```

#### Discussion

For more information about formatting source domains, see the `source_domain` property of [`AdImpressionResponse`](https://developer.apple.com/documentation/SKAdNetworkforWebAds/AdImpressionResponse).

## See Also

- [static var invalidVersion: SKAdTestError.Code](skadtesterror/invalidversion.md)
  A postback contains an incorrect version number.
- [static var invalidImpressionId: SKAdTestError.Code](skadtesterror/invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [static var invalidSourceAppAdamId: SKAdTestError.Code](skadtesterror/invalidsourceappadamid.md)
  The app ID is less than zero.
- [static var invalidSourceIdentifier: SKAdTestError.Code](skadtesterror/invalidsourceidentifier.md)
  The postback’s identifier isn’t two, three, or four digits.
- [static var unknownError: SKAdTestError.Code](skadtesterror/unknownerror.md)
  An unknown error occurred in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/invalidsourcedomain)*