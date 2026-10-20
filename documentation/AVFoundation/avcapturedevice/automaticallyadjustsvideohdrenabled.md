# automaticallyAdjustsVideoHDREnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the device automatically manages the state of high dynamic range (HDR) video streaming.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var automaticallyAdjustsVideoHDREnabled: Bool { get set }
```

```objc
@property (nonatomic) BOOL automaticallyAdjustsVideoHDREnabled;
```

#### Discussion

By default, this value is `true`, and a capture device automatically enables [`isVideoHDREnabled`](./isvideohdrenabled.md) if it’s a good fit for the active format.

This property is key-value observable.

## See Also

### Configuring HDR settings
- [var isVideoHDREnabled: Bool](./isvideohdrenabled.md)
  A Boolean value that indicates whether the device streams high dynamic range video buffers, also known as extended dynamic range (EDR).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/automaticallyadjustsvideohdrenabled)*