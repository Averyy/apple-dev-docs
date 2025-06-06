# ICCameraFile

**Framework**: ImageCaptureCore  
**Kind**: class

An object that represents a file on a camera.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
class ICCameraFile
```

## Topics

### Requesting Metadata
- [func requestMetadataDictionary(options: [ICCameraItemMetadataOption : Any]?, completion: ([AnyHashable : Any]?, (any Error)?) -> Void)](iccamerafile/requestmetadatadictionary(options:completion:).md)
  Requests metadata and executes the completion block in place of the delegate.
### Requesting Thumbnails
- [func requestThumbnailData(options: [ICCameraItemThumbnailOption : Any]?, completion: (Data?, (any Error)?) -> Void)](iccamerafile/requestthumbnaildata(options:completion:).md)
  Requests a thumbnail and executes the completion block in place of the delegate.
### Requesting Downloads
- [func requestDownload(options: [ICDownloadOption : Any]?, completion: (String?, (any Error)?) -> Void) -> Progress?](iccamerafile/requestdownload(options:completion:).md)
  Requests a download and executes the completion block in place of the delegate.
### Requesting Data
- [func requestReadData(atOffset: off_t, length: off_t, completion: (Data?, (any Error)?) -> Void)](iccamerafile/requestreaddata(atoffset:length:completion:).md)
  Requests to asynchronously read data of a specified length from a specified offset, then executes the completion block.
### Inspecting a File’s Name
- [var originalFilename: String?](iccamerafile/originalfilename.md)
  The original name of the file on disk.
- [var createdFilename: String?](iccamerafile/createdfilename.md)
  The created name of the file.
### Inspecting a File’s Identity
- [var groupUUID: String?](iccamerafile/groupuuid.md)
  The group `UUID` of the file.
- [var relatedUUID: String?](iccamerafile/relateduuid.md)
  A related UUID correlating several images from an Apple device.
- [var originatingAssetID: String?](iccamerafile/originatingassetid.md)
  The originating asset ID of an `HEIF` or `HVEC` file.
### Determining When a File Was Created or Modified
- [var fileCreationDate: Date?](iccamerafile/filecreationdate.md)
  The creation date of the file.
- [var fileModificationDate: Date?](iccamerafile/filemodificationdate.md)
  The modification date of the file.
### Inspecting a File’s Size
- [var fileSize: off_t](iccamerafile/filesize.md)
  The size of the file, in bytes.
### Inspecting a File’s Dimensions
- [var width: Int](iccamerafile/width.md)
  The width of an image or movie frame.
- [var height: Int](iccamerafile/height.md)
  The height of an image or movie frame.
### Inspecting a File’s EXIF Data
- [var orientation: ICEXIFOrientationType](iccamerafile/orientation.md)
  The orientation to use when downloading the image.
- [enum ICEXIFOrientationType](icexiforientationtype.md)
  The file’s orientation type.
- [var exifCreationDate: Date?](iccamerafile/exifcreationdate.md)
  The `EXIF` creation date of the file.
- [var exifModificationDate: Date?](iccamerafile/exifmodificationdate.md)
  The `EXIF` modification date of the file.
### Identifying a File’s Location
- [var gpsString: String?](iccamerafile/gpsstring.md)
  The GPS String of the file in standard format.
### Inspecting a File in a Burst
- [var firstPicked: Bool](iccamerafile/firstpicked.md)
  A Boolean value that indicates whether a file is autopicked by Photos to represent the burst.
- [var burstUUID: String?](iccamerafile/burstuuid.md)
  The burst UUID of the file if it is in a burst.
- [var burstFavorite: Bool](iccamerafile/burstfavorite.md)
  A Boolean value that indicates this file is the burst favorite in a burst.
- [var burstPicked: Bool](iccamerafile/burstpicked.md)
  A Boolean value that indicates whether this file is user picked in a burst.
### Inspecting Video Properties
- [var duration: Double](iccamerafile/duration.md)
  The duration, in seconds, of an audio or video file.
- [var highFramerate: Bool](iccamerafile/highframerate.md)
  A Boolean value that indicates whether the file is a slow motion or high-frame-rate video file.
- [var timeLapse: Bool](iccamerafile/timelapse.md)
  A Boolean value that indicates whether the file is a time-lapse video file.
### Identifying Related Files
- [var sidecarFiles: [ICCameraItem]?](iccamerafile/sidecarfiles.md)
  An array of two camera files associated with this file.
- [var pairedRawImage: ICCameraFile?](iccamerafile/pairedrawimage.md)
  A sidecar file containing the logical `RAW` compliment of a `JPG` or other two-format image.
### Instance Properties
- [var fingerprint: String?](iccamerafile/fingerprint.md)
### Instance Methods
- [func requestFingerprint(completion: (String?, (any Error)?) -> Void)](iccamerafile/requestfingerprint(completion:).md)
- [func requestSecurityScopedURL(completion: (URL?, (any Error)?) -> Void)](iccamerafile/requestsecurityscopedurl(completion:).md)
### Type Methods
- [class func fingerprintForFile(at: URL) -> String?](iccamerafile/fingerprintforfile(at:).md)

## Relationships

### Inherits From
- [ICCameraItem](iccameraitem.md)
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
- [class ICCameraItem](iccameraitem.md)
  An abstract class that represents a camera item.
- [class ICCameraFolder](iccamerafolder.md)
  An object that represents a folder on a camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile)*