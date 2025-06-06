# init(signingCert:signingKey:PASK:)

**Framework**: App License Delivery SDK  
**Kind**: init

Initialize a static ALDSession without a request. This should only be used when an offline generation of a static license is desired. A static license is a minimal license that is only used to install apps on the device and is not meant to enforce marketplace defined rights. Only generateStaticLicense() should be invoked to generate licenses in this case.

## Declaration

```swift
init(signingCert: [UInt8], signingKey: [UInt8]? = nil, PASK: [UInt8]) throws
```

## Parameters

- `signingCert`: The ALD provider signing cert
- `signingKey`: The ALD provider signing key in DER encoded format. When provided, one can use finalizeLicenseResponse() to automarically sign the payload.   If this key is not provided, then one must sign each license payload out of band and add it to the license response.
- `PASK`: The server side secret provided to the provider


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicensedeliverysdk/aldsession/init(signingcert:signingkey:pask:))*