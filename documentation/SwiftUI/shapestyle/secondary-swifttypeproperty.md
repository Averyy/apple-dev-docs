# secondary

**Framework**: SwiftUI  
**Kind**: property

A shape style that maps to the second level of the current content style.

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
static var secondary: HierarchicalShapeStyle { get }
```

#### Discussion

This hierarchical style maps to the second level of the current foreground style, or to the second level of the default foreground style if you haven’t set a foreground style in the view’s environment. You typically set a foreground style by supplying a non-hierarchical style to the [`foregroundStyle(_:)`](view/foregroundstyle(_:).md) modifier.

For information about how to use shape styles, see [`ShapeStyle`](shapestyle.md).

## See Also

- [var secondary: some ShapeStyle](shapestyle/secondary-swift.property.md)
  Returns the second level of this shape style.
- [var tertiary: some ShapeStyle](shapestyle/tertiary-swift.property.md)
  Returns the third level of this shape style.
- [var quaternary: some ShapeStyle](shapestyle/quaternary-swift.property.md)
  Returns the fourth level of this shape style.
- [var quinary: some ShapeStyle](shapestyle/quinary-swift.property.md)
  Returns the fifth level of this shape style.
- [static var primary: HierarchicalShapeStyle](shapestyle/primary.md)
  A shape style that maps to the first level of the current content style.
- [static var tertiary: HierarchicalShapeStyle](shapestyle/tertiary-swift.type.property.md)
  A shape style that maps to the third level of the current content style.
- [static var quaternary: HierarchicalShapeStyle](shapestyle/quaternary-swift.type.property.md)
  A shape style that maps to the fourth level of the current content style.
- [static var quinary: HierarchicalShapeStyle](shapestyle/quinary-swift.type.property.md)
  A shape style that maps to the fifth level of the current content style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/secondary-swift.type.property)*