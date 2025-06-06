# discoverAllUserIdentities

**Framework**: CloudKit JS  
**Kind**: method

Fetches all user identities in the current user’s address book.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.UserIdentitiesResponse, CloudKit.CKError> discoverAllUserIdentities();
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.UserIdentitiesResponse`](cloudkit.useridentitiesresponse.md) object, or rejects to a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

Use this method to retrieve information about other users of the app. This method returns information about those users who meet the following criteria:

- The user must be in the current user’s address book.
- The user must have run the app.
- The user must have granted the permission to be discovered for this container.

To get the user identities, use the `users` property in the [`CloudKit.UserIdentitiesResponse`](cloudkit.useridentitiesresponse.md) class, which contains an array of [`CloudKit.UserIdentity`](cloudkit.useridentity.md) dictionaries.

```javascript
myContainer.discoverAllUserIdentities().then(function(response) {
    if(response.hasErrors) {
        // Insert error handling
        throw response.errors[0];
    } else {
        // Insert successfully discovered user code
        var users = response.users;
    }
  });
```

## See Also

- [fetchCurrentUserIdentity](cloudkit.container/fetchcurrentuseridentity.md)
  Fetches information about the current user asynchronously.
- [discoverUserIdentities](cloudkit.container/discoveruseridentities.md)
  Fetches all users in the specified array.
- [discoverUserIdentityWithEmailAddress](cloudkit.container/discoveruseridentitywithemailaddress.md)
  Fetches information about a single user based on the user’s email address.
- [discoverUserIdentityWithPhoneNumber](cloudkit.container/discoveruseridentitywithphonenumber.md)
  Fetches information about a single user based on the user’s phone number.
- [discoverUserIdentityWithUserRecordName](cloudkit.container/discoveruseridentitywithuserrecordname.md)
  Fetches information about a single user using the record name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/discoveralluseridentities)*