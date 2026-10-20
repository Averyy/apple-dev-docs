# CGDisplayCreateUUIDFromDisplayID(_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func CGDisplayCreateUUIDFromDisplayID(_ displayID: UInt32) -> Unmanaged<CFUUID>!
```

```c
extern CFUUIDRefCGDisplayCreateUUIDFromDisplayID(uint32_t displayID);
```

## See Also

### Converting display identifiers
- [func CGDisplayGetDisplayIDFromUUID(CFUUID!) -> UInt32](./cgdisplaygetdisplayidfromuuid%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/cgdisplaycreateuuidfromdisplayid(_:))*