# lastDisplayUpdateTimestamp

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The time of the last framebuffer update, expressed as the number of seconds since system startup.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var lastDisplayUpdateTimestamp: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval lastDisplayUpdateTimestamp;
```

## Discussion

Use this property to determine how much time elapsed since the last frame update.

## See Also

### Getting Variable Refresh Rate Details
- [var maximumFramesPerSecond: Int](./maximumframespersecond.md)
  The maximum number of frames per second that the screen supports.
- [var minimumRefreshInterval: TimeInterval](./minimumrefreshinterval.md)
  The shortest refresh interval that the screen supports.
- [var maximumRefreshInterval: TimeInterval](./maximumrefreshinterval.md)
  The largest refresh interval that the screen supports.
- [var displayUpdateGranularity: TimeInterval](./displayupdategranularity.md)
  The number of seconds between the screen’s supported update rates, for screens that support fixed update rates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/lastdisplayupdatetimestamp)*