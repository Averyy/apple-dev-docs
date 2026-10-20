# CGEventSourceStateID.hidSystemState

**Framework**: Core Graphics  
**Kind**: case  
**Role**: Case

Specifies that an event source should use the event state table that reflects the combined state of all hardware event sources posting from the HID system.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
case hidSystemState
```

```c
kCGEventSourceStateHIDSystemState
```

## See Also

### Constants
- [CGEventSourceStateID.privateState](./privatestate.md)
  Specifies that an event source should use a private event state table.
- [CGEventSourceStateID.combinedSessionState](./combinedsessionstate.md)
  Specifies that an event source should use the event state table that reflects the combined state of all event sources posting to the current user login session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgeventsourcestateid/hidsystemstate)*