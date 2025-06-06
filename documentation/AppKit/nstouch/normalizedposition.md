# normalizedPosition

**Framework**: AppKit  
**Kind**: property

The normalized position of the touch.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var normalizedPosition: NSPoint { get }
```

#### Discussion

The normalized position is a scaled value between (0.0) and (1.0,1.0), where (0.0,0.0) is the lower-left position on the touch device.

## See Also

- [var identity: any NSCopying & NSObjectProtocol](nstouch/identity.md)
  The changes to a particular touch during its lifetime.
- [var phase: NSTouch.Phase](nstouch/phase-swift.property.md)
  The current phase of the touch.
- [NSTouch.Phase](nstouch/phase-swift.struct.md)
  The possible phases of a touch.
- [var isResting: Bool](nstouch/isresting.md)
  The indicator for a resting touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch/normalizedposition)*