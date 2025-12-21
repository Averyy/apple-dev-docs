# mouseUp(onCharacterIndex:coordinate:withModifier:client:)

**Framework**: InputMethodKit  
**Kind**: method  
**Required**: Yes

Handles a mouse-up event sent to an input method.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func mouseUp(onCharacterIndex index: Int, coordinate point: NSPoint, withModifier flags: Int, client sender: Any!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if handled; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Implement this method if your input method handles mouse-up events.

## Parameters

- `index`: The index within the sender’s text storage where the mouse-up event occurred.
- `point`: The point at which the mouse-up event occurred.
- `flags`: The modifier keys.
- `sender`: The client object.

## See Also

- [func mouseDown(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, continueTracking: UnsafeMutablePointer<ObjCBool>!, client: Any!) -> Bool](imkmousehandling/mousedown(oncharacterindex:coordinate:withmodifier:continuetracking:client:).md)
  Handles mouse-down event send to an input method.
- [func mouseMoved(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, client: Any!) -> Bool](imkmousehandling/mousemoved(oncharacterindex:coordinate:withmodifier:client:).md)
  Handles a mouse-moved event sent to an input method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkmousehandling/mouseup(oncharacterindex:coordinate:withmodifier:client:))*