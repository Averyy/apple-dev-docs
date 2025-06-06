# init(_:contents:)

**Framework**: TabularData  
**Kind**: init

Creates a column with an identifier and a sequence of nonoptional values.

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
init<S>(_ id: ColumnID<S.Element>, contents: S) where WrappedElement == S.Element, S : Sequence
```

## Parameters

- `id`: A column identifier.
- `contents`: A sequence of elements.

## See Also

- [init(name: String, capacity: Int)](column/init(name:capacity:).md)
  Creates a column with a name and a capacity.
- [init(ColumnID<WrappedElement>, capacity: Int)](column/init(_:capacity:).md)
  Creates a column with a column identifier and a capacity.
- [init<S>(name: String, contents: S)](column/init(name:contents:)-6okx3.md)
  Creates a column with a name and a sequence of nonoptional values.
- [init<S>(name: String, contents: S)](column/init(name:contents:)-8nxtj.md)
  Creates a column with a name and a sequence of optional values.
- [init<S>(ColumnID<S.Element>, contents: S)](column/init(_:contents:)-7z5ji.md)
  Creates a column with a column identifier and a sequence of optional values.
- [init(ColumnSlice<WrappedElement>)](column/init(_:).md)
  Creates a column from a column slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/init(_:contents:)-1871a)*