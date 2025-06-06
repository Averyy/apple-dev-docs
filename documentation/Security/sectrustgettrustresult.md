# SecTrustGetTrustResult(_:_:)

**Framework**: Security  
**Kind**: func

Returns the result code from the most recent trust evaluation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecTrustGetTrustResult(_ trust: SecTrust, _ result: UnsafeMutablePointer<SecTrustResultType>) -> OSStatus
```

## Mentions

- [Discovering Why a Trust Evaluation Failed](discovering-why-a-trust-evaluation-failed.md)

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

If the trust object has not yet been evaluated, the result type is [`SecTrustResultType.invalid`](sectrustresulttype/invalid.md).

## Parameters

- `trust`: The trust object from which results should be obtained
- `result`: A pointer that the function sets to point at a value that is the result type. See   for possible values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustgettrustresult(_:_:))*