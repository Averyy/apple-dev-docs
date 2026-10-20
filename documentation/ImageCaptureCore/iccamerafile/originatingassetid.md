# originatingAssetID

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The originating asset ID of an `HEIF` or `HVEC` file.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
var originatingAssetID: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * originatingAssetID;
```

## See Also

### Inspecting a File’s Identity
- [var groupUUID: String?](./groupuuid.md)
  The group `UUID` of the file.
- [var relatedUUID: String?](./relateduuid.md)
  A related UUID correlating several images from an Apple device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile/originatingassetid)*