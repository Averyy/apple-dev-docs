# buildOptional(_:)

**Framework**: Speech  
**Kind**: method

Enables support for `if` statements that do not have an `else` clause.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
static func buildOptional(_ component: (any DataInsertable)?) -> any DataInsertable
```

## See Also

- [static func buildArray([any DataInsertable]) -> any DataInsertable](sfcustomlanguagemodeldata/datainsertablebuilder/buildarray(_:).md)
  Enables support for `for..in` loops.
- [static func buildBlock(any DataInsertable...) -> any DataInsertable](sfcustomlanguagemodeldata/datainsertablebuilder/buildblock(_:).md)
  Combines statement blocks into a single product.
- [static func buildEither(first: any DataInsertable) -> any DataInsertable](sfcustomlanguagemodeldata/datainsertablebuilder/buildeither(first:).md)
  Enables support for `if-else` and `switch` constructs.
- [static func buildEither(second: any DataInsertable) -> any DataInsertable](sfcustomlanguagemodeldata/datainsertablebuilder/buildeither(second:).md)
  Enables support for `if-else` and `switch` constructs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/datainsertablebuilder/buildoptional(_:))*