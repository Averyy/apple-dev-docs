# NSCoder.DecodingFailurePolicy.setErrorAndReturn

**Framework**: Foundation  
**Kind**: case

A failure policy that directs the coder to capture the failure as an error object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case setErrorAndReturn
```

#### Discussion

On decode failure, the [`NSCoder`](nscoder.md) will capture the failure as an [`NSError`](nserror.md), and prevent further decodes (by returning `0` / `nil` equivalent as appropriate).

Use this policy if you know that all encoded objects use [`failWithError(_:)`](nscoder/failwitherror(_:).md) to communicate decode failures and don’t raise exceptions for error propagation.

## See Also

- [NSCoder.DecodingFailurePolicy.raiseException](nscoder/decodingfailurepolicy-swift.enum/raiseexception.md)
  A failure policy that directs the coder to raise an exception.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodingfailurepolicy-swift.enum/seterrorandreturn)*