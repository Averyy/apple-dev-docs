# setEventForwardingMask(_:)

**Framework**: Quartz  
**Kind**: method

Sets the mask used to filter which types of events are forwarded from the view to the composition during rendering.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setEventForwardingMask(_ mask: Int)
```

## Parameters

- `mask`: An event filtering mask. The mask can be a combination of any of the mask constants listed below, or the constant `NSAnyEventMask`. | Event | Description |
| --- | --- |
| `NSLeftMouseDownMask` | The user pressed the left button. |
| `NSLeftMouseDraggedMask` | The user moved the mouse with the left button down. |
| `NSLeftMouseUpMask` | The user released the left button. |
| `NSRightMouseDownMask` | The user pressed the right button. |
| `NSRightMouseDraggedMask` | The user moved the mouse with the right button down. |
| `NSRightMouseUpMask` | The user released the right button. |
| `NSOtherMouseDownMask` | The user pressed the middle button, or some button other than the left or right button. |
| `NSOtherMouseDraggedMask` | The user moved the mouse with the middle button down, or some button other than the left or right button. |
| `NSOtherMouseUpMask` | The user released the middle button, or some button other than the left or right button. |
| `NSMouseMovedMask` | The user moved the mouse without holding down a mouse button. |
| `NSScrollWheelMask` | The user moved the mouse scroll wheel. |
| `NSKeyDownMask` | The user generated a character or characters by pressing a key. |
| `NSKeyUpMask` | The user released a key. |
| `NSFlagsChangedMask` | The user pressed or released a modifier key, or toggled the Caps Lock key. |

## See Also

- [func eventForwardingMask() -> Int](qcview/eventforwardingmask.md)
  Retrieves the mask used to filter which types of events are forwarded from the view to the composition during rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/seteventforwardingmask(_:))*