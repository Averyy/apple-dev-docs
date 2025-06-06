# acceptsFirstMouse(for:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value indicating whether a mouse-down event both activates the window and starts dragging the slider’s knob.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func acceptsFirstMouse(for event: NSEvent?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver accepts the first mouse-down event; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). Returns [`true`](https://developer.apple.com/documentation/swift/true) by default.

#### Discussion

If you want the slider to wait for its own mouse-down event, you must override this method.

## Parameters

- `event`: The mouse-down event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/acceptsfirstmouse(for:))*