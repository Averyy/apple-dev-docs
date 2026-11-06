# kSecQWACTLSBindingErrorDomain

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
let kSecQWACTLSBindingErrorDomain: CFString
```

```c
extern CFStringRef const kSecQWACTLSBindingErrorDomain;
```

## Discussion

The CFError domain for errors returned by SecTrustCreateAndVerifyQWACTLSBinding.

Errors in this domain carry a code from SecQWACTLSBindingError. Where a failure originates below this layer, the underlying error is available in the user info dictionary under kCFErrorUnderlyingErrorKey: in particular a kSecQWACTLSBindingErrorCertificate carries the trust evaluation’s own error, which identifies the certificate at fault.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecqwactlsbindingerrordomain)*