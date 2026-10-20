# isResting

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The indicator for a resting touch.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var isResting: Bool { get }
```

```objc
@property (readonly, getter=isResting) BOOL resting;
```

#### Discussion

Resting touches occur when a user simply rests their thumb on the trackpad device.

## See Also

### Using Touch Properties
- [var identity: any NSCopying & NSObjectProtocol](./identity.md)
  The changes to a particular touch during its lifetime.
- [var phase: NSTouch.Phase](./phase-swift.property.md)
  The current phase of the touch.
- [NSTouch.Phase](./phase-swift.struct.md)
  The possible phases of a touch.
- [var normalizedPosition: NSPoint](./normalizedposition.md)
  The normalized position of the touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch/isresting)*