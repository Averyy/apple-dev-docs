# shareWithUI

**Framework**: CloudKit JS  
**Kind**: method

Presents a UI to the user which lets them share a record with other users.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.SharingUIResult, CloudKit.CKError> shareWithUI(
	Object options
);
```

#### Return Value

A `Promise` object that resolves to an object that represents the share record, or rejects to a [`CKError`](cloudkit/ckerror.md) object.

## Parameters

- `options`: A dictionary containing options for the share UI:


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.database/sharewithui)*