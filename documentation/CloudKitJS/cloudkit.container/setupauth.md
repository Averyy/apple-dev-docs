# setUpAuth

**Framework**: CloudKit JS  
**Kind**: method

Determines whether a user is signed in and presents an appropriate sign in or sign out button.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.UserIdentity, CloudKit.CKError> setUpAuth();
```

#### Return Value

A `Promise` that resolves to a [`CloudKit.UserIdentity`](cloudkit.useridentity.md) dictionary if an active CloudKit session was found; otherwise, `null`. If an error occurs, a `Promise` object that rejects to a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

Use the [`setUpAuth`](cloudkit.container/setupauth.md) method to determine whether the user is authenticated and to display the appropriate button.

```javascript
var myContainer = CloudKit.getDefaultContainer();
 
myContainer.setUpAuth().then(function(userIdentity) {
    if(userIdentity) {
        // The user is authenticated
    }
});
```

In the function, use the `userRecordName` property to get the user record name from the [`CloudKit.UserIdentity`](cloudkit.useridentity.md) parameter.

The [`setUpAuth`](cloudkit.container/setupauth.md) method displays the appropriate buttons only if the required DOM elements are found. If the user is not signed in, the method displays a sign-in button; otherwise, it displays a sign-out button.

You can call this method multiple times. For example, call this method to determine if a previous CloudKit session is still valid, and call this method later to display the buttons after you add the required DOM elements.

## See Also

- [whenUserSignsIn](cloudkit.container/whenusersignsin.md)
  Returns an object representing a deferred or asynchronous operation that resolves when the user signs in.
- [whenUserSignsOut](cloudkit.container/whenusersignsout.md)
  Returns an object representing a deferred or asynchronous operation that resolves when the user signs out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/setupauth)*