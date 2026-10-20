# CVDisplayLinkTranslateTime(_:_:_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Translates the time in the display link’s time base from one representation to another.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

> **Deprecated**: use NSView.displayLink(target:selector:), NSWindow.displayLink(target:selector:), or NSScreen.displayLink(target:selector:) 

## Declaration

```swift
func CVDisplayLinkTranslateTime(_ displayLink: CVDisplayLink, _ inTime: UnsafePointer<CVTimeStamp>, _ outTime: UnsafeMutablePointer<CVTimeStamp>) -> CVReturn
```

```c
extern CVReturn CVDisplayLinkTranslateTime(CVDisplayLinkRef displayLink, const CVTimeStamp *inTime, CVTimeStamp *outTime);
```

#### Return Value

A Core Video result code. See [Core Video Constants](./core-video-constants.md) for possible values.

#### Discussion

Note that the display link has to be running for this call to succeed.

## Parameters

- `displayLink`: The display link whose time base should be used to do the translation.
- `inTime`: A pointer to a `CVTimeStamp` structure containing the source time to translate.
- `outTime`: A pointer to a `CVTimeStamp` structure into which the target time is written. Before calling, you must set the version field (currently `0`) to indicate which version of the structure you want. You should also set the `flags` field to specify which representations to translate to.

## See Also

### Inspecting Display Links
- [func CVDisplayLinkGetCurrentCGDisplay(CVDisplayLink) -> CGDirectDisplayID](./cvdisplaylinkgetcurrentcgdisplay%28_%29.md)
  Gets the current display associated with a display link.
- [func CVDisplayLinkGetCurrentTime(CVDisplayLink, UnsafeMutablePointer<CVTimeStamp>) -> CVReturn](./cvdisplaylinkgetcurrenttime%28_,_%29.md)
  Retrieves the current (“now”) time of a given display link.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinktranslatetime(_:_:_:))*