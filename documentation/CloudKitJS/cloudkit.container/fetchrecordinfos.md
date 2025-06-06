# fetchRecordInfos

**Framework**: CloudKit JS  
**Kind**: method

Returns information about a record for which you have a `shortGUID` property.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
Promise<CloudKit.RecordInfosResponse, CKError> fetchRecordInfos(
	String[] shortGUIDs
);
```

#### Return Value

A `Promise` object that resolves to a [`CloudKit.RecordInfosResponse`](cloudkit.recordinfosresponse.md) object, or rejects to a [`CKError`](cloudkit/ckerror.md) object.

#### Discussion

Use this method to show details about a record to a user before asking them to accept a share.

## Parameters

- `shortGUIDs`: One or more short GUIDs that represent records you want to fetch information about.

## See Also

- [acceptShares](cloudkit.container/acceptshares.md)
  Accepts a share—that is represented by a `shortGUID`—on behalf of the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.container/fetchrecordinfos)*