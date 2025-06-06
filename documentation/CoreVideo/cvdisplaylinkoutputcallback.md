# CVDisplayLinkOutputCallback

**Framework**: Core Video  
**Kind**: typealias

A type for a display link callback function that the system invokes when it’s time for the app to output a video frame.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
typealias CVDisplayLinkOutputCallback = (CVDisplayLink, UnsafePointer<CVTimeStamp>, UnsafePointer<CVTimeStamp>, CVOptionFlags, UnsafeMutablePointer<CVOptionFlags>, UnsafeMutableRawPointer?) -> CVReturn
```

#### Discussion

Your app must register a callback function for the system to invoke with the data necessary to process and output a frame of video. Your callback must retrieve the frame with the timestamp that the `inOutputTime` parameter specifies, manipulate it if you require (for example, apply color correction or map onto a surface), and output it to the display.

## Parameters

- `displayLink`: A display link that requests a frame.
- `inNow`: A pointer to the current time.
- `inOutputTime`: A pointer to the display time for a frame.
- `flagsIn`: Currently unused. Pass 0.
- `flagsOut`: Currently unused. Pass 0.
- `displayLinkContext`: A pointer to app-defined data.

## See Also

- [typealias CVDisplayLinkOutputHandler](cvdisplaylinkoutputhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkoutputcallback)*