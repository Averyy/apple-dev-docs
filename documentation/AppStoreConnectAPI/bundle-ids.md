# Bundle IDs

**Framework**: App Store Connect API

Manage the bundle IDs that uniquely identify your apps.

#### Overview

The `bundleIds` resource represents the app’s unique identifier that you can register, modify, and delete. You need a bundle ID before you can assign capabilities with the [`Bundle ID Capabilities`](bundle-id-capabilities.md) resource or create a provisioning profile with the [`Profiles`](profiles.md) resource.

## Topics

### Registering Bundle IDs
- [Register a New Bundle ID](post-v1-bundleids.md)
  Register a new bundle ID for app development.
### Modifying and Removing Bundle IDs
- [Modify a Bundle ID](patch-v1-bundleids-_id_.md)
  Update a specific bundle ID’s name.
- [Delete a Bundle ID](delete-v1-bundleids-_id_.md)
### Getting Bundle ID Information
- [List Bundle IDs](get-v1-bundleids.md)
  Find and list bundle IDs that are registered to your team.
- [Read Bundle ID Information](get-v1-bundleids-_id_.md)
  Get information about a specific bundle ID.
### Getting Related Data
- [Read the App Information of a Bundle ID](get-v1-bundleids-_id_-app.md)
- [List All Profiles for a Bundle ID](get-v1-bundleids-_id_-profiles.md)
  Get a list of all profiles for a specific bundle ID.
- [List All Capabilities for a Bundle ID](get-v1-bundleids-_id_-bundleidcapabilities.md)
  Get a list of all capabilities for a specific bundle ID.
### Objects and Types
- [object BundleId](bundleid.md)
  The data structure that represents a Bundle IDs resource.
- [type BundleIdPlatform](bundleidplatform.md)
  Strings that represent the operating system intended for the bundle.
- [object BundleIdCreateRequest](bundleidcreaterequest.md)
  The request body you use to create a Bundle ID.
- [object BundleIdUpdateRequest](bundleidupdaterequest.md)
  The request body you use to update a Bundle ID.
- [object BundleIdResponse](bundleidresponse.md)
  A response that contains a single Bundle IDs resource.
- [object BundleIdWithoutIncludesResponse](bundleidwithoutincludesresponse.md)
- [object BundleIdsResponse](bundleidsresponse.md)
  A response that contains a list of Bundle ID resources.

## See Also

- [Bundle ID Capabilities](bundle-id-capabilities.md)
  Manage the app capabilities for a bundle ID.
- [Certificates](certificates.md)
  Create, download, and revoke signing certificates for app development and distribution.
- [Devices](devices.md)
  Register devices for development and testing.
- [Profiles](profiles.md)
  Create, delete, and download provisioning profiles that enable app installations for development and distribution.
- [Merchant ID](merchantids.md)
  Manage your merchant ID for Apple Pay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/bundle-ids)*