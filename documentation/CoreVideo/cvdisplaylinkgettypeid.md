# CVDisplayLinkGetTypeID()

**Framework**: Core Video  
**Kind**: func

Obtains the Core Foundation ID for the display link data type.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkGetTypeID() -> CFTypeID
```

#### Return Value

The Core Foundation ID for this type.

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
- [func CVDisplayLinkGetOutputVideoLatency(CVDisplayLink) -> CVTime](cvdisplaylinkgetoutputvideolatency(_:).md)
  Retrieves the nominal latency of a display link.
- [func CVDisplayLinkIsRunning(CVDisplayLink) -> Bool](cvdisplaylinkisrunning(_:).md)
  Indicates whether a given display link is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkgettypeid())*