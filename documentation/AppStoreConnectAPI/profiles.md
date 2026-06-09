# Profiles

**Framework**: App Store Connect API

Create, delete, and download provisioning profiles that enable app installations for development and distribution.

#### Overview

The `profiles` resource represents the provisioning profiles that allow you to install apps on your iOS devices or Mac. You can create and delete provisioning profiles, and download them to sign your code.

Provisioning profiles include signing certificates, device identifiers, and a bundle ID.

## Topics

### Creating and Deleting Provisioning Profiles
- [Create a profile](post-v1-profiles.md)
  Create a new provisioning profile.
- [Delete a profile](delete-v1-profiles-_id_.md)
  Delete a provisioning profile that is used for app development or distribution.
### Getting Provisioning Profile Information
- [List and download profiles](get-v1-profiles.md)
  Find and list provisioning profiles and download their data.
- [Read and download profile information](get-v1-profiles-_id_.md)
  Get information for a specific provisioning profile and download its data.
### Getting Related Data
- [Read the bundle id in a profile](get-v1-profiles-_id_-bundleid.md)
  Get the bundle ID information for a specific provisioning profile.
- [Get the bundle ID for a profile](get-v1-profiles-_id_-relationships-bundleid.md)
- [List all certificates in a profile](get-v1-profiles-_id_-certificates.md)
  Get a list of all certificates and their data for a specific provisioning profile.
- [List certificate IDs for a profile](get-v1-profiles-_id_-relationships-certificates.md)
- [List all devices in a profile](get-v1-profiles-_id_-devices.md)
  Get a list of all devices for a specific provisioning profile.
- [List device IDs for a profile](get-v1-profiles-_id_-relationships-devices.md)
### Objects
- [object Profile](profile.md)
  A provisioning profile that authorizes specific devices to run an app during development or distribution.
- [object ProfileCreateRequest](profilecreaterequest.md)
  The request body you use to create a Profile.
- [object ProfileResponse](profileresponse.md)
  The response body for endpoints that create or read a single provisioning profile.
- [object ProfilesResponse](profilesresponse.md)
  The response body for endpoints that list provisioning profiles.
- [object ProfilesWithoutIncludesResponse](profileswithoutincludesresponse.md)
  A response containing a list of provisioning profiles, without related resources.
- [object ProfileBundleIdLinkageResponse](profilebundleidlinkageresponse.md)
- [object ProfileCertificatesLinkagesResponse](profilecertificateslinkagesresponse.md)
- [object ProfileDevicesLinkagesResponse](profiledeviceslinkagesresponse.md)

## See Also

- [Bundle IDs](bundle-ids.md)
  Manage the bundle IDs that uniquely identify your apps.
- [Bundle ID Capabilities](bundle-id-capabilities.md)
  Manage the app capabilities for a bundle ID.
- [Certificates](certificates.md)
  Create, download, and revoke signing certificates for app development and distribution.
- [Devices](devices.md)
  Register devices for development and testing.
- [Merchant ID](merchantids.md)
  Manage your merchant ID for Apple Pay.
- [Pass type Ids](pass-type-id.md)
  Create, download, and revoke pass type ids for app development and distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/profiles)*