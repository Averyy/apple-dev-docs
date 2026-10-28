# discoverUserIdentityWithUserRecordName

**Framework**: CloudKit JS  
**Kind**: method  
**Role**: Instance Method

Fetches information about a single user using the record name.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
Promise<CloudKit.UserIdentitiesResponse, CloudKit.CKError> discoverUserIdentityWithUserRecordName(
	String userRecordName
);
```

## Return Value

A `Promise` object that resolves to [`CloudKit.UserIdentitiesResponse`](../cloudkit.useridentitiesresponse.md) object, or rejects to a [`CKError`](../cloudkit/ckerror.md) object.

## Discussion

Use this method to retrieve information about a user for whom you have the corresponding `name` property of the `User` record. The user must meet the following criteria:

- The user must be in the current user’s address book.
- The user must have run the app.
- The user must have granted the permission to be discovered for this container.

## Parameters

- `userRecordName`: The name of the user record.

## See Also

### Discovering Users
- [fetchCurrentUserIdentity](./fetchcurrentuseridentity.md)
  Fetches information about the current user asynchronously.
- [discoverAllUserIdentities](./discoveralluseridentities.md)
  Fetches all user identities in the current user’s address book.
- [discoverUserIdentities](./discoveruseridentities.md)
  Fetches all users in the specified array.
- [discoverUserIdentityWithEmailAddress](./discoveruseridentitywithemailaddress.md)
  Fetches information about a single user based on the user’s email address.
- [discoverUserIdentityWithPhoneNumber](./discoveruseridentitywithphonenumber.md)
  Fetches information about a single user based on the user’s phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/discoveruseridentitywithuserrecordname)*