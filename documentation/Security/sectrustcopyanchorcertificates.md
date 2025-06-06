# SecTrustCopyAnchorCertificates(_:)

**Framework**: Security  
**Kind**: func

Retrieves the anchor (root) certificates stored by macOS.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SecTrustCopyAnchorCertificates(_ anchors: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This function retrieves the certificates in the system’s store of anchor certificates (see [`SecTrustSetAnchorCertificates(_:_:)`](sectrustsetanchorcertificates(_:_:).md)). You can use the [`SecCertificate`](seccertificate.md) objects retrieved by this function as input to other functions of this API, such as [`SecTrustCreateWithCertificates(_:_:_:)`](sectrustcreatewithcertificates(_:_:_:).md).

It is safe to call this function concurrently on two or more threads as long as it is not used to get values from a trust management object that is simultaneously being changed by another function. For example, you can call this function on two threads at the same time, but not if you are simultaneously calling the [`SecTrustSetAnchorCertificates(_:_:)`](sectrustsetanchorcertificates(_:_:).md) function for the same trust management object on another thread.

## Parameters

- `anchors`: On return, points to an array of certificate objects for trusted anchor (root) certificates, which is the default set of anchors for the caller. In Objective-C, call the   function to release the   object when you are finished with it.

## See Also

- [func SecTrustSetAnchorCertificates(SecTrust, CFArray?) -> OSStatus](sectrustsetanchorcertificates(_:_:).md)
  Sets the anchor certificates used when evaluating a trust management object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustcopyanchorcertificates(_:))*