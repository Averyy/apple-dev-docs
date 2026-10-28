# shouldBeTreatedAsInkEvent(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Indicates whether a pen-down event should be treated as an ink event.

**Availability**:
- macOS

## Declaration

```swift
func shouldBeTreatedAsInkEvent(_ event: NSEvent) -> Bool
```

```objc
- (BOOL) shouldBeTreatedAsInkEvent:(NSEvent *) event;
```

## Return Value

Returns [`true`](../../Swift/true.md) if the specified event should be treated as an ink event, [`false`](../../Swift/false.md) if it should be treated as a mouse event.

## Discussion

This method provides the ability to distinguish when a pen-down event should start inking versus when a pen-down event should be treated as a mouse-down event. This allows for a write-anywhere model for pen-based input.

The default implementation in [`NSApplication`](../nsapplication.md) sends the method to the [`NSWindow`](../nswindow.md) object under the pen. If the window is inactive, this method returns [`true`](../../Swift/true.md), unless the pen-down is in the window drag region. If the window is active, this method is sent to the [`NSView`](../nsview.md) object under the pen.

The default implementation in [`NSView`](../nsview.md) returns [`true`](../../Swift/true.md), and [`NSControl`](../nscontrol.md) overrides and returns [`false`](../../Swift/false.md). This allows write-anywhere over most `NSView` objects, but allows the pen to be used to track in controls and to move windows.

A custom view should override this method to get the correct behavior for a pen-down in the view.

## Parameters

- `event`: An event object representing the event to be tested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/shouldbetreatedasinkevent(_:))*