# GridItem.Size

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

The size in the minor axis of one or more rows or columns in a grid layout.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
enum Size
```

#### Overview

Use a `Size` instance when you create a [`GridItem`](../griditem.md). The value tells a [`LazyHGrid`](../lazyhgrid.md) how to size its rows, or a [`LazyVGrid`](../lazyvgrid.md) how to size its columns.

## Topics

### Getting the sizes
- [case adaptive(minimum: CGFloat, maximum: CGFloat)](./size-swift.enum/adaptive%28minimum,maximum%29.md)
  Multiple items in the space of a single flexible item.
- [GridItem.Size.fixed(_:)](./size-swift.enum/fixed%28_%29.md)
  A single item with the specified fixed size.
- [case flexible(minimum: CGFloat, maximum: CGFloat)](./size-swift.enum/flexible%28minimum,maximum%29.md)
  A single flexible item.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting grid item properties
- [var alignment: Alignment?](./alignment.md)
  The alignment to use when placing each view.
- [var spacing: CGFloat?](./spacing.md)
  The spacing to the next item.
- [var size: GridItem.Size](./size-swift.property.md)
  The size of the item, which is the width of a column item or the height of a row item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/griditem/size-swift.enum)*