# groupUUID

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The group `UUID` of the file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var groupUUID: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * groupUUID;
```

## See Also

### Inspecting a File’s Identity
- [var relatedUUID: String?](./relateduuid.md)
  A related UUID correlating several images from an Apple device.
- [var originatingAssetID: String?](./originatingassetid.md)
  The originating asset ID of an `HEIF` or `HVEC` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile/groupuuid)*