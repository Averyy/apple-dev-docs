# buildEither(second:)

**Framework**: Speech  
**Kind**: method  
**Role**: Type Method

Enables support for `if-else` and `switch` constructs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+

## Declaration

```swift
static func buildEither(second: any TemplateInsertable) -> any TemplateInsertable
```

## See Also

### Result builder methods
- [static func buildArray([any TemplateInsertable]) -> any TemplateInsertable](./buildarray%28_%29.md)
  Enables support for `for..in` loops.
- [static func buildBlock(any TemplateInsertable...) -> any TemplateInsertable](./buildblock%28_%29.md)
  Combines statement blocks into a single product.
- [static func buildEither(first: any TemplateInsertable) -> any TemplateInsertable](./buildeither%28first%29.md)
  Enables support for `if-else` and `switch` constructs.
- [static func buildOptional((any TemplateInsertable)?) -> any TemplateInsertable](./buildoptional%28_%29.md)
  Enables support for `if` statements that do not have an `else` clause.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/templateinsertablebuilder/buildeither(second:))*