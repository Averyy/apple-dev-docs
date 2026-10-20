# CAClockNew(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func CAClockNew(_ inReservedFlags: UInt32, _ outCAClock: UnsafeMutablePointer<CAClockRef?>) -> OSStatus
```

```c
extern OSStatus CAClockNew(UInt32 inReservedFlags, CAClockRef*outCAClock);
```

## See Also

### Creating a Clock
- [func CAClockDispose(CAClockRef) -> OSStatus](./caclockdispose%28_%29.md)
- [typealias CAClockRef](./caclockref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/caclocknew(_:_:))*