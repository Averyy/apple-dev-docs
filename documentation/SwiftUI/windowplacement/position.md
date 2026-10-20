# WindowPlacement.Position

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A semantic or positional value for the location of a window.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Position
```

## Topics

### Type Properties
- [static var utilityPanel: WindowPlacement.Position](./position/utilitypanel.md)
  Utility panel window position.
### Type Methods
- [static func above(WindowProxy) -> WindowPlacement.Position](./position/above%28_%29.md)
  Window position relative to the top edge of another window.
- [static func below(WindowProxy) -> WindowPlacement.Position](./position/below%28_%29.md)
  Window position relative to the bottom edge of another window.
- [static func leading(WindowProxy) -> WindowPlacement.Position](./position/leading%28_%29.md)
  Window position relative to the leading edge of another window.
- [static func replacing(WindowProxy) -> WindowPlacement.Position](./position/replacing%28_%29.md)
  Positions the window in the same spot as an existing window, hiding the old window in the process.
- [static func trailing(WindowProxy) -> WindowPlacement.Position](./position/trailing%28_%29.md)
  Window position relative to the trailing edge of another window.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowplacement/position)*