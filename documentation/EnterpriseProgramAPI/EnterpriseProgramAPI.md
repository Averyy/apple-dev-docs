# Enterprise Program API

**Framework**: Enterprise Program API  
**Kind**: module

Automate the tasks you perform on the Apple Developer website.

#### Overview

The Enterprise Program API is a REST API that enables the automation of actions you take on the [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com). Click [`OpenAPI specification`](https://developer.apple.comhttp://developer.apple.com/sample-code/enterprise/enterprise-program-openapi-oas.zip) to download the specification file.

Calls to the API require JSON Web Tokens (JWT) for authorization; you obtain keys to create the tokens from your organization’s Enterprise Program account. See [`Creating API Keys for Enterprise Program API`](creating-api-keys-for-enterprise-program-api.md) to create your keys and tokens.

> ❗ **Important**:  Changes you make using the Enterprise Program API affect the production data you use for development and distribution.

 Changes you make using the Enterprise Program API affect the production data you use for development and distribution.

The API provides resources to automate the following areas of the [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com):

- . Manage bundle IDs, capabilities, signing certificates, devices, and provisioning profiles.
- . Send invitations for users to join your team. Adjust their level of access or remove users.

The Enterprise Program API returns responses from resources that are consistent JSON data and contain links to additional related resources.

## Topics

### Essentials
- [Creating API Keys for Enterprise Program API](creating-api-keys-for-enterprise-program-api.md)
  Create API keys to sign JSON Web Tokens (JWTs) and authorize API requests.
- [Generating Tokens for API Requests](generating-tokens-for-api-requests.md)
  Create JSON Web Tokens (JWTs) signed with your private key to authorize API requests.
- [Revoking API Keys](revoking-api-keys.md)
  Revoke unused, lost, or compromised private keys.
- [Identifying Rate Limits](identifying-rate-limits.md)
  Recognize the rate limits that REST API responses provide and handle them in your code.
- [Enterprise Program API Release Notes](enterprise-api-release-notes.md)
  Learn about new features and updates in the Enterprise Program API.
### Provisioning
- [Bundle IDs](bundle-ids.md)
  Manage the bundle IDs that uniquely identify your apps.
- [Bundle ID Capabilities](bundle-id-capabilities.md)
  Manage the app capabilities for a bundle ID.
- [Certificates](certificates.md)
  Create, download, and revoke signing certificates for app development and distribution.
- [Devices](devices.md)
  Register devices for development and testing.
- [Pass Type Ids](passtypeids.md)
  Create, download, and revoke pass type ids for app development and distribution.
- [Profiles](profiles.md)
  Create, delete, and download provisioning profiles for development and distribution.
### Users and Roles
- [Users](users.md)
  Manage users on your Enterprise Program team.
- [User Invitations](user-invitations.md)
  Email invitations to join your Enterprise Program team.
### Error Handling
- [Interpreting and Handling Errors](interpreting-and-handling-errors.md)
  Learn how the Enterprise Program API returns errors and handle them in your code.
- [object ErrorResponse](errorresponse.md)
  The error details that an API returns in the response body whenever the API request isn’t successful.
### Paging
- [Large Data Sets](large-data-sets.md)
  Retrieve large data sets with paging information.
### Dictionaries
- [object JsonPointer](jsonpointer.md)
  An object that contains the JSON pointer that indicates the location of the error.
- [object Parameter](parameter.md)
  An object that contains the query parameter that produced the error.
- [object RelationshipLinks](relationshiplinks.md)
  The links to the related data and the relationship’s self-link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/EnterpriseProgramAPI)*