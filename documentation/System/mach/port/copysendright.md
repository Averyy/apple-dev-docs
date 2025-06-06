# copySendRight()

**Framework**: System  
**Kind**: method

Create another send right from a given send right.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
func copySendRight() throws -> Mach.Port<Mach.SendRight>
```

#### Discussion

This does not affect the makeSendCount of the receive right.

If the send right being copied has become a dead name, meaning the receiving side has been deallocated, then copySendRight() will throw a Mach.PortRightError.deadName error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/mach/port/copysendright())*