# CVDisplayLinkGetCurrentCGDisplay(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Gets the current display associated with a display link.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

> **Deprecated**: use NSView.displayLink(target:selector:), NSWindow.displayLink(target:selector:), or NSScreen.displayLink(target:selector:) 

## Declaration

```swift
func CVDisplayLinkGetCurrentCGDisplay(_ displayLink: CVDisplayLink) -> CGDirectDisplayID
```

```c
extern CGDirectDisplayID CVDisplayLinkGetCurrentCGDisplay(CVDisplayLinkRef displayLink);
```

#### Return Value

An identifier representing the current display. For more information on the display identifier type, see [`CGDirectDisplayID`](../CoreGraphics/cgdirectdisplayid.md).

## Parameters

- `displayLink`: The display link whose current display you want to obtain.

## See Also

### Inspecting Display Links
- [func CVDisplayLinkGetCurrentTime(CVDisplayLink, UnsafeMutablePointer<CVTimeStamp>) -> CVReturn](./cvdisplaylinkgetcurrenttime%28_,_%29.md)
  Retrieves the current (“now”) time of a given display link.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkgetcurrentcgdisplay(_:))*