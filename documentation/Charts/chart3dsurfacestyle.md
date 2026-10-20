# Chart3DSurfaceStyle

**Framework**: Swift Charts  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol Chart3DSurfaceStyle : Hashable
```

## Topics

### Type Properties
- [static var heightBased: BasicChart3DSurfaceStyle](./chart3dsurfacestyle/heightbased.md)
  Height (Y) based style.
- [static var normalBased: BasicChart3DSurfaceStyle](./chart3dsurfacestyle/normalbased.md)
  Surface normal based style.
### Type Methods
- [static func heightBased(Gradient, yRange: ClosedRange<CGFloat>?) -> Self](./chart3dsurfacestyle/heightbased%28_,yrange%29.md)
  Height (Y) based style with gradient and Y range.
- [static func heightBased(yRange: ClosedRange<CGFloat>) -> Self](./chart3dsurfacestyle/heightbased%28yrange%29.md)
  Height (Y) based style with Y range.

## Relationships

### Inherits From
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
### Conforming Types
- [BasicChart3DSurfaceStyle](./basicchart3dsurfacestyle.md)

## See Also

### Configuring surfaces
- [struct BasicChart3DSurfaceStyle](./basicchart3dsurfacestyle.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chart3dsurfacestyle)*