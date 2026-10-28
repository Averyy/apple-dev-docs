# invalidSourceIdentifier

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Type Property

The postback’s identifier isn’t two, three, or four digits.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
static var invalidSourceIdentifier: SKAdTestError.Code { get }
```

## Discussion

A valid postback includes two to four digits of the impression’s [`sourceIdentifier`](../../StoreKit/skadimpression/sourceidentifier.md). For more information about the varying length of source identifiers, see [Receiving postbacks in multiple conversion windows](../../StoreKit/receiving-postbacks-in-multiple-conversion-windows.md).

## See Also

### Getting Other Errors
- [static var invalidVersion: SKAdTestError.Code](./invalidversion.md)
  A postback contains an incorrect version number.
- [static var invalidImpressionId: SKAdTestError.Code](./invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [static var invalidSourceAppAdamId: SKAdTestError.Code](./invalidsourceappadamid.md)
  The app ID is less than zero.
- [static var invalidSourceDomain: SKAdTestError.Code](./invalidsourcedomain.md)
  The source domain isn’t in the correct format.
- [static var unknownError: SKAdTestError.Code](./unknownerror.md)
  An unknown error occurred in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/invalidsourceidentifier)*