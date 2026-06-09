# init(importing:)

**Framework**: CloudKit  
**Kind**: init

Initialize a new [`CKAsset`](ckasset.md) that can be used to create a copy of an asset that already exists in iCloud, potentially in a different container.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
convenience init(importing exportedAssetID: CKAsset.ExportedAssetID)
```

#### Discussion

When this asset is saved, a server-side copy of the referenced asset is created.

The new [`CKAsset`](ckasset.md) does not reference any data on the local device (its [`fileURL`](ckasset/fileurl.md) is `nil`).

When you assign this asset to a field in a [`CKRecord`](ckrecord.md) and save the record, the CloudKit server creates a new asset by copying the contents of the asset identified by the `exportedAssetID`.

If the source asset no longer exists on the server, saving the record fails with [`CKError.Code.unknownItem`](ckerror/code/unknownitem.md).

If the `exportedAssetID` is invalid or expired, saving the record fails with [`CKError.Code.assetNotAvailable`](ckerror/code/assetnotavailable.md).

Assets created this way are supported starting with iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, and visionOS 1.0. Devices running older OS versions may fail to download the created asset.

## Parameters

- `exportedAssetID`: Identifies the source asset that this [`CKAsset`](ckasset.md) will copy. The `exportedAssetID` is only valid on the same device it was created, and it expires after a few days.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckasset/init(importing:))*