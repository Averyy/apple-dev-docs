# OptionalColumnProtocol Implementations

**Framework**: TabularData

## Topics

### Operators
- [static func * (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](columnslice/*(_:_:)-4sw7w.md)
  Generates a column by multiplying each element in an optional column by a value.
- [static func * (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](columnslice/*(_:_:)-86zas.md)
  Generates a column by multiplying a value by each element in an optional column type.
- [static func * (Self, Self) -> Column<Self.WrappedElement>](columnslice/*(_:_:)-hl25.md)
  Generates a column by multiplying each element in an optional column type by the corresponding elements of another.
- [static func + (Self, Self) -> Column<Self.WrappedElement>](columnslice/+(_:_:)-3mep5.md)
  Generates a column by adding each element in an optional column type to the corresponding elements of another.
- [static func + (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](columnslice/+(_:_:)-3xsx4.md)
  Generates a column by adding a value to each element in an optional column.
- [static func + (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](columnslice/+(_:_:)-ooqt.md)
  Generates a column by adding each element in an optional column to a value.
- [static func - (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](columnslice/-(_:_:)-5mbpd.md)
  Generates a column by subtracting each element in an optional column from a value.
- [static func - (Self, Self) -> Column<Self.WrappedElement>](columnslice/-(_:_:)-6dkqb.md)
  Generates a column by subtracting each element in an optional column type from the corresponding elements of another.
- [static func - (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](columnslice/-(_:_:)-nkha.md)
  Generates a column by subtracting a value from each element in an optional column type.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](columnslice/_(_:_:)-1oxxv.md)
  Generates a floating-point column by dividing each element in an optional column by a value.
- [static func / (Self, Self) -> Column<Self.WrappedElement>](columnslice/_(_:_:)-3so2z.md)
  Generates an integer column by dividing each element in an optional column type by the corresponding elements of another.
- [static func / (Self, Self) -> Column<Self.WrappedElement>](columnslice/_(_:_:)-4125n.md)
  Generates a floating-point column by dividing each element in an optional column type by the corresponding elements of another.
- [static func / (Self, Self.WrappedElement) -> Column<Self.WrappedElement>](columnslice/_(_:_:)-8n9gx.md)
  Generates an integer column by dividing each element in an optional column by a value.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](columnslice/_(_:_:)-992oe.md)
  Generates an integer column by dividing a value by each element in an optional column type.
- [static func / (Self.WrappedElement, Self) -> Column<Self.WrappedElement>](columnslice/_(_:_:)-esxm.md)
  Generates a floating-point column by dividing a value by each element in an optional column type.
### Instance Methods
- [func description(options: FormattingOptions) -> String](columnslice/description(options:).md)
  Generates a string description of the optional column type.
- [func filled(with: Self.WrappedElement) -> FilledColumn<Self>](columnslice/filled(with:).md)
  Generates a filled column by replacing missing elements with a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnslice/optionalcolumnprotocol-implementations)*