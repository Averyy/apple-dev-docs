# fetchCurrentUserIdentity

**Framework**: CloudKit JS  
**Kind**: method  
**Role**: Instance Method

Fetches information about the current user asynchronously.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
Promise<CloudKit.UserIdentity, CloudKit.CKError> fetchCurrentUserIdentity();
```

## Return Value

A `Promise` object that resolves to a [`CloudKit.UserIdentity`](../cloudkit.useridentity.md) dictionary if the current user is found, or rejects to a [`CKError`](../cloudkit/ckerror.md) object.

## Discussion

If the current user is discoverable, the [`CloudKit.UserIdentity`](../cloudkit.useridentity.md) dictionary contains a `nameComponents` key that you can use to get the user’s first and last name.

## See Also

### Discovering Users
- [discoverAllUserIdentities](./discoveralluseridentities.md)
  Fetches all user identities in the current user’s address book.
- [discoverUserIdentities](./discoveruseridentities.md)
  Fetches all users in the specified array.
- [discoverUserIdentityWithEmailAddress](./discoveruseridentitywithemailaddress.md)
  Fetches information about a single user based on the user’s email address.
- [discoverUserIdentityWithPhoneNumber](./discoveruseridentitywithphonenumber.md)
  Fetches information about a single user based on the user’s phone number.
- [discoverUserIdentityWithUserRecordName](./discoveruseridentitywithuserrecordname.md)
  Fetches information about a single user using the record name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/fetchcurrentuseridentity)*