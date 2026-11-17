# PHPhotosUIError.Code

**Framework**: PhotosUI  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
enum Code
```

```c
enum PHPhotosUIError : NSInteger;
```

## Overview

Error codes delivered via `PHPhotosUIErrorDomain` describing why an operation failed.

Every error in this domain carries a user-presentable `localizedDescription`.

## Topics

### Enumeration Cases
- [PHPhotosUIError.Code.assetCollectionCreationFailed](./code/assetcollectioncreationfailed.md)
  Album creation did not produce an asset collection.
- [PHPhotosUIError.Code.assetCollectionNotFound](./code/assetcollectionnotfound.md)
  No album could be resolved for the supplied local identifier in the specified photo library.
- [PHPhotosUIError.Code.assetCollectionNotWritable](./code/assetcollectionnotwritable.md)
  The user does not have permission to add content to the target album.
- [PHPhotosUIError.Code.iCloudPhotosNotEnabled](./code/icloudphotosnotenabled.md)
  The requested operation requires iCloud Photos, which is not enabled on this device.
- [PHPhotosUIError.Code.sharedAlbumMigrationInProgress](./code/sharedalbummigrationinprogress.md)
  The target shared album is in the process of migrating and can’t accept new content until migration completes.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phphotosuierror-swift.struct/code)*