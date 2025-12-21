# preferredDisplayDynamicRange

**Framework**: AVKit  
**Kind**: property

Describes how High Dynamic Range (HDR) video content renders.

**Availability**:
- macOS 26.0+

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

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerview/preferreddisplaydynamicrange)*