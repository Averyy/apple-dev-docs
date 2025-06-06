# CVDisplayLinkStop(_:)

**Framework**: Core Video  
**Kind**: func

Stops a display link.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkStop(_ displayLink: CVDisplayLink) -> CVReturn
```

#### Return Value

A Core Video result code. See [`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

If the specified display link is already stopped, `CVDisplayLinkStop` returns an error.

In macOS 10.4 and later, the display link thread is automatically stopped if the user employs Fast User Switching. The display link is restarted when switching back to the original user.

## Parameters

- `displayLink`: The display link to be stopped.

## See Also

- [func CVDisplayLinkStart(CVDisplayLink) -> CVReturn](cvdisplaylinkstart(_:).md)
  Activates a display link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkstop(_:))*