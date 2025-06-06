# init(request:PASK:encryptionCert:signingCert:signingKey:)

**Framework**: App License Delivery SDK  
**Kind**: init

Initialize a ALDSession with a license request. Call generateLicense() to create a license.

## Declaration

```swift
init(request: [UInt8], PASK: [UInt8], encryptionCert: [UInt8], signingCert: [UInt8], signingKey: [UInt8]? = nil) throws
```

## Parameters

- `request`: Opaque request bytes sent by the client
- `PASK`: The server side secret provided to the provider
- `encryptionCert`: The ALD provider encryption cert
- `signingCert`: The ALD provider signing cert
- `signingKey`: The ALD provider signing key in DER encoded format. When provided, one can use finalizeLicenseResponse() to automarically sign the payload.   If this key is not provided, then one must sign each license payload out of band and add it to the license response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicensedeliverysdk/aldsession/init(request:pask:encryptioncert:signingcert:signingkey:))*