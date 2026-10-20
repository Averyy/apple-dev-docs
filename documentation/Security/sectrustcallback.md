# SecTrustCallback

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

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

```c
typedef void (^)(struct __SecTrust *, enum SecTrustResultType) SecTrustCallback;
```

#### Discussion

Use a block of this type when making a call to [`SecTrustEvaluateAsync(_:_:_:)`](./sectrustevaluateasync%28_,_,_%29.md) to receive the result of the trust evaluation.

## Parameters

- `trustRef`: The trust that was evaluated.
- `trustResult`: The result of the trust evaluation. See [`SecTrustResultType`](./sectrustresulttype.md) for a list of possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustcallback)*