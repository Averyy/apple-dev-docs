# ALDProvider

**Framework**: App License Delivery SDK  
**Kind**: class

An object that creates a session with the alternative app marketplace’s signing assets.

## Declaration

```swift
class ALDProvider
```

## Mentions

- [Licensing alternative distribution apps](licensing-alternative-distribution-apps.md)

## Topics

### Initializers
- [init(encryptionCert: [UInt8], signingCert: [UInt8], PASK: [UInt8], signingKey: [UInt8]?)](aldprovider/init(encryptioncert:signingcert:pask:signingkey:).md)
  Initializes a provider with the marketplace’s App License Delivery assets and their unique signing key.
### Instance Methods
- [func createSession(clientRequest: [UInt8]) throws -> ALDSession](aldprovider/createsession(clientrequest:).md)
  Creates an ALD Session

## See Also

- [Licensing alternative distribution apps](licensing-alternative-distribution-apps.md)
  Build a license server that supports the installation of your apps and the apps available in your marketplace.
- [Renewing and revoking app licenses](renewing-and-revoking-app-licenses.md)
  Determine whether an app for which you issue a license launches.
- [struct ALDAppKey](aldappkey.md)
  A structure that identifies an app and a key that’s required to decrypt the app’s license request.
- [struct ALDLicenseAttribute](aldlicenseattribute.md)
  A structure that defines the requested license type for the session.
- [class ALDSession](aldsession.md)
  A structure that contains the details of a license request and methods to generate license responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicensedeliverysdk/aldprovider)*