# acceptsFirstMouse(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether a mouse-down event both activates the window and starts dragging the slider’s knob.

**Availability**:
- macOS

## Declaration

```swift
func acceptsFirstMouse(for event: NSEvent?) -> Bool
```

```objc
- (BOOL) acceptsFirstMouse:(NSEvent *) event;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver accepts the first mouse-down event; otherwise, [`false`](../../Swift/false.md). Returns [`true`](../../Swift/true.md) by default.

#### Discussion

If you want the slider to wait for its own mouse-down event, you must override this method.

## Parameters

- `event`: The mouse-down event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/acceptsfirstmouse(for:))*