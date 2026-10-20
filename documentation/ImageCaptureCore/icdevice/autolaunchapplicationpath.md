# autolaunchApplicationPath

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

The file system path of an application to launch automatically when this device is added.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var autolaunchApplicationPath: String? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * autolaunchApplicationPath;
```

## See Also

### Configuring a Device’s Characteristics
- [var userData: NSMutableDictionary?](./userdata.md)
  A bookkeeping object for client convenience.
- [var isRemote: Bool](./isremote.md)
  A Boolean value indicating whether the device is published by the Image Capture device-sharing facility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/autolaunchapplicationpath)*