# signatureData

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The result of signing the data provided by the caller using the requested digital identity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
let signatureData: Data
```

#### Discussion

The pass determines the signature data format.

## See Also

### Defining the certificate and signed data
- [let certificate: JPKIPassContents.Certificate<IdentityType>](./certificate.md)
  The certificate associated with an identity document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/jpkipasscontents/signature/signaturedata)*