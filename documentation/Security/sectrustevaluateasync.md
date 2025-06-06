# SecTrustEvaluateAsync(_:_:_:)

**Framework**: Security  
**Kind**: func

Evaluates a trust object asynchronously on the specified dispatch queue.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func SecTrustEvaluateAsync(_ trust: SecTrust, _ queue: dispatch_queue_t?, _ result: @escaping SecTrustCallback) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This function is functionally equivalent to [`SecTrustEvaluate(_:_:)`](sectrustevaluate(_:_:).md) except that it performs evaluation asynchronously and calls a block when evaluation completes. For a detailed discussion of the evaluation process, see [`SecTrustEvaluate(_:_:)`](sectrustevaluate(_:_:).md).

## Parameters

- `trust`: The trust management object to evaluate. A trust management object includes the certificate to be verified plus the policy or policies to be used in evaluating trust. It can optionally also include other certificates to be used in verifying the first certificate. Use the   function to create a trust management object.
- `queue`: The dispatch queue on which the result block should execute.
- `result`: A block called with the result of evaluation. See   for descriptions of possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustevaluateasync(_:_:_:))*