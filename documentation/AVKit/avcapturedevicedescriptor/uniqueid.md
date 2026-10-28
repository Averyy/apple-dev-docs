# uniqueID

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

An identifier that uniquely identifies the device’s camera.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+

## Declaration

```swift
var uniqueID: String { get }
```

```objc
@property (nonatomic, readonly) NSString * uniqueID;
```

## Discussion

This value matches the [`uniqueID`](../../AVFoundation/avcapturedevice/uniqueid.md) of the camera it describes. Pass it to [`init(uniqueID:)`](../../AVFoundation/avcapturedevice/init%28uniqueid%29.md) on a background actor to get the camera itself.

## See Also

### Identifying the device
- [var localizedName: String](./localizedname.md)
  A name for the camera that’s suitable for display in your interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcapturedevicedescriptor/uniqueid)*