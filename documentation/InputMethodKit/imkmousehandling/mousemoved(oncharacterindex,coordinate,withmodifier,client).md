# mouseMoved(onCharacterIndex:coordinate:withModifier:client:)

**Framework**: InputMethodKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles a mouse-moved event sent to an input method.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func mouseMoved(onCharacterIndex index: Int, coordinate point: NSPoint, withModifier flags: Int, client sender: Any!) -> Bool
```

```objc
- (BOOL) mouseMovedOnCharacterIndex:(NSUInteger) index coordinate:(NSPoint) point withModifier:(NSUInteger) flags client:(id) sender;
```

## Return Value

[`true`](../../Swift/true.md) if handled; otherwise [`false`](../../Swift/false.md).

## Discussion

Implement this method if your input method handles mouse-moved events.

## Parameters

- `index`: The index within the sender’s text storage where the mouse-moved event occurred.
- `point`: The point at which the mouse-moved event occurred.
- `flags`: The modifier keys.
- `sender`: The client object.

## See Also

### Handling Mouse Events
- [func mouseDown(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, continueTracking: UnsafeMutablePointer<ObjCBool>!, client: Any!) -> Bool](./mousedown%28oncharacterindex,coordinate,withmodifier,continuetracking,client%29.md)
  Handles mouse-down event send to an input method.
- [func mouseUp(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, client: Any!) -> Bool](./mouseup%28oncharacterindex,coordinate,withmodifier,client%29.md)
  Handles a mouse-up event sent to an input method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkmousehandling/mousemoved(oncharacterindex:coordinate:withmodifier:client:))*