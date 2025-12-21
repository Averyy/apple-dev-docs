# mouseDown(onCharacterIndex:coordinate:withModifier:continueTracking:client:)

**Framework**: InputMethodKit  
**Kind**: method  
**Required**: Yes

Handles mouse-down event send to an input method.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func mouseDown(onCharacterIndex index: Int, coordinate point: NSPoint, withModifier flags: Int, continueTracking keepTracking: UnsafeMutablePointer<ObjCBool>!, client sender: Any!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if handled; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Implement this method if your input method handles mouse-down events.

## Parameters

- `index`: The index within the sender’s text storage where the mouse-down event occurred.
- `point`: The point at which the mouse-down event occurred.
- `flags`: The modifier keys.
- `keepTracking`: Set this parameter to   if you want to receive subsequent mouse-moved and mouse -up events.
- `sender`: The client object.

## See Also

- [func mouseUp(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, client: Any!) -> Bool](imkmousehandling/mouseup(oncharacterindex:coordinate:withmodifier:client:).md)
  Handles a mouse-up event sent to an input method.
- [func mouseMoved(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, client: Any!) -> Bool](imkmousehandling/mousemoved(oncharacterindex:coordinate:withmodifier:client:).md)
  Handles a mouse-moved event sent to an input method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkmousehandling/mousedown(oncharacterindex:coordinate:withmodifier:continuetracking:client:))*