# ALDLicenseAttribute

**Framework**: App License Delivery SDK  
**Kind**: struct  
**Role**: Structure

A structure that defines the requested license type for the session.

## Declaration

```swift
struct ALDLicenseAttribute
```

## Topics

### Initializers
- [init(licenseID: UInt64)](./aldlicenseattribute/init%28licenseid%29.md)
  Create a license attribue
### Instance Properties
- [var duration: UInt64](./aldlicenseattribute/duration.md)
  The maximum amount of time, in seconds, that iOS considers the license valid.
- [var issuedTime: UInt64](./aldlicenseattribute/issuedtime.md)
### Instance Methods
- [func addAppKey(ALDAppKey) throws](./aldlicenseattribute/addappkey%28_%29.md)
  Add an AppKey to be associated with this license
- [func revokeAppleItemID(UInt64) throws](./aldlicenseattribute/revokeappleitemid%28_%29.md)
  An appleItemID to be revoked by the license

## See Also

### App licensing
- [Licensing alternative distribution apps](./licensing-alternative-distribution-apps.md)
  Build a license server that supports the installation of your apps and the apps available in your marketplace.
- [Renewing and revoking app licenses](./renewing-and-revoking-app-licenses.md)
  Determine whether an app for which you issue a license launches.
- [struct ALDAppKey](./aldappkey.md)
  A structure that identifies an app and a key that’s required to decrypt the app’s license request.
- [class ALDProvider](./aldprovider.md)
  An object that creates a session with the alternative app marketplace’s signing assets.
- [class ALDSession](./aldsession.md)
  A structure that contains the details of a license request and methods to generate license responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicensedeliverysdk/aldlicenseattribute)*