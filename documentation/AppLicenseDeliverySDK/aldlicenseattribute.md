# ALDLicenseAttribute

**Framework**: App License Delivery SDK  
**Kind**: struct

A structure that defines the requested license type for the session.

## Declaration

```swift
struct ALDLicenseAttribute
```

## Topics

### Initializers
- [init(licenseID: UInt64)](aldlicenseattribute/init(licenseid:).md)
  Create a license attribue
### Instance Properties
- [var duration: UInt64](aldlicenseattribute/duration.md)
  The maximum amount of time, in seconds, that iOS considers the license valid.
- [var issuedTime: UInt64](aldlicenseattribute/issuedtime.md)
### Instance Methods
- [func addAppKey(ALDAppKey) throws](aldlicenseattribute/addappkey(_:).md)
  Add an AppKey to be associated with this license
- [func revokeAppleItemID(UInt64) throws](aldlicenseattribute/revokeappleitemid(_:).md)
  An appleItemID to be revoked by the license

## See Also

- [Licensing alternative distribution apps](licensing-alternative-distribution-apps.md)
  Build a license server that supports the installation of your apps and the apps available in your marketplace.
- [Renewing and revoking app licenses](renewing-and-revoking-app-licenses.md)
  Determine whether an app for which you issue a license launches.
- [struct ALDAppKey](aldappkey.md)
  A structure that identifies an app and a key that’s required to decrypt the app’s license request.
- [class ALDProvider](aldprovider.md)
  An object that creates a session with the alternative app marketplace’s signing assets.
- [class ALDSession](aldsession.md)
  A structure that contains the details of a license request and methods to generate license responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicensedeliverysdk/aldlicenseattribute)*