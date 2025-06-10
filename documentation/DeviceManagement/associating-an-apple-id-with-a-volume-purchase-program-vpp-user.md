# Associating an Apple ID with a Volume Purchase Program (VPP) User

**Framework**: Device Management

Manage Apple IDs within your organization effectively.

#### Overview

When a user’s managed Apple ID is tied to the same organization as the content manager’s Apple ID, the MDM server may associate the user’s managed Apple ID with the given VPP user. This removes the need to send out an invitation (email or push) to users and wait for them to join by going through an acceptance process.

##### Managed Apple Ids

Managed Apple IDs may be associated with a VPP user by adding the optional parameter `managedAppleIDStr` to the requests for the following endpoints:

- [`Register a User`](register-a-user.md)
- [`Edit a User`](edit-a-user.md)

These endpoints use the Apple ID passed in by the `managedAppleIDStr` parameter to look up the userʼs organization. If the content manager associated with the sToken provided in the request is also a managed Apple ID, and that Apple IDʼs organization is the same as the userʼs, the VPP user will be linked to the supplied Apple ID.

If the user’s Apple ID cannot be found in the iTunes database, or if the user is found but the userʼs organization does not match the organization of the `sToken`, the endpoint will return the error `9635,` meaning the Apple ID can’t be used.

> **Note**:  Managed Apple IDs were introduced in iOS 9.3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/associating-an-apple-id-with-a-volume-purchase-program-vpp-user)*