# /=(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Modifies a floating-point column by dividing each element by a value.

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
static func /= (lhs: inout Column<WrappedElement>, rhs: WrappedElement) where WrappedElement : FloatingPoint
```

## Parameters

- `lhs`: A column.
- `rhs`: A value of the same type as the column’s elements.

## See Also

### Modifying a Column with a Value
- [static func += (inout Column<WrappedElement>, WrappedElement)](./pluseq%28_,_%29-94q8g.md)
  Modifies a column by adding a value to each element.
- [static func -= (inout Column<WrappedElement>, WrappedElement)](./minuseq%28_,_%29-8arlr.md)
  Modifies a column by subtracting a value from each element.
- [static func *= (inout Column<WrappedElement>, WrappedElement)](./stareq%28_,_%29-4rraw.md)
  Modifies a column by multiplying each element by a value.
- [static func /= (inout Column<WrappedElement>, WrappedElement)](./opeq%28_,_%29-8jmir.md)
  Modifies an integer column by dividing each element by a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/_=(_:_:)-3hfr5)*