# whenUserSignsOut

**Framework**: CloudKit JS  
**Kind**: method  
**Role**: Instance Method

Returns an object representing a deferred or asynchronous operation that resolves when the user signs out.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
Promise<Undefined, CloudKit.CKError> whenUserSignsOut();
```

## Return Value

A `Promise` object that resolves to `Undefined` when the user signs out, or rejects to a [`CKError`](../cloudkit/ckerror.md) object.

## Discussion

Use the [`whenUserSignsOut`](./whenusersignsout.md) method to call a function when the user signs out.

```javascript
myContainer.whenUserSignsOut().then(function() {
    // The user signed out
});
```

## See Also

### Authenticating Users
- [setUpAuth](./setupauth.md)
  Determines whether a user is signed in and presents an appropriate sign in or sign out button.
- [whenUserSignsIn](./whenusersignsin.md)
  Returns an object representing a deferred or asynchronous operation that resolves when the user signs in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/whenusersignsout)*