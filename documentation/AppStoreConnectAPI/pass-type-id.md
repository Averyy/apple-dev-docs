# Pass type Ids

**Framework**: App Store Connect API

Create, download, and revoke pass type ids for app development and distribution.

#### Overview

The `passTypeId` resource represents a pass type certificates unique identifier that you can register, modify, and delete. You need a pass type ID before you can create a pass type certificate with the [`Certificates`](certificates.md) resource.

## Topics

### Managing pass type Ids
- [List PassTypeID Ids for a certificate](get-v1-certificates-_id_-passtypeid.md)
  List all PassTypeID Ids for a specific certificate.
- [GET /v1/certificates/{id}/relationships/passTypeId](get-v1-certificates-_id_-relationships-passtypeid.md)
- [List Pass Type Ids](get-v1-passtypeids.md)
  Find and list pass type IDs that are registered to your team.
- [Read PassTypeId Information](get-v1-passtypeids-_id_.md)
  Get information about a specific pass type ID.
- [List All Certificates for a PassTypeId](get-v1-passtypeids-_id_-certificates.md)
  List all certificates for a specific pass type ID.
- [GET /v1/passTypeIds/{id}/relationships/certificates](get-v1-passtypeids-_id_-relationships-certificates.md)
- [Modify a PassTypeId](patch-v1-passtypeids-_id_.md)
  Update a specific pass type ID’s name.
- [Create a PassTypeId](post-v1-passtypeids.md)
  Create a new identifier for use with a pass type ID certificate using a certificate signing request.
- [Delete a PassTypeId](delete-v1-passtypeids-_id_.md)
  Delete a pass type ID that is used for app distribution.
### Object and data types
- [object CertificatePassTypeIdLinkageResponse](certificatepasstypeidlinkageresponse.md)
  A response body that contains the ID of a single related resource.
- [object PassTypeId](passtypeid.md)
  The data structure that represents a pass type id resource.
- [object PassTypeIdCertificatesLinkagesResponse](passtypeidcertificateslinkagesresponse.md)
  A response that contains a list of pass type id certificates linkages response resources.
- [object PassTypeIdCreateRequest](passtypeidcreaterequest.md)
  The request body you use to create a pass type id create request resource.
- [object PassTypeIdResponse](passtypeidresponse.md)
  A response that contains a single pass type id response resource.
- [object PassTypeIdUpdateRequest](passtypeidupdaterequest.md)
  The request body you use to update a pass type id update request.
- [object PassTypeIdsResponse](passtypeidsresponse.md)
  A response that contains a list of pass type ids response resources.

## See Also

- [Bundle IDs](bundle-ids.md)
  Manage the bundle IDs that uniquely identify your apps.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/pass-type-id)*