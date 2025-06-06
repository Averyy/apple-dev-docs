# whenUserSignsIn

**Framework**: CloudKit JS  
**Kind**: method

Returns an object representing a deferred or asynchronous operation that resolves when the user signs in.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.UserIdentity, CloudKit.CKError> whenUserSignsIn();
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.UserIdentity`](cloudkit.useridentity.md) dictionary when the user signs in, or rejects to a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

Use the [`whenUserSignsIn`](cloudkit.container/whenusersignsin.md) method to call a function when the user signs in.

```javascript
myContainer.whenUserSignsIn().then(function(userIdentity) {
    // The user signed in
});
```

## See Also

- [setUpAuth](cloudkit.container/setupauth.md)
  Determines whether a user is signed in and presents an appropriate sign in or sign out button.
- [whenUserSignsOut](cloudkit.container/whenusersignsout.md)
  Returns an object representing a deferred or asynchronous operation that resolves when the user signs out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/whenusersignsin)*