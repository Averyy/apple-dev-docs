# CVDisplayLinkTranslateTime(_:_:_:)

**Framework**: Core Video  
**Kind**: func

Translates the time in the display link’s time base from one representation to another.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkTranslateTime(_ displayLink: CVDisplayLink, _ inTime: UnsafePointer<CVTimeStamp>, _ outTime: UnsafeMutablePointer<CVTimeStamp>) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

Note that the display link has to be running for this call to succeed.

## Parameters

- `displayLink`: The display link whose time base should be used to do the translation.
- `inTime`: A pointer to a   structure containing the source time to translate.
- `outTime`: A pointer to a   structure into which the target time is written. Before calling, you must set the version field (currently  ) to indicate which version of the structure you want. You should also set the   field to specify which representations to translate to.

## See Also

- [func CVDisplayLinkGetCurrentCGDisplay(CVDisplayLink) -> CGDirectDisplayID](cvdisplaylinkgetcurrentcgdisplay(_:).md)
  Gets the current display associated with a display link.
- [func CVDisplayLinkGetCurrentTime(CVDisplayLink, UnsafeMutablePointer<CVTimeStamp>) -> CVReturn](cvdisplaylinkgetcurrenttime(_:_:).md)
  Retrieves the current (“now”) time of a given display link.
- [func CVDisplayLinkGetActualOutputVideoRefreshPeriod(CVDisplayLink) -> Double](cvdisplaylinkgetactualoutputvideorefreshperiod(_:).md)
  Retrieves the actual output refresh period of a display as measured by the system time.
- [func CVDisplayLinkGetNominalOutputVideoRefreshPeriod(CVDisplayLink) -> CVTime](cvdisplaylinkgetnominaloutputvideorefreshperiod(_:).md)
  Retrieves the nominal refresh period of a display link.
- [func CVDisplayLinkGetOutputVideoLatency(CVDisplayLink) -> CVTime](cvdisplaylinkgetoutputvideolatency(_:).md)
  Retrieves the nominal latency of a display link.
- [func CVDisplayLinkIsRunning(CVDisplayLink) -> Bool](cvdisplaylinkisrunning(_:).md)
  Indicates whether a given display link is running.
- [func CVDisplayLinkGetTypeID() -> CFTypeID](cvdisplaylinkgettypeid().md)
  Obtains the Core Foundation ID for the display link data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinktranslatetime(_:_:_:))*