# VppUser

**Framework**: Device Management  
**Kind**: dictionary

A user within the purchase program.

**Availability**:
- VPP License Management 1.0+

## Declaration

```swift
object VppUser
```

## Properties

- `clientUserIdStr` (string): The identifier supplied by the client when registering a user. An identifier must be unique within the organization.
- `email` (string): The user’s email address.
- `itsIdHash` (string): The hash of the user’s iTunes Store ID. The `itsIdHash` field is included only when the user is associated with an iTunes Store account.
- `licenses` ([VppLicense]): The list of licenses which have been assigned to this user.
- `status` (string): The status of the user’s account in VPP. Possible values are: - `Registered`: Indicates the user has been created, but is not yet associated with an iTunes account.
- `Associated`: Indicates that the user has been associated with an iTunes account. When a user is associated with an iTunes account, an `itsIdHash` is generated for the user.
- `Retired`: Indicates the user has been retired via  [`Retire a User`](retire-a-user.md).
- `Deleted`: Indicates that a VPP user is retired and its associated iTunes user has since been invited and associated with a new VPP user that shares the same `clientUserIdStr`. Because there are two VPP users with distinct `userId` values but the same `clientUserIdStr` value, the Deleted status is used to ensure database consistency. A user with a `Deleted` status will never change status; its sole purpose is to ensure that your software can recognize that the userId is no longer associated with the `clientUserIdStr` record, and update any internal references appropriately.
- `userId` (int64): The unique identifier assigned by the VPP when registering the user.

## See Also

- [object VppAsset](vppasset.md)
  A particular asset in the purchase program.
- [object VppAssignment](vppassignment.md)
  An assignment’s properties and their values.
- [object VppLicense](vpplicense.md)
  A license for a product in the purchase program.
- [object VppAssociation](vppassociation.md)
  An association between a license and a user or device.
- [object VppLocation](vpplocation.md)
  A location used for managing purchases.
- [object VppErrorCode](vpperrorcode.md)
  An error code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vppuser)*