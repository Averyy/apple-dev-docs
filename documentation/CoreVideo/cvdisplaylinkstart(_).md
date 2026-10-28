# CVDisplayLinkStart(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Activates a display link.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

> **Deprecated**: use NSView.displayLink(target:selector:), NSWindow.displayLink(target:selector:), or NSScreen.displayLink(target:selector:) 

## Declaration

```swift
func CVDisplayLinkStart(_ displayLink: CVDisplayLink) -> CVReturn
```

```c
extern CVReturn CVDisplayLinkStart(CVDisplayLinkRef displayLink);
```

## Return Value

A Core Video result code. See[Core Video Constants](./core-video-constants.md) for possible values.

## Discussion

Calling this function starts the display link thread, which then periodically calls back to your application to request that you display frames. If the specified display link is already running, `CVDisplayLinkStart` returns an error.

## Parameters

- `displayLink`: The display link to be activated.

## See Also

### Managing Display Links
- [func CVDisplayLinkStop(CVDisplayLink) -> CVReturn](./cvdisplaylinkstop%28_%29.md)
  Stops a display link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkstart(_:))*