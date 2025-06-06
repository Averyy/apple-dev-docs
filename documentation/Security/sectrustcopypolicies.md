# SecTrustCopyPolicies(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the policies used by a given trust management object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecTrustCopyPolicies(_ trust: SecTrust, _ policies: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

It is safe to call this function concurrently on two or more threads as long as it is not used to get values from a trust management object that is simultaneously being changed by another function. For example, you can call this function on two threads at the same time, but not if you are simultaneously calling the [`SecTrustSetPolicies(_:_:)`](sectrustsetpolicies(_:_:).md) function for the same trust management object on another thread.

## Parameters

- `trust`: The trust management object whose policies you wish to retrieve.
- `policies`: On return, an array of   objects for the policies used by this trust management object. In Objective-C, call the   function to release this object when you are finished with it.

## See Also

- [func SecTrustSetPolicies(SecTrust, CFTypeRef) -> OSStatus](sectrustsetpolicies(_:_:).md)
  Sets the policies to use in an evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustcopypolicies(_:_:))*