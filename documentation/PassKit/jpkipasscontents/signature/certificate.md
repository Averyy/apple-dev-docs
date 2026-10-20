# certificate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The certificate associated with an identity document.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
let certificate: JPKIPassContents.Certificate<IdentityType>
```

## See Also

### Defining the certificate and signed data
- [let signatureData: Data](./signaturedata.md)
  The result of signing the data provided by the caller using the requested digital identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/signature/certificate)*