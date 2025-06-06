# modifierFlags

**Framework**: AppKit  
**Kind**: property

An integer bit field that indicates the pressed modifier keys.

**Availability**:
- macOS ?+

## Declaration

```swift
var modifierFlags: NSEvent.ModifierFlags { get }
```

#### Discussion

You can examine individual flag settings using the C bitwise AND operator with the predefined key masks described in `Getting Unicode Values`. The lower 16 bits of the modifier flags are reserved for device-dependent bits.

## See Also

- [NSEvent.ModifierFlags](nsevent/modifierflags-swift.struct.md)
  Flags that represent key states in an event object.
- [class var modifierFlags: NSEvent.ModifierFlags](nsevent/modifierflags-swift.type.property.md)
  The currently pressed modifier keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/modifierflags-swift.property)*