# OptionalColumnProtocol Implementations

**Framework**: TabularData

## Topics

### Operators
- [static func * (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](column/*(_:_:)-3dm6q.md)
  Generates a column by multiplying a value by each element in an optional column type.
- [static func * (Self, Self) -> Column<Self.WrappedElement>](column/*(_:_:)-8n0od.md)
  Generates a column by multiplying each element in an optional column type by the corresponding elements of another.
- [static func * (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](column/*(_:_:)-8ndcj.md)
  Generates a column by multiplying each element in an optional column by a value.
- [static func + (Self, Self) -> Column<Self.WrappedElement>](column/+(_:_:)-3hy3o.md)
  Generates a column by adding each element in an optional column type to the corresponding elements of another.
- [static func + (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](column/+(_:_:)-7jy9x.md)
  Generates a column by adding a value to each element in an optional column.
- [static func + (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](column/+(_:_:)-8uo1v.md)
  Generates a column by adding each element in an optional column to a value.
- [static func - (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](column/-(_:_:)-326lu.md)
  Generates a column by subtracting each element in an optional column from a value.
- [static func - (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](column/-(_:_:)-5zgbu.md)
  Generates a column by subtracting a value from each element in an optional column type.
- [static func - (Self, Self) -> Column<Self.WrappedElement>](column/-(_:_:)-9ltja.md)
  Generates a column by subtracting each element in an optional column type from the corresponding elements of another.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](column/_(_:_:)-1rwra.md)
  Generates a floating-point column by dividing each element in an optional column by a value.
- [static func / (Self, Self) -> Column<Self.WrappedElement>](column/_(_:_:)-2bk2d.md)
  Generates an integer column by dividing each element in an optional column type by the corresponding elements of another.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](column/_(_:_:)-2p0ex.md)
  Generates a floating-point column by dividing a value by each element in an optional column type.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](column/_(_:_:)-60cwp.md)
  Generates an integer column by dividing each element in an optional column by a value.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](column/_(_:_:)-7or0v.md)
  Generates an integer column by dividing a value by each element in an optional column type.
- [static func / (Self, Self) -> Column<Self.WrappedElement>](column/_(_:_:)-8jh9v.md)
  Generates a floating-point column by dividing each element in an optional column type by the corresponding elements of another.
### Instance Methods
- [func description(options: FormattingOptions) -> String](column/description(options:).md)
  Generates a string description of the optional column type.
- [func filled(with: Self.WrappedElement) -> FilledColumn<Self>](column/filled(with:).md)
  Generates a filled column by replacing missing elements with a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/optionalcolumnprotocol-implementations)*