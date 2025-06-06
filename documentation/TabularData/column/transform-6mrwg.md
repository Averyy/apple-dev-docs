# transform(_:)

**Framework**: TabularData  
**Kind**: method

Applies a transformation to every element in the column.

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
mutating func transform(_ transform: (Column<WrappedElement>.Element) throws -> Column<WrappedElement>.Element) rethrows
```

## Parameters

- `transform`: A transformation closure.

## See Also

- [func transform((WrappedElement) throws -> WrappedElement) rethrows](column/transform(_:)-271dd.md)
  Applies a transformation to every element that isn’t missing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/transform(_:)-6mrwg)*