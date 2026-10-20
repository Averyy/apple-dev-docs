# normalizedPosition

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The normalized position of the touch.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var normalizedPosition: NSPoint { get }
```

```objc
@property (readonly) NSPoint normalizedPosition;
```

#### Discussion

The normalized position is a scaled value between (0.0) and (1.0,1.0), where (0.0,0.0) is the lower-left position on the touch device.

## See Also

### Using Touch Properties
- [var identity: any NSCopying & NSObjectProtocol](./identity.md)
  The changes to a particular touch during its lifetime.
- [var phase: NSTouch.Phase](./phase-swift.property.md)
  The current phase of the touch.
- [NSTouch.Phase](./phase-swift.struct.md)
  The possible phases of a touch.
- [var isResting: Bool](./isresting.md)
  The indicator for a resting touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch/normalizedposition)*