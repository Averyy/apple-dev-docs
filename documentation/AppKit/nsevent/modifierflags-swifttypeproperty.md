# modifierFlags

**Framework**: AppKit  
**Kind**: property

The currently pressed modifier keys.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class var modifierFlags: NSEvent.ModifierFlags { get }
```

#### Return Value

A mask of the current modifiers using the values in `Modifier Flags`.

#### Discussion

This returns the state of devices combined with synthesized events at the moment, independent of which events have been delivered via the event stream.

## See Also

- [var modifierFlags: NSEvent.ModifierFlags](nsevent/modifierflags-swift.property.md)
  An integer bit field that indicates the pressed modifier keys.
- [NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct.md)
  Flags that represent key states in an event object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/modifierflags-swift.type.property)*