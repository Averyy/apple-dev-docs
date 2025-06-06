# minimumRefreshInterval

**Framework**: AppKit  
**Kind**: property

The shortest refresh interval that the screen supports.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var minimumRefreshInterval: TimeInterval { get }
```

#### Discussion

This interval represents the minimum amount of time, in seconds, your app has to generate new frames. It corresponds to the highest refresh rate of the display.

## See Also

- [var maximumFramesPerSecond: Int](nsscreen/maximumframespersecond.md)
  The maximum number of frames per second that the screen supports.
- [var maximumRefreshInterval: TimeInterval](nsscreen/maximumrefreshinterval.md)
  The largest refresh interval that the screen supports.
- [var displayUpdateGranularity: TimeInterval](nsscreen/displayupdategranularity.md)
  The number of seconds between the screen’s supported update rates, for screens that support fixed update rates.
- [var lastDisplayUpdateTimestamp: TimeInterval](nsscreen/lastdisplayupdatetimestamp.md)
  The time of the last framebuffer update, expressed as the number of seconds since system startup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/minimumrefreshinterval)*