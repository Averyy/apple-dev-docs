# !=(_:_:)

**Framework**: TabularData  
**Kind**: op

Returns a Boolean array that indicates whether the corresponding element of a column type isn’t equal to a value.

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
static func != (lhs: Self, rhs: Self.Element) -> [Bool]
```

#### Return Value

A Boolean array.

#### Discussion

- lhs: A column type.
- rhs: A value of the same type as the column.

## See Also

- [static func == (Self, Self.Element) -> [Bool]](columnprotocol/==(_:_:)-5jc0x.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is equal to a value.
- [static func == (Self.Element, Self) -> [Bool]](columnprotocol/==(_:_:)-4hx04.md)
  Returns a Boolean array that indicates whether the value is equal to the corresponding element of a column type.
- [static func != (Self.Element, Self) -> [Bool]](columnprotocol/!=(_:_:)-72ddh.md)
  Returns a Boolean array that indicates whether the value isn’t equal to the corresponding element of a column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnprotocol/!=(_:_:)-557vb)*