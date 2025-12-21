# proposedCredential

**Framework**: Foundation  
**Kind**: property

The proposed credential for this challenge.

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
var proposedCredential: URLCredential? { get }
```

#### Discussion

This method returns `nil` if there is no default credential for this challenge.

If you have previously attempted to authenticate and failed, this method returns the most recent failed credential.

If the proposed credential is not `nil` and returns [`true`](https://developer.apple.com/documentation/Swift/true) when you call its [`hasPassword`](urlcredential/haspassword.md) method, then the credential is ready to use as-is. If the proposed credential’s [`hasPassword`](urlcredential/haspassword.md) method returns [`false`](https://developer.apple.com/documentation/Swift/false), then the credential provides a default user name, and the client must prompt the user for a corresponding password.

## See Also

- [var failureResponse: URLResponse?](urlauthenticationchallenge/failureresponse.md)
  The URL response object representing the last authentication failure.
- [var previousFailureCount: Int](urlauthenticationchallenge/previousfailurecount.md)
  The receiver’s count of failed authentication attempts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/proposedcredential)*