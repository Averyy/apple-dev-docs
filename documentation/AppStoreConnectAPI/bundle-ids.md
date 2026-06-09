# Bundle IDs

**Framework**: App Store Connect API

Manage the bundle IDs that uniquely identify your apps.

#### Overview

The `bundleIds` resource represents the app’s unique identifier that you can register, modify, and delete. You need a bundle ID before you can assign capabilities with the [`Bundle ID Capabilities`](bundle-id-capabilities.md) resource or create a provisioning profile with the [`Profiles`](profiles.md) resource.

## Topics

### Registering Bundle IDs
- [Register a new bundle id](post-v1-bundleids.md)
  Register a new bundle ID for app development.
### Modifying and Removing Bundle IDs
- [Modify a bundle id](patch-v1-bundleids-_id_.md)
  Update a specific bundle ID’s name.
- [Delete a bundle id](delete-v1-bundleids-_id_.md)
### Getting Bundle ID Information
- [List bundle ids](get-v1-bundleids.md)
  Find and list bundle IDs that are registered to your team.
- [Read bundle id information](get-v1-bundleids-_id_.md)
  Get information about a specific bundle ID.
### Getting Related Data
- [Read the app information of a bundle id](get-v1-bundleids-_id_-app.md)
- [List all profiles for a bundle id](get-v1-bundleids-_id_-profiles.md)
  Get a list of all profiles for a specific bundle ID.
- [List all capabilities for a bundle id](get-v1-bundleids-_id_-bundleidcapabilities.md)
  Get a list of all capabilities for a specific bundle ID.
- [Get the app ID for a bundle ID](get-v1-bundleids-_id_-relationships-app.md)
- [Read bundle Id capabilities ids for a bundle Id](get-v1-bundleids-_id_-relationships-bundleidcapabilities.md)
  List all bundleIdCapabilities IDs for a specific bundle Id.
- [List profile IDs for a bundle ID](get-v1-bundleids-_id_-relationships-profiles.md)
### Objects and types
- [object BundleId](bundleid.md)
  An App ID registered with Apple, associating a specific bundle identifier with capabilities and provisioning profiles.
- [type BundleIdPlatform](bundleidplatform.md)
  Strings that represent the operating system intended for the bundle.
- [object BundleIdCreateRequest](bundleidcreaterequest.md)
  The request body you use to create a Bundle ID.
- [object BundleIdUpdateRequest](bundleidupdaterequest.md)
  The request body you use to update a Bundle ID.
- [object BundleIdResponse](bundleidresponse.md)
  The response body for endpoints that create, read, or modify a single bundle ID.
- [object BundleIdWithoutIncludesResponse](bundleidwithoutincludesresponse.md)
  A response containing a single bundle ID, without including capability and profile details.
- [object BundleIdsResponse](bundleidsresponse.md)
  The response body for endpoints that list bundle IDs.
- [object BundleIdAppLinkageResponse](bundleidapplinkageresponse.md)
- [object BundleIdBundleIdCapabilitiesLinkagesResponse](bundleidbundleidcapabilitieslinkagesresponse.md)
- [object BundleIdProfilesLinkagesResponse](bundleidprofileslinkagesresponse.md)

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
- [Pass type Ids](pass-type-id.md)
  Create, download, and revoke pass type ids for app development and distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/bundle-ids)*