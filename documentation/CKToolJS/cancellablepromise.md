# CancellablePromise

**Framework**: CKTool JS  
**Kind**: class

A promise that has a function to cancel its operation.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface CancellablePromise
```

#### Overview

This class wraps an ordinary promise, but also provides a method that can be used to cancel the promise. The `cancel` function throws `CancelledError` if called.

API object methods return a promise of this type. For example, `PromisesApi` has a `createRecord` method that returns a `CancellablePromise`.

## Topics

### Initializers
- [CancellablePromise](cancellablepromise/cancellablepromise.md)
### Instance Properties
- [inner](cancellablepromise/inner.md)
  The wrapped promise.
### Instance Methods
- [cancel](cancellablepromise/cancel.md)
  Stops any work the promise is doing.
- [catch](cancellablepromise/catch.md)
  Tells `CancellablePromise` what callback to call on failure of the inner promise.
- [finally](cancellablepromise/finally.md)
  Tells `CancellablePromise` what callback to call when the inner promise either succeeds or fails.
- [then](cancellablepromise/then.md)
  Tells `CancellablePromise` what callbacks to call on success or failure of the inner promise.

## See Also

- [PromisesApi](promisesapi.md)
  A class that exposes promise-based functions for interacting with the API.
- [CKToolDatabaseModule](cktooldatabasemodule.md)
  The imported package that provides access to CloudKit containers and databases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cancellablepromise)*