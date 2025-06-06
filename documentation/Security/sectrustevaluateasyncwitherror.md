# SecTrustEvaluateAsyncWithError(_:_:_:)

**Framework**: Security  
**Kind**: func

Evaluates a trust object asynchronously on the specified dispatch queue.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func SecTrustEvaluateAsyncWithError(_ trust: SecTrust, _ queue: dispatch_queue_t, _ result: @escaping SecTrustWithErrorCallback) -> OSStatus
```

## Mentions

- [Evaluating a Trust and Parsing the Result](evaluating-a-trust-and-parsing-the-result.md)

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This method behaves like [`SecTrustEvaluateWithError(_:_:)`](sectrustevaluatewitherror(_:_:).md), except that it provides an evaluation by calling the given closure. The method might do this synchronously before returning if the trust instance already contains a result. Otherwise, the method returns immediately, performs the evaluation asynchronously, and calls the closure with the result later.

> ❗ **Important**:  You must call this method from the same dispatch queue that you specify as the `queue` parameter.

 You must call this method from the same dispatch queue that you specify as the `queue` parameter.

## Parameters

- `trust`: The trust management object to evaluate. A trust management object includes the certificate to be verified plus the policy or policies to be used in evaluating trust. It can optionally also include other certificates to be used in verifying the first certificate. Use the   function to create a trust management object.
- `queue`: The dispatch queue on which the result block should execute. You must call the method from the same queue.
- `result`: A closure that the method calls to report the result of trust evaluation. The method calls the closure exactly once if the method returns  , and not at all otherwise. The method might call the closure synchronously in some cases, before returning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustevaluateasyncwitherror(_:_:_:))*