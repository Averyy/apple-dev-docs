# targetHDRHeadroom

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

Target HDR headroom for image rendering.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var targetHDRHeadroom: CGFloat { get set }
```

```objc
@property (nonatomic, assign) CGFloat targetHDRHeadroom;
```

#### Discussion

Specifies the target headroom value for HDR image rendering. Headroom represents the ratio between the maximum display brightness and standard dynamic range (SDR) white level.

- A headroom value of `0.0` means “headroom unknown”. Images with unknown content headroom will be excluded from tone mapping, following CGImage documentation behavior.
- Headroom values less than `0.0` or between `0.0` and `1.0` (exclusive) are undefined and will be clamped to `0.0` (unknown) rather than throwing an error.
- Headroom is dependent on the current display capabilities. It is the responsibility of the caller to re-request the image if the display’s headroom characteristics change. Swift view default behavior applies to views that use images outside of the current display headroom supported range.

Defaults to `1.0` (SDR, fully tone mapped).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptions/targethdrheadroom)*