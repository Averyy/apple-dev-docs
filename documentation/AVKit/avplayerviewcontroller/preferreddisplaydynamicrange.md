# preferredDisplayDynamicRange

**Framework**: AVKit  
**Kind**: property

Describes how High Dynamic Range (HDR) video content renders.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@MainActor
var preferredDisplayDynamicRange: AVDisplayDynamicRange { get set }
```

#### Discussion

Defaults to `AVDisplayDynamicRangeAutomatic`.

> **Note**: This property will only have effect if the video content supports HDR.

## See Also

- [enum AVDisplayDynamicRange](avdisplaydynamicrange.md)
  Describes how High Dynamic Range (HDR) video content renders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/preferreddisplaydynamicrange)*