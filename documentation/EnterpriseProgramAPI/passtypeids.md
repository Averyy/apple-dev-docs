# Pass Type Ids

**Framework**: Enterprise Program API

Create, download, and revoke pass type ids for app development and distribution.

#### Overview

The `passTypeId` resource represents a pass type certificates unique identifier that you can register, modify, and delete. You need a pass type ID before you can create a pass type certificate with the [`Certificates`](certificates.md) resource.

## Topics

### Managing Pass Type Ids
- [Create a PassTypeId](create-a-passtypeid.md)
  Create a new identifier for use with a pass type ID certificate using a certificate signing request.
- [List Pass Type Ids](list-pass-type-ids.md)
  Find and list pass type IDs that are registered to your team.
- [Read PassTypeId Information](read-passtypeid-information.md)
  Get information about a specific pass type ID.
- [List All Certificates for a PassTypeId](list-all-certificates-for-a-passtypeid.md)
  List all certificates for a specific pass type ID.
- [Modify a PassTypeId](modify-a-passtypeid.md)
  Update a specific pass type ID’s name.
- [Delete a PassTypeId](delete-a-passtypeid.md)
  Delete a pass type ID that is used for app development.
### Getting Pass Type Id Infomation and Data
- [Read the Pass Type Id Information of a Certificate](read-the-pass-type-id-information-of-a-certificate.md)
### Object and Data Types
- [object PassTypeId](passtypeid.md)
  The data structure that represents a pass type ID.
- [object PassTypeIdCreateRequest](passtypeidcreaterequest.md)
  The request body you use to create a pass type ID.
- [object PassTypeIdResponse](passtypeidresponse.md)
  A response that contains a pass type ID resource.
- [object PassTypeIdsResponse](passtypeidsresponse.md)
  A response that contains a list of pass type ID resources.
- [object PassTypeIdUpdateRequest](passtypeidupdaterequest.md)
  The request body you use to update a pass type ID name.

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
  Create, delete, and download provisioning profiles for development and distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/passtypeids)*