# UIPointerRegionRequest

**Framework**: UIKit  
**Kind**: class

An object to describe the pointer’s location in the interaction’s view.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPointerRegionRequest
```

#### Overview

The `UIPointerRegionRequest` is given to the `UIPointerInteractionDelegate` to allow for changes to the pointer interaction.

## Topics

### Inspecting the region request
- [var location: CGPoint](uipointerregionrequest/location.md)
  The location of the pointer in the interaction’s view’s coordinate space.
- [var modifiers: UIKeyModifierFlags](uipointerregionrequest/modifiers.md)
  Key modifier flags representing keyboard keys pressed by the user at the time of this request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIPointerRegion](uipointerregion.md)
  A rectangular region that interacts with pointer movements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerregionrequest)*