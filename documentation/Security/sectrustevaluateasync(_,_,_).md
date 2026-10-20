# SecTrustEvaluateAsync(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Evaluates a trust object asynchronously on the specified dispatch queue.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0 (renamed: SecTrustEvaluateAsyncWithError(_:_:_:))
- iPadOS 7.0+ - Deprecated in 13.0 (renamed: SecTrustEvaluateAsyncWithError(_:_:_:))
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: SecTrustEvaluateAsyncWithError(_:_:_:))
- macOS 10.7+ - Deprecated in 10.15 (renamed: SecTrustEvaluateAsyncWithError(_:_:_:))
- tvOS 7.0+ - Deprecated in 13.0 (renamed: SecTrustEvaluateAsyncWithError(_:_:_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: SecTrustEvaluateAsyncWithError(_:_:_:))
- watchOS 1.0+ - Deprecated in 6.0 (renamed: SecTrustEvaluateAsyncWithError(_:_:_:))

> **Deprecated**: Use [`SecTrustEvaluateAsyncWithError(_:_:_:)`](./sectrustevaluateasyncwitherror%28_,_,_%29.md) instead.

## Declaration

```swift
func SecTrustEvaluateAsync(_ trust: SecTrust, _ queue: dispatch_queue_t?, _ result: @escaping SecTrustCallback) -> OSStatus
```

```c
OSStatus SecTrustEvaluateAsync(SecTrustRef trust, dispatch_queue_t queue, SecTrustCallback result);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

This function is functionally equivalent to [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md) except that it performs evaluation asynchronously and calls a block when evaluation completes. For a detailed discussion of the evaluation process, see [`SecTrustEvaluate(_:_:)`](./sectrustevaluate%28_,_%29.md).

## Parameters

- `trust`: The trust management object to evaluate. A trust management object includes the certificate to be verified plus the policy or policies to be used in evaluating trust. It can optionally also include other certificates to be used in verifying the first certificate. Use the [`SecTrustCreateWithCertificates(_:_:_:)`](./sectrustcreatewithcertificates%28_,_,_%29.md) function to create a trust management object.
- `queue`: The dispatch queue on which the result block should execute.
- `result`: A block called with the result of evaluation. See [`SecTrustResultType`](./sectrustresulttype.md) for descriptions of possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustevaluateasync(_:_:_:))*