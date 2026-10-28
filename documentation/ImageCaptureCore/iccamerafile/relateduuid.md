# relatedUUID

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) NSString * relatedUUID;
```

## Discussion

This value is the same for both the image and video of a LivePhoto.

## See Also

### Inspecting a File’s Identity
- [var groupUUID: String?](./groupuuid.md)
  The group `UUID` of the file.
- [var originatingAssetID: String?](./originatingassetid.md)
  The originating asset ID of an `HEIF` or `HVEC` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile/relateduuid)*