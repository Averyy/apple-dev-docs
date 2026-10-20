# mouseDownFlags

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The flags in effect at the mouse-down event that started the current tracking session.

**Availability**:
- macOS

## Declaration

```swift
var mouseDownFlags: Int { get }
```

```objc
@property (readonly) NSInteger mouseDownFlags;
```

#### Discussion

The [`NSMatrix`](../nsmatrix.md) [`mouseDown(with:)`](./mousedown%28with%29.md) method obtains these flags by sending a [`modifierFlags`](../nsevent/modifierflags-swift.property.md) message to the event passed into [`mouseDown(with:)`](./mousedown%28with%29.md). Use this property if you want to access these flags. This property is valid only during tracking; it isn’t useful if the target of the receiver initiates another tracking loop as part of its action method (as a cell that pops up a pop-up list does, for example).

## See Also

### Related Documentation
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](../nscontrol/sendaction%28on%29.md)
  Sets the conditions on which the receiver sends action messages to its target.
### Handling Event and Action Messages
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](./acceptsfirstmouse%28for%29.md)
  Returns a Boolean value indicating whether the receiver accepts the first mouse.
- [func mouseDown(with: NSEvent)](./mousedown%28with%29.md)
  Responds to a mouse-down event.
- [func performKeyEquivalent(with: NSEvent) -> Bool](./performkeyequivalent%28with%29.md)
  Looks for a cell that has the given key equivalent and, if found, makes that cell respond as if clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/mousedownflags)*