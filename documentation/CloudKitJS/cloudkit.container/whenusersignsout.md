# whenUserSignsOut

**Framework**: CloudKit JS  
**Kind**: method

Returns an object representing a deferred or asynchronous operation that resolves when the user signs out.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<Undefined, CloudKit.CKError> whenUserSignsOut();
```

#### Return Value

A `Promise` object that resolves to `Undefined` when the user signs out, or rejects to a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

Use the [`whenUserSignsOut`](cloudkit.container/whenusersignsout.md) method to call a function when the user signs out.

```javascript
myContainer.whenUserSignsOut().then(function() {
    // The user signed out
});
```

## See Also

- [setUpAuth](cloudkit.container/setupauth.md)
  Determines whether a user is signed in and presents an appropriate sign in or sign out button.
- [whenUserSignsIn](cloudkit.container/whenusersignsin.md)
  Returns an object representing a deferred or asynchronous operation that resolves when the user signs in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/whenusersignsout)*