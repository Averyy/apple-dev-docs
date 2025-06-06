# relatedUUID

**Framework**: ImageCaptureCore  
**Kind**: property

A related UUID correlating several images from an Apple device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var relatedUUID: String? { get }
```

#### Discussion

This value is the same for both the image and video of a LivePhoto.

## See Also

- [var groupUUID: String?](iccamerafile/groupuuid.md)
  The group `UUID` of the file.
- [var originatingAssetID: String?](iccamerafile/originatingassetid.md)
  The originating asset ID of an `HEIF` or `HVEC` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile/relateduuid)*