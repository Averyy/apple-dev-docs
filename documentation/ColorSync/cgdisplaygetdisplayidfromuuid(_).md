# CGDisplayGetDisplayIDFromUUID(_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func CGDisplayGetDisplayIDFromUUID(_ uuid: CFUUID!) -> UInt32
```

```c
extern uint32_t CGDisplayGetDisplayIDFromUUID(CFUUIDRef uuid);
```

## See Also

### Converting display identifiers
- [func CGDisplayCreateUUIDFromDisplayID(UInt32) -> Unmanaged<CFUUID>!](./cgdisplaycreateuuidfromdisplayid%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/cgdisplaygetdisplayidfromuuid(_:))*