# GridItem.Size.flexible(minimum:maximum:)

**Framework**: SwiftUI  
**Kind**: case  
**Role**: Case

A single flexible item.

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
case flexible(minimum: CGFloat = 10, maximum: CGFloat = .infinity)
```

## Discussion

The size of this item is the size of the grid with spacing and inflexible items removed, divided by the number of flexible items, clamped to the provided bounds.

## See Also

### Getting the sizes
- [case adaptive(minimum: CGFloat, maximum: CGFloat)](./adaptive%28minimum,maximum%29.md)
  Multiple items in the space of a single flexible item.
- [GridItem.Size.fixed(_:)](./fixed%28_%29.md)
  A single item with the specified fixed size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/griditem/size-swift.enum/flexible(minimum:maximum:))*