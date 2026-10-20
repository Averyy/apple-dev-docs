# CVDisplayLink

**Framework**: Core Video  
**Role**: API Collection

A high-priority thread that notifies your app when a given display will need each frame.

#### Overview

A Core Video display link provides a separate high-priority thread to notify your application when a given display will need each frame. You can use a display link to easily synchronize with the refresh rate of a display. The display link API uses the Core Foundation class system internally to provide reference counting behavior and other useful properties.

## Topics

### Creating Display Links
- [func CVDisplayLinkCreateWithCGDisplay(CGDirectDisplayID, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](./cvdisplaylinkcreatewithcgdisplay%28_,_%29.md)
  Creates a display link for a single display.
- [func CVDisplayLinkCreateWithCGDisplays(UnsafeMutablePointer<CGDirectDisplayID>, CFIndex, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](./cvdisplaylinkcreatewithcgdisplays%28_,_,_%29.md)
  Creates a display link for an array of displays.
- [func CVDisplayLinkCreateWithActiveCGDisplays(UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](./cvdisplaylinkcreatewithactivecgdisplays%28_%29.md)
  Creates a display link capable of being used with all active displays.
- [func CVDisplayLinkCreateWithOpenGLDisplayMask(CGOpenGLDisplayMask, UnsafeMutablePointer<CVDisplayLink?>) -> CVReturn](./cvdisplaylinkcreatewithopengldisplaymask%28_,_%29.md)
  Creates a display link from an OpenGL display mask.
### Configuring Display Links
- [func CVDisplayLinkSetCurrentCGDisplay(CVDisplayLink, CGDirectDisplayID) -> CVReturn](./cvdisplaylinksetcurrentcgdisplay%28_,_%29.md)
  Sets the current display of a display link.
- [func CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext(CVDisplayLink, CGLContextObj, CGLPixelFormatObj) -> CVReturn](./cvdisplaylinksetcurrentcgdisplayfromopenglcontext%28_,_,_%29.md)
  Selects the display link most optimal for the current renderer of an OpenGL context.
- [func CVDisplayLinkSetOutputCallback(CVDisplayLink, CVDisplayLinkOutputCallback?, UnsafeMutableRawPointer?) -> CVReturn](./cvdisplaylinksetoutputcallback%28_,_,_%29.md)
  Sets the renderer output callback function.
- [func CVDisplayLinkSetOutputHandler(CVDisplayLink, CVDisplayLinkOutputHandler) -> CVReturn](./cvdisplaylinksetoutputhandler%28_,_%29.md)
- [typealias CVDisplayLinkOutputHandler](./cvdisplaylinkoutputhandler.md)
### Inspecting Display Links
- [func CVDisplayLinkGetCurrentCGDisplay(CVDisplayLink) -> CGDirectDisplayID](./cvdisplaylinkgetcurrentcgdisplay%28_%29.md)
  Gets the current display associated with a display link.
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
### Managing Display Links
- [func CVDisplayLinkStart(CVDisplayLink) -> CVReturn](./cvdisplaylinkstart%28_%29.md)
  Activates a display link.
- [func CVDisplayLinkStop(CVDisplayLink) -> CVReturn](./cvdisplaylinkstop%28_%29.md)
  Stops a display link.
### Data Types
- [class CVDisplayLink](./cvdisplaylink.md)
  A reference to a display link object.
- [typealias CVOptionFlags](./cvoptionflags.md)
  The flags to be used for the display link output callback function.
### Callbacks
- [typealias CVDisplayLinkOutputCallback](./cvdisplaylinkoutputcallback.md)
  A type for a display link callback function that the system invokes when it’s time for the app to output a video frame.
- [typealias CVDisplayLinkOutputHandler](./cvdisplaylinkoutputhandler.md)

## See Also

### Time Management
- [CVTime](./cvtime-q1e.md)
  A structure used for storing Core Video time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylink-k0k)*