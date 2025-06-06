# kSecImportItemTrust

**Framework**: Security  
**Kind**: var

Trust management object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecImportItemTrust: CFString
```

## Mentions

- [Importing an Identity](importing-an-identity.md)

#### Discussion

The corresponding value is of type `SecTrustRef`. The trust reference returned by the [`SecPKCS12Import(_:_:_:)`](secpkcs12import(_:_:_:).md) function has been evaluated against the basic X.509 policy and includes as complete a certificate chain as could be constructed from the certificates in the PKCS #12 blob, certificates on the keychain, and any other certificates available to the system. You can use the [`SecTrustEvaluate(_:_:)`](sectrustevaluate(_:_:).md) function if you want to know whether the certificate chain is complete and valid (according to the basic X.509 policy). There is no guarantee that the evaluation will succeed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecimportitemtrust)*