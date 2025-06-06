# lastDisplayUpdateTimestamp

**Framework**: AppKit  
**Kind**: property

The time of the last framebuffer update, expressed as the number of seconds since system startup.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var lastDisplayUpdateTimestamp: TimeInterval { get }
```

#### Discussion

Use this property to determine how much time elapsed since the last frame update.

## See Also

- [var maximumFramesPerSecond: Int](nsscreen/maximumframespersecond.md)
  The maximum number of frames per second that the screen supports.
- [var minimumRefreshInterval: TimeInterval](nsscreen/minimumrefreshinterval.md)
  The shortest refresh interval that the screen supports.
- [var maximumRefreshInterval: TimeInterval](nsscreen/maximumrefreshinterval.md)
  The largest refresh interval that the screen supports.
- [var displayUpdateGranularity: TimeInterval](nsscreen/displayupdategranularity.md)
  The number of seconds between the screen’s supported update rates, for screens that support fixed update rates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/lastdisplayupdatetimestamp)*