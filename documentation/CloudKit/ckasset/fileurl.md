# fileURL

**Framework**: CloudKit  
**Kind**: property

The URL for accessing the asset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var fileURL: URL? { get }
```

#### Discussion

After you create an asset, use the URL in this property to access the asset’s contents. The URL in this property is different from the one you specify when creating the asset.

> **Note**:  If a modify operation fails with a [`serverRecordChanged`](ckerror/serverrecordchanged.md) error, CloudKit doesn’t download assets for the copy of the server’s record that’s accessible using the error’s [`serverRecord`](ckerror/serverrecord.md) property. In this scenario, [`fileURL`](ckasset/fileurl.md) is `nil` for all of that record’s asset fields.

 If a modify operation fails with a [`serverRecordChanged`](ckerror/serverrecordchanged.md) error, CloudKit doesn’t download assets for the copy of the server’s record that’s accessible using the error’s [`serverRecord`](ckerror/serverrecord.md) property. In this scenario, [`fileURL`](ckasset/fileurl.md) is `nil` for all of that record’s asset fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckasset/fileurl)*