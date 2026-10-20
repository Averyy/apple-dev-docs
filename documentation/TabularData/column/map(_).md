# map(_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

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
func map<T>(_ transform: (Column<WrappedElement>.Element) throws -> T?) rethrows -> Column<T>
```

## Parameters

- `transform`: A transformation closure.

## See Also

### Creating Transformed Columns
- [func mapNonNil<T>((WrappedElement) throws -> T?) rethrows -> Column<T>](./mapnonnil%28_%29.md)
  Creates a new column by applying the transformation to every element that isn’t missing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/map(_:))*