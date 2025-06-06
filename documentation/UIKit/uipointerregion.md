# UIPointerRegion

**Framework**: UIKit  
**Kind**: class

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

## Topics

### Creating a region
- [convenience init(rect: CGRect, identifier: AnyHashable?)](uipointerregion/init(rect:identifier:).md)
  Creates a pointer region with the specified rectangle and optional identifier.
### Configuring a region
- [var rect: CGRect](uipointerregion/rect.md)
  The rectangle bounds of the region.
- [var identifier: AnyHashable?](uipointerregion/identifier-1tw1m.md)
  An optional identifier for the region.
- [var latchingAxes: UIAxis](uipointerregion/latchingaxes.md)
  Axes along which the region latches after a primary click.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIPointerRegionRequest](uipointerregionrequest.md)
  An object to describe the pointer’s location in the interaction’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerregion)*