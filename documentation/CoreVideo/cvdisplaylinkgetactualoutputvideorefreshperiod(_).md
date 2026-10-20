# CVDisplayLinkGetActualOutputVideoRefreshPeriod(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Retrieves the actual output refresh period of a display as measured by the system time.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

> **Deprecated**: use NSView.displayLink(target:selector:), NSWindow.displayLink(target:selector:), or NSScreen.displayLink(target:selector:) 

## Declaration

```swift
func CVDisplayLinkGetActualOutputVideoRefreshPeriod(_ displayLink: CVDisplayLink) -> Double
```

```c
extern double CVDisplayLinkGetActualOutputVideoRefreshPeriod(CVDisplayLinkRef displayLink);
```

#### Return Value

A double-precision floating-point value representing the actual refresh period in seconds. This value may be zero if the device is not running or is otherwise unavailable.

#### Discussion

This call returns the actual output refresh period computed relative to the system time (as measured using the [`CVGetCurrentHostTime()`](./cvgetcurrenthosttime%28%29.md) function).

## Parameters

- `displayLink`: The display link to get the refresh period from.

## See Also

### Inspecting Display Links
- [func CVDisplayLinkGetCurrentCGDisplay(CVDisplayLink) -> CGDirectDisplayID](./cvdisplaylinkgetcurrentcgdisplay%28_%29.md)
  Gets the current display associated with a display link.
- [func CVDisplayLinkGetCurrentTime(CVDisplayLink, UnsafeMutablePointer<CVTimeStamp>) -> CVReturn](./cvdisplaylinkgetcurrenttime%28_,_%29.md)
  Retrieves the current (“now”) time of a given display link.
- [func CVDisplayLinkTranslateTime(CVDisplayLink, UnsafePointer<CVTimeStamp>, UnsafeMutablePointer<CVTimeStamp>) -> CVReturn](./cvdisplaylinktranslatetime%28_,_,_%29.md)
  Translates the time in the display link’s time base from one representation to another.
- [func CVDisplayLinkGetNominalOutputVideoRefreshPeriod(CVDisplayLink) -> CVTime](./cvdisplaylinkgetnominaloutputvideorefreshperiod%28_%29.md)
  Retrieves the nominal refresh period of a display link.
- [func CVDisplayLinkGetOutputVideoLatency(CVDisplayLink) -> CVTime](./cvdisplaylinkgetoutputvideolatency%28_%29.md)
  Retrieves the nominal latency of a display link.
- [func CVDisplayLinkIsRunning(CVDisplayLink) -> Bool](./cvdisplaylinkisrunning%28_%29.md)
  Indicates whether a given display link is running.
- [func CVDisplayLinkGetTypeID() -> CFTypeID](./cvdisplaylinkgettypeid%28%29.md)
  Obtains the Core Foundation ID for the display link data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkgetactualoutputvideorefreshperiod(_:))*