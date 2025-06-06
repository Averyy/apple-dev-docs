# identity

**Framework**: AppKit  
**Kind**: property

The changes to a particular touch during its lifetime.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var identity: any NSCopying & NSObjectProtocol { get }
```

#### Discussion

While touch identities may be re-used, they are unique during the life of the touch, even when multiple devices are present.

Identity objects implement the [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying) protocol so that they may be used as keys in an [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary). Use isEqual: to compare two touch identities.

## See Also

- [var phase: NSTouch.Phase](nstouch/phase-swift.property.md)
  The current phase of the touch.
- [NSTouch.Phase](nstouch/phase-swift.struct.md)
  The possible phases of a touch.
- [var normalizedPosition: NSPoint](nstouch/normalizedposition.md)
  The normalized position of the touch.
- [var isResting: Bool](nstouch/isresting.md)
  The indicator for a resting touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch/identity)*