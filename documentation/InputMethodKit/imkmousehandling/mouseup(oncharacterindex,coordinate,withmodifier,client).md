# mouseUp(onCharacterIndex:coordinate:withModifier:client:)

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles a mouse-up event sent to an input method.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func mouseUp(onCharacterIndex index: Int, coordinate point: NSPoint, withModifier flags: Int, client sender: Any!) -> Bool
```

```objc
- (BOOL) mouseUpOnCharacterIndex:(NSUInteger) index coordinate:(NSPoint) point withModifier:(NSUInteger) flags client:(id) sender;
```

#### Return Value

[`true`](../../Swift/true.md) if handled; otherwise [`false`](../../Swift/false.md).

#### Discussion

Implement this method if your input method handles mouse-up events.

## Parameters

- `index`: The index within the sender’s text storage where the mouse-up event occurred.
- `point`: The point at which the mouse-up event occurred.
- `flags`: The modifier keys.
- `sender`: The client object.

## See Also

### Handling Mouse Events
- [func mouseDown(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, continueTracking: UnsafeMutablePointer<ObjCBool>!, client: Any!) -> Bool](./mousedown%28oncharacterindex,coordinate,withmodifier,continuetracking,client%29.md)
  Handles mouse-down event send to an input method.
- [func mouseMoved(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, client: Any!) -> Bool](./mousemoved%28oncharacterindex,coordinate,withmodifier,client%29.md)
  Handles a mouse-moved event sent to an input method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkmousehandling/mouseup(oncharacterindex:coordinate:withmodifier:client:))*