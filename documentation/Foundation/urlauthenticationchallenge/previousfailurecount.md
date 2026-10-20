# previousFailureCount

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The receiver’s count of failed authentication attempts.

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
var previousFailureCount: Int { get }
```

```objc
@property (readonly) NSInteger previousFailureCount;
```

#### Discussion

The previous failure count includes failures from *all* protection spaces, not just the current one.

## See Also

### Getting properties of previous authentication attempts
- [var failureResponse: URLResponse?](./failureresponse.md)
  The URL response object representing the last authentication failure.
- [var proposedCredential: URLCredential?](./proposedcredential.md)
  The proposed credential for this challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/previousfailurecount)*