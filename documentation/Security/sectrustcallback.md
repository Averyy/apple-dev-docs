# SecTrustCallback

**Framework**: Security  
**Kind**: typealias

A block called with the results of an asynchronous trust evaluation.

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
typealias SecTrustCallback = (SecTrust, SecTrustResultType) -> Void
```

#### Discussion

Use a block of this type when making a call to [`SecTrustEvaluateAsync(_:_:_:)`](sectrustevaluateasync(_:_:_:).md) to receive the result of the trust evaluation.

## Parameters

- `trustRef`: The trust that was evaluated.
- `trustResult`: The result of the trust evaluation. See   for a list of possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustcallback)*