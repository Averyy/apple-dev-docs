# map(_:)

**Framework**: TabularData  
**Kind**: method

Creates a new column by applying a transformation to every element.

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
func map<T>(_ transform: (ColumnSlice<WrappedElement>.Element) throws -> T?) rethrows -> Column<T>
```

## Parameters

- `transform`: The transformation closure.

## See Also

- [func filled(with: Self.WrappedElement) -> FilledColumn<Self>](columnslice/filled(with:).md)
  Generates a filled column by replacing missing elements with a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/map(_:))*