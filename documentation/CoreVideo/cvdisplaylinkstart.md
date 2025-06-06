# CVDisplayLinkStart(_:)

**Framework**: Core Video  
**Kind**: func

Activates a display link.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func CVDisplayLinkStart(_ displayLink: CVDisplayLink) -> CVReturn
```

#### Return Value

A Core Video result code. See[`Core Video Constants`](core-video-constants.md) for possible values.

#### Discussion

Calling this function starts the display link thread, which then periodically calls back to your application to request that you display frames. If the specified display link is already running, `CVDisplayLinkStart` returns an error.

## Parameters

- `displayLink`: The display link to be activated.

## See Also

- [func CVDisplayLinkStop(CVDisplayLink) -> CVReturn](cvdisplaylinkstop(_:).md)
  Stops a display link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvdisplaylinkstart(_:))*