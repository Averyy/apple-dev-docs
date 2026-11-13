# !=(_:_:)

**Framework**: TabularData  
**Kind**: op  
**Role**: Operator

Returns a Boolean array that indicates whether the value isn’t equal to the corresponding element of a column type.

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
static func != (lhs: Self.Element, rhs: Self) -> [Bool]
```

Available when `Element` conforms to `Comparable`.

## Return Value

A Boolean array.

## Discussion

- lhs: A value of the same type as the column.
- rhs: A column type.

## See Also

### Comparing two columns
- [static func != (Self, Self.Element) -> [Bool]](./noteq%28_,_%29-557vb.md)
  Returns a Boolean array that indicates whether the corresponding element of a column type isn’t equal to a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/columnprotocol/!=(_:_:)-72ddh)*