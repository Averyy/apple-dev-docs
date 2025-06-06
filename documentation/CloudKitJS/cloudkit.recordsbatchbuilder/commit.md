# commit

**Framework**: CloudKit JS  
**Kind**: method

Executes the operations on the database that created this batch builder object.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.RecordsResponse, CloudKit.CKError> commit();
```

#### Return Value

A `Promise` object that resolves to a RecordsResponse object if the operation succeeds; otherwise, a [`CKError`](cloudkit/ckerror.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.recordsbatchbuilder/commit)*