# IMKMouseHandling

**Framework**: InputMethodKit  
**Kind**: protocol

The `IMKMouseHandling` protocol defines methods that your input method can implement to handle mouse events.

**Availability**:
- macOS 10.5+

## Declaration

```swift
protocol IMKMouseHandling
```

## Topics

### Handling Mouse Events
- [func mouseDown(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, continueTracking: UnsafeMutablePointer<ObjCBool>!, client: Any!) -> Bool](imkmousehandling/mousedown(oncharacterindex:coordinate:withmodifier:continuetracking:client:).md)
  Handles mouse-down event send to an input method.
- [func mouseUp(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, client: Any!) -> Bool](imkmousehandling/mouseup(oncharacterindex:coordinate:withmodifier:client:).md)
  Handles a mouse-up event sent to an input method.
- [func mouseMoved(onCharacterIndex: Int, coordinate: NSPoint, withModifier: Int, client: Any!) -> Bool](imkmousehandling/mousemoved(oncharacterindex:coordinate:withmodifier:client:).md)
  Handles a mouse-moved event sent to an input method.

## Relationships

### Conforming Types
- [IMKInputController](imkinputcontroller.md)

## See Also

- [IMKServerInput](imkserverinput.md)
  `IMKServerInput` is an informal protocol that defines methods for receiving text events. This is intentionally not a formal protocol because there are three ways to receive events. An input method chooses one of the following approaches and implements the appropriate methods:
- [protocol IMKStateSetting](imkstatesetting.md)
  The `IMKStateSetting` protocol defines methods for setting or accessing values that indicate the state of an input method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkmousehandling)*