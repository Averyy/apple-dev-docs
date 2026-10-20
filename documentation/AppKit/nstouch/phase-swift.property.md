# phase

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current phase of the touch.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var phase: NSTouch.Phase { get }
```

```objc
@property (readonly) NSTouchPhase phase;
```

#### Discussion

See [`NSTouch.Phase`](./phase-swift.struct.md) for possible values.

## See Also

### Using Touch Properties
- [var identity: any NSCopying & NSObjectProtocol](./identity.md)
  The changes to a particular touch during its lifetime.
- [NSTouch.Phase](./phase-swift.struct.md)
  The possible phases of a touch.
- [var normalizedPosition: NSPoint](./normalizedposition.md)
  The normalized position of the touch.
- [var isResting: Bool](./isresting.md)
  The indicator for a resting touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch/phase-swift.property)*