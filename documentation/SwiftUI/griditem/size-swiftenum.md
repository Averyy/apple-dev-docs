# GridItem.Size

**Framework**: SwiftUI  
**Kind**: enum

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

Use a `Size` instance when you create a [`GridItem`](griditem.md). The value tells a [`LazyHGrid`](lazyhgrid.md) how to size its rows, or a [`LazyVGrid`](lazyvgrid.md) how to size its columns.

## Topics

### Getting the sizes
- [case adaptive(minimum: CGFloat, maximum: CGFloat)](griditem/size-swift.enum/adaptive(minimum:maximum:).md)
  Multiple items in the space of a single flexible item.
- [GridItem.Size.fixed(_:)](griditem/size-swift.enum/fixed(_:).md)
  A single item with the specified fixed size.
- [case flexible(minimum: CGFloat, maximum: CGFloat)](griditem/size-swift.enum/flexible(minimum:maximum:).md)
  A single flexible item.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var alignment: Alignment?](griditem/alignment.md)
  The alignment to use when placing each view.
- [var spacing: CGFloat?](griditem/spacing.md)
  The spacing to the next item.
- [var size: GridItem.Size](griditem/size-swift.property.md)
  The size of the item, which is the width of a column item or the height of a row item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/griditem/size-swift.enum)*