# OptionalColumnProtocol Implementations

**Framework**: TabularData

## Topics

### Operators
- [static func * (Self, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/*(_:_:)-2tbo9.md)
  Generates a column by multiplying each element in an optional column type by the corresponding elements of another.
- [static func * (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/*(_:_:)-3dsxf.md)
  Generates a column by multiplying a value by each element in an optional column type.
- [static func * (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](discontiguouscolumnslice/*(_:_:)-8faxs.md)
  Generates a column by multiplying each element in an optional column by a value.
- [static func + (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](discontiguouscolumnslice/+(_:_:)-2ba70.md)
  Generates a column by adding a value to each element in an optional column.
- [static func + (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/+(_:_:)-77c23.md)
  Generates a column by adding each element in an optional column to a value.
- [static func + (Self, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/+(_:_:)-7swqp.md)
  Generates a column by adding each element in an optional column type to the corresponding elements of another.
- [static func - (Self, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/-(_:_:)-2hf72.md)
  Generates a column by subtracting each element in an optional column type from the corresponding elements of another.
- [static func - (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/-(_:_:)-5nwcb.md)
  Generates a column by subtracting each element in an optional column from a value.
- [static func - (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](discontiguouscolumnslice/-(_:_:)-hqv5.md)
  Generates a column by subtracting a value from each element in an optional column type.
- [static func / (Self, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/_(_:_:)-1e5kt.md)
  Generates an integer column by dividing each element in an optional column type by the corresponding elements of another.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/_(_:_:)-29za6.md)
  Generates an integer column by dividing a value by each element in an optional column type.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](discontiguouscolumnslice/_(_:_:)-3bul1.md)
  Generates a floating-point column by dividing each element in an optional column by a value.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](discontiguouscolumnslice/_(_:_:)-51brc.md)
  Generates an integer column by dividing each element in an optional column by a value.
- [static func / (Self, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/_(_:_:)-6dcws.md)
  Generates a floating-point column by dividing each element in an optional column type by the corresponding elements of another.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](discontiguouscolumnslice/_(_:_:)-80g7i.md)
  Generates a floating-point column by dividing a value by each element in an optional column type.
### Instance Methods
- [func description(options: FormattingOptions) -> String](discontiguouscolumnslice/description(options:).md)
  Generates a string description of the optional column type.
- [func filled(with: Self.WrappedElement) -> FilledColumn<Self>](discontiguouscolumnslice/filled(with:).md)
  Generates a filled column by replacing missing elements with a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/discontiguouscolumnslice/optionalcolumnprotocol-implementations)*