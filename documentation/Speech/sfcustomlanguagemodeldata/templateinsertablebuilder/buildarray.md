# buildArray(_:)

**Framework**: Speech  
**Kind**: method

Enables support for `for..in` loops.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
static func buildArray(_ components: [any TemplateInsertable]) -> any TemplateInsertable
```

## See Also

- [static func buildBlock(any TemplateInsertable...) -> any TemplateInsertable](sfcustomlanguagemodeldata/templateinsertablebuilder/buildblock(_:).md)
  Combines statement blocks into a single product.
- [static func buildEither(first: any TemplateInsertable) -> any TemplateInsertable](sfcustomlanguagemodeldata/templateinsertablebuilder/buildeither(first:).md)
  Enables support for `if-else` and `switch` constructs.
- [static func buildEither(second: any TemplateInsertable) -> any TemplateInsertable](sfcustomlanguagemodeldata/templateinsertablebuilder/buildeither(second:).md)
  Enables support for `if-else` and `switch` constructs.
- [static func buildOptional((any TemplateInsertable)?) -> any TemplateInsertable](sfcustomlanguagemodeldata/templateinsertablebuilder/buildoptional(_:).md)
  Enables support for `if` statements that do not have an `else` clause.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/templateinsertablebuilder/buildarray(_:))*