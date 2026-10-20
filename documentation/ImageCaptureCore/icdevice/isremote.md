# isRemote

**Framework**: ImageCaptureCore  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the device is published by the Image Capture device-sharing facility.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var isRemote: Bool { get }
```

```objc
@property (readonly, getter=isRemote) BOOL remote;
```

## See Also

### Configuring a Device’s Characteristics
- [var userData: NSMutableDictionary?](./userdata.md)
  A bookkeeping object for client convenience.
- [var autolaunchApplicationPath: String?](./autolaunchapplicationpath.md)
  The file system path of an application to launch automatically when this device is added.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevice/isremote)*