# displayUpdateGranularity

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of seconds between the screen’s supported update rates, for screens that support fixed update rates.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var displayUpdateGranularity: TimeInterval { get }
```

```objc
@property (readonly) NSTimeInterval displayUpdateGranularity;
```

## Discussion

All screen refresh rates fall between the values in the [`minimumRefreshInterval`](./minimumrefreshinterval.md) and [`maximumRefreshInterval`](./maximumrefreshinterval.md) properties. For screens that support fixed update rates, this property contains the amount of time between two successive rates. For example, if a screen supports update rates between 30Hz and 120Hz with an update granularity of 5ms, the screen supports additional refresh rates of approximately 35Hz, 43Hz, 55Hz, and 75Hz.

If the value of this property is `0`, the screen supports any update rate between the minimum and maximum refresh intervals.

## See Also

### Getting Variable Refresh Rate Details
- [var maximumFramesPerSecond: Int](./maximumframespersecond.md)
  The maximum number of frames per second that the screen supports.
- [var minimumRefreshInterval: TimeInterval](./minimumrefreshinterval.md)
  The shortest refresh interval that the screen supports.
- [var maximumRefreshInterval: TimeInterval](./maximumrefreshinterval.md)
  The largest refresh interval that the screen supports.
- [var lastDisplayUpdateTimestamp: TimeInterval](./lastdisplayupdatetimestamp.md)
  The time of the last framebuffer update, expressed as the number of seconds since system startup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/displayupdategranularity)*