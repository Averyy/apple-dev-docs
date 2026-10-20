# append(contentsOf:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

Appends a sequence of nonoptional values to the column.

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
mutating func append<S>(contentsOf sequence: S) where WrappedElement == S.Element, S : Sequence
```

## Parameters

- `sequence`: A sequence of nonoptional elements.

## See Also

### Adding Elements
- [func append(WrappedElement)](./append%28_%29-qycj.md)
  Appends a nonoptional value to the column.
- [func append(Column<WrappedElement>.Element)](./append%28_%29-4t2pt.md)
  Appends an optional value to the column.
- [func append<S>(contentsOf: S)](./append%28contentsof%29-42y1d.md)
  Appends a sequence of optional values to the column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/append(contentsof:)-qb4p)*