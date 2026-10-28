# NSFocusRingType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the style of the focus ring.

**Availability**:
- macOS

## Declaration

```swift
enum NSFocusRingType
```

```c
enum NSFocusRingType : NSUInteger;
```

## Overview

The focus ring type is used by [`NSView`](./nsview.md) and [`NSCell`](./nscell.md) to configure whether and how a control draws its focus ring.

## Topics

### Constants
- [NSFocusRingType.default](./nsfocusringtype/default.md)
  The default focus ring type for a view or cell.
- [NSFocusRingType.none](./nsfocusringtype/none.md)
  No focus ring.
- [NSFocusRingType.exterior](./nsfocusringtype/exterior.md)
  The standard Aqua focus ring.
### Initializers
- [init?(rawValue: UInt)](./nsfocusringtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Drawing Focus Rings
- [func set()](./nsfocusringplacement/set%28%29.md)
  Specifies how the system draws the focus ring.
- [enum NSFocusRingPlacement](./nsfocusringplacement.md)
  Constants that indicate how the system draws the focus ring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfocusringtype)*