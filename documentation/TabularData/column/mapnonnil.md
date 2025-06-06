# mapNonNil(_:)

**Framework**: TabularData  
**Kind**: method

Creates a new column by applying the transformation to every element that isn’t missing.

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
func mapNonNil<T>(_ transform: (WrappedElement) throws -> T?) rethrows -> Column<T>
```

## Parameters

- `transform`: A transformation closure.

## See Also

- [func map<T>((Column<WrappedElement>.Element) throws -> T?) rethrows -> Column<T>](column/map(_:).md)
  Creates a new column by applying a transformation to every element.
- [func filled(with: Self.WrappedElement) -> FilledColumn<Self>](column/filled(with:).md)
  Generates a filled column by replacing missing elements with a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/mapnonnil(_:))*