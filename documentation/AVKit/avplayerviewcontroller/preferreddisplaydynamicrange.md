# preferredDisplayDynamicRange

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Describes how High Dynamic Range (HDR) video content renders.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var preferredDisplayDynamicRange: AVDisplayDynamicRange { get set }
```

```objc
@property (nonatomic, assign, readwrite) AVDisplayDynamicRange preferredDisplayDynamicRange;
```

## Discussion

Defaults to `AVDisplayDynamicRangeAutomatic`.

> **Note**: This property will only have effect if the video content supports HDR.

## See Also

### High dynamic range
- [enum AVDisplayDynamicRange](../avdisplaydynamicrange.md)
  Describes how High Dynamic Range (HDR) video content renders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/preferreddisplaydynamicrange)*