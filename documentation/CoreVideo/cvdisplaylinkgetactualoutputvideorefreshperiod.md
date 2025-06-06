# CVDisplayLinkGetActualOutputVideoRefreshPeriod(_:)

**Framework**: Core Video  
**Kind**: func

Retrieves the actual output refresh period of a display as measured by the system time.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkGetActualOutputVideoRefreshPeriod(_ displayLink: CVDisplayLink) -> Double
```

#### Return Value

A double-precision floating-point value representing the actual refresh period in seconds. This value may be zero if the device is not running or is otherwise unavailable.

#### Discussion

This call returns the actual output refresh period computed relative to the system time (as measured using the [`CVGetCurrentHostTime()`](cvgetcurrenthosttime().md) function).

## Parameters

- `displayLink`: The display link to get the refresh period from.

## See Also

- [func CVDisplayLinkGetCurrentCGDisplay(CVDisplayLink) -> CGDirectDisplayID](cvdisplaylinkgetcurrentcgdisplay(_:).md)
  Gets the current display associated with a display link.
- [func CVDisplayLinkGetCurrentTime(CVDisplayLink, UnsafeMutablePointer<CVTimeStamp>) -> CVReturn](cvdisplaylinkgetcurrenttime(_:_:).md)
  Retrieves the current (“now”) time of a given display link.
- [func CVDisplayLinkTranslateTime(CVDisplayLink, UnsafePointer<CVTimeStamp>, UnsafeMutablePointer<CVTimeStamp>) -> CVReturn](cvdisplaylinktranslatetime(_:_:_:).md)
  Translates the time in the display link’s time base from one representation to another.
- [func CVDisplayLinkGetNominalOutputVideoRefreshPeriod(CVDisplayLink) -> CVTime](cvdisplaylinkgetnominaloutputvideorefreshperiod(_:).md)
  Retrieves the nominal refresh period of a display link.
- [func CVDisplayLinkGetOutputVideoLatency(CVDisplayLink) -> CVTime](cvdisplaylinkgetoutputvideolatency(_:).md)
  Retrieves the nominal latency of a display link.
- [func CVDisplayLinkIsRunning(CVDisplayLink) -> Bool](cvdisplaylinkisrunning(_:).md)
  Indicates whether a given display link is running.
- [func CVDisplayLinkGetTypeID() -> CFTypeID](cvdisplaylinkgettypeid().md)
  Obtains the Core Foundation ID for the display link data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkgetactualoutputvideorefreshperiod(_:))*