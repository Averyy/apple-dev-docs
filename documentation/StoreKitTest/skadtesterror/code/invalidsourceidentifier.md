# SKAdTestError.Code.invalidSourceIdentifier

**Framework**: StoreKit Test  
**Kind**: case  
**Role**: Case

The postback’s identifier isn’t two, three, or four digits.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
case invalidSourceIdentifier
```

```c
SKAdTestErrorCodeInvalidSourceIdentifier
```

## Discussion

A valid postback includes two to four digits of the impression’s [`sourceIdentifier`](../../../StoreKit/skadimpression/sourceidentifier.md). For more information about the varying length of source identifiers, see [Receiving postbacks in multiple conversion windows](../../../StoreKit/receiving-postbacks-in-multiple-conversion-windows.md).

## See Also

### Other Errors
- [SKAdTestError.Code.invalidVersion](./invalidversion.md)
  A postback contains an incorrect version number.
- [SKAdTestError.Code.invalidImpressionId](./invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [SKAdTestError.Code.invalidSourceAppAdamId](./invalidsourceappadamid.md)
  The app ID is less than zero.
- [SKAdTestError.Code.invalidSourceDomain](./invalidsourcedomain.md)
  The source domain isn’t in the correct format.
- [SKAdTestError.Code.unknownError](./unknownerror.md)
  An unknown error occurred in the testing environment.
- [SKAdTestError.Code.invalidVersion](./invalidversion.md)
  A postback contains an incorrect version number.
- [SKAdTestError.Code.invalidImpressionId](./invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [SKAdTestError.Code.invalidSourceAppAdamId](./invalidsourceappadamid.md)
  The app ID is less than zero.
- [SKAdTestError.Code.invalidSourceDomain](./invalidsourcedomain.md)
  The source domain isn’t in the correct format.
- [SKAdTestError.Code.unknownError](./unknownerror.md)
  An unknown error occurred in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/code/invalidsourceidentifier)*