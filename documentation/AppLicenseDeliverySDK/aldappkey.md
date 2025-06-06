# ALDAppKey

**Framework**: App License Delivery SDK  
**Kind**: struct

A structure that identifies an app and a key that’s required to decrypt the app’s license request.

## Declaration

```swift
struct ALDAppKey
```

#### Overview

An instance of this structure represents a unique variant for an app. The [`AppleItemID`](https://developer.apple.com/documentation/MarketplaceKit/AppleItemID) argument to the [`init(appleItemID:appKeyBlob:)`](aldappkey/init(appleitemid:appkeyblob:).md) initializer refers to the app, and the `appKeyBlob` argument refers to a  for a specific app variant that App Store Connect provides your marketplace server during app ingestion. For more information, see [`Ingesting an alternative distribution package`](https://developer.apple.com/documentation/appdistribution/ingesting-an-alternative-distribution-package).

## Topics

### Initializers
- [init(appleItemID: UInt64, appKeyBlob: [UInt8]) throws](aldappkey/init(appleitemid:appkeyblob:).md)
  Creates an app key to decrypt a license request.

## See Also

- [Licensing alternative distribution apps](licensing-alternative-distribution-apps.md)
  Build a license server that supports the installation of your apps and the apps available in your marketplace.
- [Renewing and revoking app licenses](renewing-and-revoking-app-licenses.md)
  Determine whether an app for which you issue a license launches.
- [struct ALDLicenseAttribute](aldlicenseattribute.md)
  A structure that defines the requested license type for the session.
- [class ALDProvider](aldprovider.md)
  An object that creates a session with the alternative app marketplace’s signing assets.
- [class ALDSession](aldsession.md)
  A structure that contains the details of a license request and methods to generate license responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicensedeliverysdk/aldappkey)*