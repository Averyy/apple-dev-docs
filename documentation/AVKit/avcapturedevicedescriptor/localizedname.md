# localizedName

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

A name for the camera that’s suitable for display in your interface.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+

## Declaration

```swift
var localizedName: String { get }
```

```objc
@property (nonatomic, readonly) NSString * localizedName;
```

#### Discussion

This value matches the [`localizedName`](../../AVFoundation/avcapturedevice/localizedname.md) of the camera it describes.

## See Also

### Identifying the device
- [var uniqueID: String](./uniqueid.md)
  An identifier that uniquely identifies the device’s camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor/localizedname)*