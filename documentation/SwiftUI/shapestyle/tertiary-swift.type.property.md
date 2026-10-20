# tertiary

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A shape style that maps to the third level of the current content style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@export(implementation)
static var tertiary: HierarchicalShapeStyle { get }
```

Available when `Self` is `HierarchicalShapeStyle`.

#### Discussion

This hierarchical style maps to the third level of the current foreground style, or to the third level of the default foreground style if you haven’t set a foreground style in the view’s environment. You typically set a foreground style by supplying a non-hierarchical style to the [`foregroundStyle(_:)`](../view/foregroundstyle%28_%29.md) modifier.

For information about how to use shape styles, see [`ShapeStyle`](../shapestyle.md).

## See Also

### Hierarchical styles
- [var secondary: some ShapeStyle](./secondary-swift.property.md)
  Returns the second level of this shape style.
- [var tertiary: some ShapeStyle](./tertiary-swift.property.md)
  Returns the third level of this shape style.
- [var quaternary: some ShapeStyle](./quaternary-swift.property.md)
  Returns the fourth level of this shape style.
- [var quinary: some ShapeStyle](./quinary-swift.property.md)
  Returns the fifth level of this shape style.
- [static var primary: HierarchicalShapeStyle](./primary.md)
  A shape style that maps to the first level of the current content style.
- [static var secondary: HierarchicalShapeStyle](./secondary-swift.type.property.md)
  A shape style that maps to the second level of the current content style.
- [static var quaternary: HierarchicalShapeStyle](./quaternary-swift.type.property.md)
  A shape style that maps to the fourth level of the current content style.
- [static var quinary: HierarchicalShapeStyle](./quinary-swift.type.property.md)
  A shape style that maps to the fifth level of the current content style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/tertiary-swift.type.property)*