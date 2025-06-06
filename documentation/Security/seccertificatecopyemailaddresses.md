# SecCertificateCopyEmailAddresses(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the email addresses for the subject of a certificate.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func SecCertificateCopyEmailAddresses(_ certificate: SecCertificate, _ emailAddresses: UnsafeMutablePointer<CFArray?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

Not every certificate subject includes an email address. If the function does not find any email addresses, it returns a `CFArrayRef` object with zero elements in the array.

## Parameters

- `certificate`: The certificate object from which to retrieve the email addresses.
- `emailAddresses`: On return, an array of zero or more   elements, each containing one email address found in the certificate subject. In Objective-C, call the   function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificatecopyemailaddresses(_:_:))*