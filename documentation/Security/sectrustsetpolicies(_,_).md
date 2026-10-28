# SecTrustSetPolicies(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the policies to use in an evaluation.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecTrustSetPolicies(_ trust: SecTrust, _ policies: CFTypeRef) -> OSStatus
```

```c
OSStatus SecTrustSetPolicies(SecTrustRef trust, CFTypeRef policies);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

The policies you set with this function replace any already in the trust management object.

It is safe to call this function concurrently on two or more threads as long as it is not used to change the value of a trust management object that is simultaneously being used by another function. For example, you cannot call this function on one thread at the same time as you are calling the [`SecTrustEvaluateWithError(_:_:)`](./sectrustevaluatewitherror%28_,_%29.md) function for the same trust management object on another thread, but you can call this function and simultaneously evaluate a different trust management object on another thread. Similarly, calls to functions that return information about a trust management object (such as the [`SecTrustCopyCustomAnchorCertificates(_:_:)`](./sectrustcopycustomanchorcertificates%28_,_%29.md) function) may fail or return an unexpected result if this function is simultaneously changing the same trust management object on another thread.

## Parameters

- `trust`: The trust management object whose policy list you wish to set.
- `policies`: An array of one or more [`SecPolicy`](./secpolicy.md) objects for the policies to be used by this trust management object. A single policy object of type `SecPolicyRef` may also be passed, representing an array of one policy.

## See Also

### Related Documentation
- [func SecTrustCopyPolicies(SecTrust, UnsafeMutablePointer<CFArray?>) -> OSStatus](./sectrustcopypolicies%28_,_%29.md)
  Retrieves the policies used by a given trust management object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsetpolicies(_:_:))*