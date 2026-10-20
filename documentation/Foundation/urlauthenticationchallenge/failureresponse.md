# failureResponse

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly, nullable) NSURLResponse * failureResponse;
```

#### Discussion

This value is `nil` if the protocol doesn’t use responses to indicate an authentication failure.

## See Also

### Related Documentation
- [var error: (any Error)?](./error.md)
  The error object representing the last authentication failure.
### Getting properties of previous authentication attempts
- [var previousFailureCount: Int](./previousfailurecount.md)
  The receiver’s count of failed authentication attempts.
- [var proposedCredential: URLCredential?](./proposedcredential.md)
  The proposed credential for this challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/failureresponse)*