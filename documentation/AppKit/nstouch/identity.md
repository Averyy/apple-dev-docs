# identity

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The changes to a particular touch during its lifetime.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var identity: any NSCopying & NSObjectProtocol { get }
```

```objc
@property (strong, readonly) id<NSCopying,NSObject> identity;
```

#### Discussion

While touch identities may be re-used, they are unique during the life of the touch, even when multiple devices are present.

Identity objects implement the [`NSCopying`](../../Foundation/nscopying.md) protocol so that they may be used as keys in an [`NSDictionary`](../../Foundation/nsdictionary.md). Use isEqual: to compare two touch identities.

## See Also

### Using Touch Properties
- [var phase: NSTouch.Phase](./phase-swift.property.md)
  The current phase of the touch.
- [NSTouch.Phase](./phase-swift.struct.md)
  The possible phases of a touch.
- [var normalizedPosition: NSPoint](./normalizedposition.md)
  The normalized position of the touch.
- [var isResting: Bool](./isresting.md)
  The indicator for a resting touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouch/identity)*