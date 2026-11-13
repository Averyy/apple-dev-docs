# >=(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Returns a Boolean array that indicates whether the corresponding element of a column type is greater than or equal to a value.

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
static func >= (lhs: Self, rhs: Self.Element) -> [Bool]
```

Available when `Element` conforms to `Comparable`.

## Return Value

A Boolean array.

## Discussion

- lhs: A column type.
- rhs: A value of the same type as the column.

## See Also

### Comparing a column with a value
- [static func == (Self, Self.Element) -> [Bool]](./eqeq%28_,_%29-5jc0x.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is equal to a value.
- [static func == (Self.Element, Self) -> [Bool]](./eqeq%28_,_%29-4hx04.md)
  Returns a Boolean array that indicates whether the value is equal to the corresponding element of a column type.
- [static func != (Self, Self.Element) -> [Bool]](./noteq%28_,_%29-557vb.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type isn’t equal to a value.
- [static func != (Self.Element, Self) -> [Bool]](./noteq%28_,_%29-72ddh.md)
  Returns a Boolean array that indicates whether the value isn’t equal to the corresponding element of a column type.
- [static func < (Self, Self.Element) -> [Bool]](./op%28_,_%29-7gy2j.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is less than a value.
- [static func < (Self.Element, Self) -> [Bool]](./op%28_,_%29-70vl1.md)
  Returns a Boolean array that indicates whether the value is less than the corresponding element of a column type.
- [static func <= (Self, Self.Element) -> [Bool]](./opeq%28_,_%29-9wr8s.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is less than or equal to a value.
- [static func <= (Self.Element, Self) -> [Bool]](./opeq%28_,_%29-17m6l.md)
  Returns a Boolean array that indicates whether the value is less than or equal to the corresponding element of a column type.
- [static func > (Self, Self.Element) -> [Bool]](./op%28_,_%29-9rct2.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type is greater than a value.
- [static func > (Self.Element, Self) -> [Bool]](./op%28_,_%29-68any.md)
  Returns a Boolean array that indicates whether the value is greater than the corresponding element of a column type.
- [static func >= (Self.Element, Self) -> [Bool]](./opeq%28_,_%29-8jak4.md)
  Returns a Boolean array that indicates whether the value is greater than or equal to the corresponding element of a column type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnprotocol/_=(_:_:)-2w8gt)*