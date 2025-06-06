# filled(with:)

**Framework**: TabularData  
**Kind**: method

Generates a filled column by replacing missing elements with a value.

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
func filled(with value: Self.WrappedElement) -> FilledColumn<Self>
```

#### Return Value

A filled column.

## Parameters

- `value`: A value the method uses to replace the column’s missing elements.

## See Also

- [func map<T>((Column<WrappedElement>.Element) throws -> T?) rethrows -> Column<T>](column/map(_:).md)
  Creates a new column by applying a transformation to every element.
- [func mapNonNil<T>((WrappedElement) throws -> T?) rethrows -> Column<T>](column/mapnonnil(_:).md)
  Creates a new column by applying the transformation to every element that isn’t missing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/filled(with:))*