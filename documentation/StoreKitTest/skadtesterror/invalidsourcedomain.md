# invalidSourceDomain

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Type Property

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

For more information about formatting source domains, see the `source_domain` property of [`AdImpressionResponse`](../../SKAdNetworkforWebAds/adimpressionresponse.md).

## See Also

### Getting Other Errors
- [static var invalidVersion: SKAdTestError.Code](./invalidversion.md)
  A postback contains an incorrect version number.
- [static var invalidImpressionId: SKAdTestError.Code](./invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [static var invalidSourceAppAdamId: SKAdTestError.Code](./invalidsourceappadamid.md)
  The app ID is less than zero.
- [static var invalidSourceIdentifier: SKAdTestError.Code](./invalidsourceidentifier.md)
  The postback’s identifier isn’t two, three, or four digits.
- [static var unknownError: SKAdTestError.Code](./unknownerror.md)
  An unknown error occurred in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/invalidsourcedomain)*