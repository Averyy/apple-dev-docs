# init(encryptionCert:signingCert:PASK:signingKey:)

**Framework**: App License Delivery SDK  
**Kind**: init

Initializes a provider with the marketplace’s App License Delivery assets and their unique signing key.

## Declaration

```swift
init(encryptionCert: [UInt8], signingCert: [UInt8], PASK: [UInt8], signingKey: [UInt8]? = nil)
```

## Mentions

- [Licensing alternative distribution apps](licensing-alternative-distribution-apps.md)

#### Discussion

For an example that uses a provider, see [`Licensing alternative distribution apps`](licensing-alternative-distribution-apps.md).

## Parameters

- `encryptionCert`: Apple issued encryption certificate in bytes.
- `signingCert`: Apple issued signing certificate in bytes.
- `PASK`: Apple provided secret blob.
- `signingKey`: Private key corresponding to the   in   format with   encoding. This parameter is optional if you choose to sign the license response manually.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicensedeliverysdk/aldprovider/init(encryptioncert:signingcert:pask:signingkey:))*