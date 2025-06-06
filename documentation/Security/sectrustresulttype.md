# SecTrustResultType

**Framework**: Security  
**Kind**: enum

Trust evaluation result codes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum SecTrustResultType
```

#### Overview

You get one of these constants when you call the [`SecTrustGetTrustResult(_:_:)`](sectrustgettrustresult(_:_:).md) method after evaluating a trust instance with either the [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md) method or the [`SecTrustEvaluateAsyncWithError(_:_:_:)`](sectrustevaluateasyncwitherror(_:_:_:).md) method. If evaluation fails and [`SecTrustGetTrustResult(_:_:)`](sectrustgettrustresult(_:_:).md) reports [`SecTrustResultType.recoverableTrustFailure`](sectrustresulttype/recoverabletrustfailure.md), you might be able to change parameters like the evaluation date, and reevaluate to obtain a passing result, as described in [`Configuring a Trust`](configuring-a-trust.md).

See an individual constant below for more information about how to handle that result type in your app.

## Topics

### Result Codes
- [SecTrustResultType.unspecified](sectrustresulttype/unspecified.md)
  The user did not specify a trust setting.
- [SecTrustResultType.proceed](sectrustresulttype/proceed.md)
  The user granted permission to trust the certificate for the purposes designated in the specified policies.
- [SecTrustResultType.deny](sectrustresulttype/deny.md)
  The user specified that the certificate should not be trusted.
- [SecTrustResultType.recoverableTrustFailure](sectrustresulttype/recoverabletrustfailure.md)
  Trust is denied, but recovery may be possible.
- [SecTrustResultType.fatalTrustFailure](sectrustresulttype/fataltrustfailure.md)
  Trust is denied and no simple fix is available.
- [SecTrustResultType.otherError](sectrustresulttype/othererror.md)
  A value that indicates a failure other than trust evaluation.
- [SecTrustResultType.invalid](sectrustresulttype/invalid.md)
  An indication of an invalid setting or result.
- [SecTrustResultType.confirm](sectrustresulttype/confirm.md)
  User confirmation is required before proceeding.
### Initializers
- [init?(rawValue: UInt32)](sectrustresulttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustresulttype)*