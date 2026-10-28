# discoverUserIdentityWithEmailAddress

**Framework**: CloudKit JS  
**Kind**: method  
**Role**: Instance Method

Fetches information about a single user based on the user’s email address.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
Promise<CloudKit.UserIdentitiesResponse, CloudKit.CKError> discoverUserIdentityWithEmailAddress(
	String emailAddress
);
```

## Return Value

A `Promise` object that resolves to [`CloudKit.UserIdentitiesResponse`](../cloudkit.useridentitiesresponse.md) object, or rejects to a [`CKError`](../cloudkit/ckerror.md) object.

## Discussion

Use this method to get the ID of a user based on the user’s email address. The user must meet the following criteria:

- The user must be in the current user’s address book.
- The user must have run the app.
- The user must have granted the permission to be discovered for this container.

## Parameters

- `emailAddress`: The user’s email address.

## See Also

### Discovering Users
- [fetchCurrentUserIdentity](./fetchcurrentuseridentity.md)
  Fetches information about the current user asynchronously.
- [discoverAllUserIdentities](./discoveralluseridentities.md)
  Fetches all user identities in the current user’s address book.
- [discoverUserIdentities](./discoveruseridentities.md)
  Fetches all users in the specified array.
- [discoverUserIdentityWithPhoneNumber](./discoveruseridentitywithphonenumber.md)
  Fetches information about a single user based on the user’s phone number.
- [discoverUserIdentityWithUserRecordName](./discoveruseridentitywithuserrecordname.md)
  Fetches information about a single user using the record name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/discoveruseridentitywithemailaddress)*