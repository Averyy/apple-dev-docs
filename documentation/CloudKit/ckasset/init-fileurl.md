# init(fileURL:)

**Framework**: CloudKit  
**Kind**: init

Creates an asset that references a file.

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
init(fileURL: URL)
```

#### Return Value

An asset object that represents the specified file, or `nil` if the system can’t create the asset.

#### Discussion

Use this method to initialize new file-based assets that you want to transfer to iCloud. After saving an asset to the server, CloudKit doesn’t delete the file at the specified URL. If you no longer need the file, you must delete it yourself. When you subsequently download a record that contains an asset, CloudKit downloads its own copy of the asset data to the local device and provides you with a URL to that file.

You can assign only one record to the asset that this method returns. If you want multiple records to point to the same file, you must create separate assets for each one.

> ❗ **Important**:  CloudKit saves only the contents of the file and doesn’t save the filename or any file-related metadata. To preserve the filename or any file-related metadata, save that data separately in the record.

## Parameters

- `fileURL`: The URL of the file that you want to store in CloudKit. The URL must be a file URL, and must not be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckasset/init(fileurl:))*