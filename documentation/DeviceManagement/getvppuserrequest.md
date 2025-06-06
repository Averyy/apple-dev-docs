# GetVppUserRequest

**Framework**: Device Management  
**Kind**: dictionary

The request for the user details service.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object GetVppUserRequest
```

#### Discussion

Either `clientUserIdStr` or `userId` is required. If `clientUserIdStr` is used, an `itsIdHash` (iTunes Store ID hash) value may be included, but it is optional. If `userId` has a value, only that value is used, and `clientUserIdStr` and `itsIdHash` are ignored.

##### Clientuseridstr

It is possible for more than one user record to exist for the same `clientUserIdStr` value, one for each iTunes account that the `clientUserIdStr` value has been associated with in the past (in addition to a currently active record or a retired and never-associated record). However, no more than one of these records can be active at any given time.

When a new record is associated with a `clientUserIdStr` that was previously associated with a different user, any irrevocable licenses originally associated with the previous user, if any, are moved to the new user (as identified by `userId`) automatically.

If you use a `clientUserIdStr` value to fetch the VPP user after such a reassociation, the status of that user changes from Retired to Associated. If you use `userId` values to fetch the VPP users after the association, the status of the first VPP user changes from Retired to Deleted, and the status of the second VPP user changes from Registered to Associated.

To obtain only the record for the currently active user matching a `clientUserIdStr` value, your MDM server passes the `clientUserIdStr` by itself. If no users for the `clientUserIdStr` are active (all are retired or no matching record exists), `Get User` returns a “result not found” error.

To obtain a retired user record previously associated with an iTunes Store account, your MDM server can pass either the `userId` for that record or the `clientUserIdStr` and `itsIdHash` for that record.

## See Also

- [object GetVppUserResponse](getvppuserresponse.md)
  The response from the user details service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/getvppuserrequest)*