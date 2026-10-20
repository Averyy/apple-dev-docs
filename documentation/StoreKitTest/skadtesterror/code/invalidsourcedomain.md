# SKAdTestError.Code.invalidSourceDomain

**Framework**: StoreKit Test  
**Kind**: case  
**Role**: Case

The source domain isn’t in the correct format.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
case invalidSourceDomain
```

```c
SKAdTestErrorCodeInvalidSourceDomain
```

#### Discussion

For more information about formatting source domains, see the `source_domain` property of [`AdImpressionResponse`](../../../SKAdNetworkforWebAds/adimpressionresponse.md).

## See Also

### Other Errors
- [SKAdTestError.Code.invalidVersion](./invalidversion.md)
  A postback contains an incorrect version number.
- [SKAdTestError.Code.invalidImpressionId](./invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [SKAdTestError.Code.invalidSourceAppAdamId](./invalidsourceappadamid.md)
  The app ID is less than zero.
- [SKAdTestError.Code.invalidSourceIdentifier](./invalidsourceidentifier.md)
  The postback’s identifier isn’t two, three, or four digits.
- [SKAdTestError.Code.unknownError](./unknownerror.md)
  An unknown error occurred in the testing environment.
- [SKAdTestError.Code.invalidVersion](./invalidversion.md)
  A postback contains an incorrect version number.
- [SKAdTestError.Code.invalidImpressionId](./invalidimpressionid.md)
  The impression ID isn’t a valid UUID string.
- [SKAdTestError.Code.invalidSourceAppAdamId](./invalidsourceappadamid.md)
  The app ID is less than zero.
- [SKAdTestError.Code.invalidSourceIdentifier](./invalidsourceidentifier.md)
  The postback’s identifier isn’t two, three, or four digits.
- [SKAdTestError.Code.unknownError](./unknownerror.md)
  An unknown error occurred in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtesterror/code/invalidsourcedomain)*