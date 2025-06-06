# failureResponse

**Framework**: Foundation  
**Kind**: property

The URL response object representing the last authentication failure.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var failureResponse: URLResponse? { get }
```

#### Discussion

This value is `nil` if the protocol doesn’t use responses to indicate an authentication failure.

## See Also

- [var error: (any Error)?](urlauthenticationchallenge/error.md)
  The error object representing the last authentication failure.
- [var previousFailureCount: Int](urlauthenticationchallenge/previousfailurecount.md)
  The receiver’s count of failed authentication attempts.
- [var proposedCredential: URLCredential?](urlauthenticationchallenge/proposedcredential.md)
  The proposed credential for this challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/failureresponse)*