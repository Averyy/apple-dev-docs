# acceptShares

**Framework**: CloudKit JS  
**Kind**: method

Accepts a share—that is represented by a `shortGUID`—on behalf of the current user.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.RecordInfosResponse, CKError> acceptShares(
	String[] shortGUIDs
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.RecordInfosResponse`](cloudkit.recordinfosresponse.md) object, or rejects to a [`CKError`](cloudkit/ckerror.md) object.

## Parameters

- `shortGUIDs`: One or more short GUIDs that represent shared records.

## See Also

- [fetchRecordInfos](cloudkit.container/fetchrecordinfos.md)
  Returns information about a record for which you have a `shortGUID` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/acceptshares)*