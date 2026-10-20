# supportedDepthDataFormats

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The list of data formats compatible with this video format.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var supportedDepthDataFormats: [AVCaptureDevice.Format] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVCaptureDeviceFormat *> * supportedDepthDataFormats;
```

#### Discussion

Depth data capture requires a compatible pairing of video format and depth data format. After you set a capture device’s [`activeFormat`](../activeformat.md) property to this format, you can set the device’s [`activeDepthDataFormat`](../activedepthdataformat.md) property to one of the formats in this array.

Supported depth data formats always match the aspect ratio of their corresponding video format.

## See Also

### Determining depth capture support
- [var supportedVideoZoomFactorsForDepthDataDelivery: [CGFloat]](./supportedvideozoomfactorsfordepthdatadelivery.md)
  The zoom factors that a format supports for depth data delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/supporteddepthdataformats)*