# CVDisplayLinkStop(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Stops a display link.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.4+ - Deprecated in 15.0

> **Deprecated**: use NSView.displayLink(target:selector:), NSWindow.displayLink(target:selector:), or NSScreen.displayLink(target:selector:) 

## Declaration

```swift
func CVDisplayLinkStop(_ displayLink: CVDisplayLink) -> CVReturn
```

```c
extern CVReturn CVDisplayLinkStop(CVDisplayLinkRef displayLink);
```

## Return Value

A Core Video result code. See [Core Video Constants](./core-video-constants.md) for possible values.

## Discussion

If the specified display link is already stopped, `CVDisplayLinkStop` returns an error.

In macOS 10.4 and later, the display link thread is automatically stopped if the user employs Fast User Switching. The display link is restarted when switching back to the original user.

## Parameters

- `displayLink`: The display link to be stopped.

## See Also

### Managing Display Links
- [func CVDisplayLinkStart(CVDisplayLink) -> CVReturn](./cvdisplaylinkstart%28_%29.md)
  Activates a display link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkstop(_:))*