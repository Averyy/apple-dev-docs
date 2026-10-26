# UIPointerRegion

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A rectangular region that interacts with pointer movements.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPointerRegion
```

```objc
@interface UIPointerRegion : NSObject
```

## Topics

### Creating a region
- [convenience init(rect: CGRect, identifier: AnyHashable?)](./uipointerregion/init%28rect,identifier%29.md)
  Creates a pointer region with the specified rectangle and optional identifier.
- [+ regionWithRect:identifier:](./uipointerregion/regionwithrect_identifier_.md)
  Creates a pointer region with the specified rectangle and optional identifier.
### Configuring a region
- [var rect: CGRect](./uipointerregion/rect.md)
  The rectangle bounds of the region.
- [var identifier: AnyHashable?](./uipointerregion/identifier-1tw1m.md)
  An optional identifier for the region.
- [var latchingAxes: UIAxis](./uipointerregion/latchingaxes.md)
  Axes along which the region latches after a primary click.
- [identifier](./uipointerregion/identifier-9i5wc.md)
  An optional identifier for the region.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Pointer region
- [class UIPointerRegionRequest](./uipointerregionrequest.md)
  An object to describe the pointer’s location in the interaction’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerregion)*