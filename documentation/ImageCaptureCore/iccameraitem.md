# ICCameraItem

**Framework**: ImageCaptureCore  
**Kind**: class

An abstract class that represents a camera item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
class ICCameraItem
```

#### Overview

The ImageCaptureCore framework defines two concrete subclasses of camera items: [`ICCameraFolder`](iccamerafolder.md) and [`ICCameraFile`](iccamerafile.md).

## Topics

### Inspecting an Item’s Name and Type
- [var uti: String?](iccameraitem/uti.md)
  The item’s uniform type identifier (UTI) string.
- [var name: String?](iccameraitem/name.md)
  The item’s name.
- [var ptpObjectHandle: UInt32](iccameraitem/ptpobjecthandle.md)
  The item’s `PTP` object handle value, if the camera uses the `PTP` protocol.
- [var isRaw: Bool](iccameraitem/israw.md)
  A Boolean value indicating whether the item is a raw image file.
### Determining an Item’s Change Dates
- [var creationDate: Date?](iccameraitem/creationdate.md)
  The item’s creation date, usually the same as its `EXIF` creation date.
- [var modificationDate: Date?](iccameraitem/modificationdate.md)
  The item’s modification date, usually the same as its `EXIF` modification date.
- [var wasAddedAfterContentCatalogCompleted: Bool](iccameraitem/wasaddedaftercontentcatalogcompleted.md)
  A Boolean value indicating whether the item was captured on the camera after the camera’s content had been fully enumerated.
### Locating an Item
- [var device: ICCameraDevice?](iccameraitem/device.md)
  The item’s parent device.
- [var fileSystemPath: String?](iccameraitem/filesystempath.md)
  The item’s file system path on a camera using the mass storage transport type.
- [var parentFolder: ICCameraFolder?](iccameraitem/parentfolder.md)
  This item’s parent folder.
- [var isInTemporaryStore: Bool](iccameraitem/isintemporarystore.md)
  A Boolean value that indicates whether this item is in a temporary store.
### Requesting Metadata
- [func requestMetadata()](iccameraitem/requestmetadata.md)
  Requests metadata for the item.
- [var metadata: [AnyHashable : Any]?](iccameraitem/metadata.md)
  The item’s metadata.
- [var metadataIfAvailable: [String : Any]?](iccameraitem/metadataifavailable.md)
  The item’s metadata if it is readily available.
- [func flushMetadataCache()](iccameraitem/flushmetadatacache.md)
  Deletes the item’s cached metadata.
- [struct ICCameraItemMetadataOption](iccameraitemmetadataoption.md)
  An option for the item’s metadata.
### Requesting Thumbnails
- [func requestThumbnail()](iccameraitem/requestthumbnail.md)
  Requests a thumbnail for the item.
- [var thumbnail: CGImage?](iccameraitem/thumbnail.md)
  The item’s thumbnail.
- [var thumbnailIfAvailable: CGImage?](iccameraitem/thumbnailifavailable.md)
  The item’s thumbnail if it is readily available.
- [var largeThumbnailIfAvailable: CGImage?](iccameraitem/largethumbnailifavailable.md)
  A large thumbnail for the item if one is readily available.
- [func flushThumbnailCache()](iccameraitem/flushthumbnailcache.md)
  Deletes the item’s cached thumbnail.
- [struct ICCameraItemThumbnailOption](iccameraitemthumbnailoption.md)
  An option for the item’s thumbnail.
### Accessing a Protected Item
- [var isLocked: Bool](iccameraitem/islocked.md)
  A Boolean value that indicates whether the storage card in the camera is locked.
### Storing Information
- [var userData: NSMutableDictionary?](iccameraitem/userdata.md)
  A mutable dictionary to store arbitrary key-value pairs associated with a camera item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ICCameraFile](iccamerafile.md)
- [ICCameraFolder](iccamerafolder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ICCameraDevice](iccameradevice.md)
  An object that represents a camera.
- [protocol ICCameraDeviceDelegate](iccameradevicedelegate.md)
  Methods for detecting cameras, getting metadata and thumbnails, handling access and capability changes, and performing other actions on connected cameras.
- [class ICCameraFile](iccamerafile.md)
  An object that represents a file on a camera.
- [class ICCameraFolder](iccamerafolder.md)
  An object that represents a folder on a camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameraitem)*