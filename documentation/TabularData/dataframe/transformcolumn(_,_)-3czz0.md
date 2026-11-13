# transformColumn(_:_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Applies a transform closure that modifies the elements of a column you select by name.

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
mutating func transformColumn<From, To>(_ name: String, _ transform: (From?) throws -> To?) rethrows
```

## Parameters

- `name`: The name of a column in the data frame.
- `transform`: A closure that transforms each element in the column.

## See Also

### Transforming a column
- [func transformColumn<From, To>(ColumnID<From>, (From) throws -> To?) rethrows](./transformcolumn%28_,_%29-2avtt.md)
  Applies a transform closure that modifies the nonempty elements of a column you select by column identifier.
- [func transformColumn<From, To>(ColumnID<From>, (From?) throws -> To?) rethrows](./transformcolumn%28_,_%29-5s9en.md)
  Applies a transform closure that modifies the elements of a column you select by column identifier.
- [func transformColumn<From, To>(String, (From) throws -> To?) rethrows](./transformcolumn%28_,_%29-6cxpn.md)
  Applies a transform closure that modifies the nonempty elements of a column you select by name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/transformcolumn(_:_:)-3czz0)*