# mouseDown(onCharacterIndex:coordinate:withModifier:continueTracking:client:)

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles mouse-down event send to an input method.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func mouseDown(onCharacterIndex index: Int, coordinate point: NSPoint, withModifier flags: Int, continueTracking keepTracking: UnsafeMutablePointer<ObjCBool>!, client sender: Any!) -> Bool
```

```objc
- (BOOL) mouseDownOnCharacterIndex:(NSUInteger) index coordinate:(NSPoint) point withModifier:(NSUInteger) flags continueTracking:(BOOL *) keepTracking client:(id) sender;
```

#### Return Value

[`true`](../../Swift/true.md) if handled; otherwise [`false`](../../Swift/false.md).

#### Discussion

Implement this method if your input method handles mouse-down events.

## Parameters

- `index`: The index within the sender’s text storage where the mouse-down event occurred.
- `point`: The point at which the mouse-down event occurred.
- `flags`: The modifier keys.
- `keepTracking`: Set this parameter to [`true`](../../Swift/true.md) if you want to receive subsequent mouse-moved and mouse -up events.
- `sender`: The client object.

## See Also

### Handling Mouse Events
- [func mouseUp(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, client: Any!) -> Bool](./mouseup%28oncharacterindex,coordinate,withmodifier,client%29.md)
  Handles a mouse-up event sent to an input method.
- [func mouseMoved(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, client: Any!) -> Bool](./mousemoved%28oncharacterindex,coordinate,withmodifier,client%29.md)
  Handles a mouse-moved event sent to an input method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkmousehandling/mousedown(oncharacterindex:coordinate:withmodifier:continuetracking:client:))*