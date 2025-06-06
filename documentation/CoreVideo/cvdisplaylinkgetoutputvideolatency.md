# CVDisplayLinkGetOutputVideoLatency(_:)

**Framework**: Core Video  
**Kind**: func

Retrieves the nominal latency of a display link.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkGetOutputVideoLatency(_ displayLink: CVDisplayLink) -> CVTime
```

#### Return Value

A `CVTime` structure that holds the latency value. This value may be indefinite.

#### Discussion

This call allows you to retrieve the device’s built-in output latency. For example, an NTSC device with one frame of latency might report back 1001/30000 or 2002/60000.

## Parameters

- `displayLink`: The display link whose latency value you want to obtain.

## See Also

- [func CVDisplayLinkGetCurrentCGDisplay(CVDisplayLink) -> CGDirectDisplayID](cvdisplaylinkgetcurrentcgdisplay(_:).md)
  Gets the current display associated with a display link.
- [func CVDisplayLinkGetCurrentTime(CVDisplayLink, UnsafeMutablePointer<CVTimeStamp>) -> CVReturn](cvdisplaylinkgetcurrenttime(_:_:).md)
  Retrieves the current (“now”) time of a given display link.
- [func CVDisplayLinkTranslateTime(CVDisplayLink, UnsafePointer<CVTimeStamp>, UnsafeMutablePointer<CVTimeStamp>) -> CVReturn](cvdisplaylinktranslatetime(_:_:_:).md)
  Translates the time in the display link’s time base from one representation to another.
- [func CVDisplayLinkGetActualOutputVideoRefreshPeriod(CVDisplayLink) -> Double](cvdisplaylinkgetactualoutputvideorefreshperiod(_:).md)
  Retrieves the actual output refresh period of a display as measured by the system time.
- [func CVDisplayLinkGetNominalOutputVideoRefreshPeriod(CVDisplayLink) -> CVTime](cvdisplaylinkgetnominaloutputvideorefreshperiod(_:).md)
  Retrieves the nominal refresh period of a display link.
- [func CVDisplayLinkIsRunning(CVDisplayLink) -> Bool](cvdisplaylinkisrunning(_:).md)
  Indicates whether a given display link is running.
- [func CVDisplayLinkGetTypeID() -> CFTypeID](cvdisplaylinkgettypeid().md)
  Obtains the Core Foundation ID for the display link data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkgetoutputvideolatency(_:))*