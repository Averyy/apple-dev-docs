# shouldBeTreatedAsInkEvent(_:)

**Framework**: AppKit  
**Kind**: method

Indicates whether a pen-down event should be treated as an ink event.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func shouldBeTreatedAsInkEvent(_ event: NSEvent) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the specified event should be treated as an ink event, [`false`](https://developer.apple.com/documentation/Swift/false) if it should be treated as a mouse event.

#### Discussion

This method provides the ability to distinguish when a pen-down event should start inking versus when a pen-down event should be treated as a mouse-down event. This allows for a write-anywhere model for pen-based input.

The default implementation in [`NSApplication`](nsapplication.md) sends the method to the [`NSWindow`](nswindow.md) object under the pen. If the window is inactive, this method returns [`true`](https://developer.apple.com/documentation/Swift/true), unless the pen-down is in the window drag region. If the window is active, this method is sent to the [`NSView`](nsview.md) object under the pen.

The default implementation in [`NSView`](nsview.md) returns [`true`](https://developer.apple.com/documentation/Swift/true), and [`NSControl`](nscontrol.md) overrides and returns [`false`](https://developer.apple.com/documentation/Swift/false). This allows write-anywhere over most `NSView` objects, but allows the pen to be used to track in controls and to move windows.

A custom view should override this method to get the correct behavior for a pen-down in the view.

## Parameters

- `event`: An event object representing the event to be tested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/shouldbetreatedasinkevent(_:))*