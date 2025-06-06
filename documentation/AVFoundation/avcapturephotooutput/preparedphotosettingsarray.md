# preparedPhotoSettingsArray

**Framework**: AVFoundation  
**Kind**: property

An array of photo settings for which the photo output has prepared capture resources.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var preparedPhotoSettingsArray: [AVCapturePhotoSettings] { get }
```

#### Discussion

Some types of photo capture, such as bracketed captures and RAW captures, require the photo output to allocate additional buffers or prepare other resources. To prevent photo capture requests from executing slowly due to lazy resource allocation, you may call the [`setPreparedPhotoSettingsArray(_:completionHandler:)`](avcapturephotooutput/setpreparedphotosettingsarray(_:completionhandler:).md) method with an array of settings objects representative of the types of capture you will be performing (such as settings for a bracketed capture, RAW capture, or capture with still image stabilization).

By default, the photo output prepares sufficient resources to capture photos with default settings (as defined by the [`AVCapturePhotoSettings`](avcapturephotosettings.md) default initializer).

## See Also

- [func setPreparedPhotoSettingsArray([AVCapturePhotoSettings], completionHandler: ((Bool, (any Error)?) -> Void)?)](avcapturephotooutput/setpreparedphotosettingsarray(_:completionhandler:).md)
  Tells the photo capture output to prepare resources for future capture requests with the specified settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/preparedphotosettingsarray)*