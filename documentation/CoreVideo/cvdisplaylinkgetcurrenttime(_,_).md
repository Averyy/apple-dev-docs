# CVDisplayLinkGetCurrentTime(_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Retrieves the current (“now”) time of a given display link.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

> **Deprecated**: use NSView.displayLink(target:selector:), NSWindow.displayLink(target:selector:), or NSScreen.displayLink(target:selector:) 

## Declaration

```swift
func CVDisplayLinkGetCurrentTime(_ displayLink: CVDisplayLink, _ outTime: UnsafeMutablePointer<CVTimeStamp>) -> CVReturn
```

```c
extern CVReturn CVDisplayLinkGetCurrentTime(CVDisplayLinkRef displayLink, CVTimeStamp *outTime);
```

#### Return Value

A Core Video result code. See [Core Video Constants](./core-video-constants.md) for possible values.

#### Discussion

You use this call to obtain the timestamp of the frame that is currently being displayed.

## Parameters

- `displayLink`: The display link whose current time you want to obtain.
- `outTime`: A pointer to a `CVTimeStamp` structure. Note that you must set the version in the structure (currently 0) before calling to indicate which version of the timestamp structure you want.

## See Also

### Inspecting Display Links
- [func CVDisplayLinkGetCurrentCGDisplay(CVDisplayLink) -> CGDirectDisplayID](./cvdisplaylinkgetcurrentcgdisplay%28_%29.md)
  Gets the current display associated with a display link.
- [func CVDisplayLinkTranslateTime(CVDisplayLink, UnsafePointer<CVTimeStamp>, UnsafeMutablePointer<CVTimeStamp>) -> CVReturn](./cvdisplaylinktranslatetime%28_,_,_%29.md)
  Translates the time in the display link’s time base from one representation to another.
- [func CVDisplayLinkGetActualOutputVideoRefreshPeriod(CVDisplayLink) -> Double](./cvdisplaylinkgetactualoutputvideorefreshperiod%28_%29.md)
  Retrieves the actual output refresh period of a display as measured by the system time.
- [func CVDisplayLinkGetNominalOutputVideoRefreshPeriod(CVDisplayLink) -> CVTime](./cvdisplaylinkgetnominaloutputvideorefreshperiod%28_%29.md)
  Retrieves the nominal refresh period of a display link.
- [func CVDisplayLinkGetOutputVideoLatency(CVDisplayLink) -> CVTime](./cvdisplaylinkgetoutputvideolatency%28_%29.md)
  Retrieves the nominal latency of a display link.
- [func CVDisplayLinkIsRunning(CVDisplayLink) -> Bool](./cvdisplaylinkisrunning%28_%29.md)
  Indicates whether a given display link is running.
- [func CVDisplayLinkGetTypeID() -> CFTypeID](./cvdisplaylinkgettypeid%28%29.md)
  Obtains the Core Foundation ID for the display link data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkgetcurrenttime(_:_:))*