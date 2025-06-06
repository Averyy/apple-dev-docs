# discoverUserIdentities

**Framework**: CloudKit JS  
**Kind**: method

Fetches all users in the specified array.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.UserIdentitiesResponse, CloudKit.CKError> discoverUserIdentities(
	CloudKit.UserLookupInfo[] userLookupInfos
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.UserIdentitiesResponse`](cloudkit.useridentitiesresponse.md) object, or rejects to a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

This method returns information about those users who meet the following criteria:

- The user must be in the current user’s address book.
- The user must have run the app.
- The user must have granted the permission to be discovered for this container.

## Parameters

- `userLookupInfos`: Array of information about users to fetch.

## See Also

- [fetchCurrentUserIdentity](cloudkit.container/fetchcurrentuseridentity.md)
  Fetches information about the current user asynchronously.
- [discoverAllUserIdentities](cloudkit.container/discoveralluseridentities.md)
  Fetches all user identities in the current user’s address book.
- [discoverUserIdentityWithEmailAddress](cloudkit.container/discoveruseridentitywithemailaddress.md)
  Fetches information about a single user based on the user’s email address.
- [discoverUserIdentityWithPhoneNumber](cloudkit.container/discoveruseridentitywithphonenumber.md)
  Fetches information about a single user based on the user’s phone number.
- [discoverUserIdentityWithUserRecordName](cloudkit.container/discoveruseridentitywithuserrecordname.md)
  Fetches information about a single user using the record name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/discoveruseridentities)*