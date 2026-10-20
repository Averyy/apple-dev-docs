# setCertificate(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Specifies the certificate that’s displayed in the view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func setCertificate(_ certificate: SecCertificate!)
```

```objc
- (void) setCertificate:(SecCertificateRef) certificate;
```

## Parameters

- `certificate`: The new certificate for the view.

## See Also

### Related Documentation
- [func certificate() -> Unmanaged<SecCertificate>!](./certificate%28%29.md)
  Returns the certificate currently displayed in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/setcertificate(_:))*