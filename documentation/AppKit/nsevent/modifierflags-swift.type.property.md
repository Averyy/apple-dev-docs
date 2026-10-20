# modifierFlags

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The currently pressed modifier keys.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class var modifierFlags: NSEvent.ModifierFlags { get }
```

```objc
@property (class, readonly) NSEventModifierFlags modifierFlags;
```

#### Return Value

A mask of the current modifiers using the values in `Modifier Flags`.

#### Discussion

This returns the state of devices combined with synthesized events at the moment, independent of which events have been delivered via the event stream.

## See Also

### Getting modifier flags
- [var modifierFlags: NSEvent.ModifierFlags](./modifierflags-swift.property.md)
  An integer bit field that indicates the pressed modifier keys.
- [NSEvent.ModifierFlags](./modifierflags-swift.struct.md)
  Flags that represent key states in an event object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/modifierflags-swift.type.property)*