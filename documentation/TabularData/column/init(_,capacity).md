# init(_:capacity:)

**Framework**: TabularData  
**Kind**: init  
**Role**: Initializer

Creates a column with a column identifier and a capacity.

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
init(_ id: ColumnID<WrappedElement>, capacity: Int)
```

## Parameters

- `id`: A column identifier.
- `capacity`: An integer that represents the number of elements the column can initially store.

## See Also

### Creating a Column
- [init(name: String, capacity: Int)](./init%28name,capacity%29.md)
  Creates a column with a name and a capacity.
- [init<S>(name: String, contents: S)](./init%28name,contents%29-6okx3.md)
  Creates a column with a name and a sequence of nonoptional values.
- [init<S>(name: String, contents: S)](./init%28name,contents%29-8nxtj.md)
  Creates a column with a name and a sequence of optional values.
- [init<S>(ColumnID<S.Element>, contents: S)](./init%28_,contents%29-1871a.md)
  Creates a column with an identifier and a sequence of nonoptional values.
- [init<S>(ColumnID<S.Element>, contents: S)](./init%28_,contents%29-7z5ji.md)
  Creates a column with a column identifier and a sequence of optional values.
- [init(ColumnSlice<WrappedElement>)](./init%28_%29.md)
  Creates a column from a column slice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/init(_:capacity:))*