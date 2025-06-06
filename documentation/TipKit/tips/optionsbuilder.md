# Tips.OptionsBuilder

**Framework**: TipKit  
**Kind**: struct

The result builder for generating a tip’s options.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@resultBuilder
struct OptionsBuilder
```

## Topics

### Type Methods
- [static func buildBlock() -> some TipOption](tips/optionsbuilder/buildblock.md)
- [static func buildEither(first: some TipOption) -> some TipOption](tips/optionsbuilder/buildeither(first:).md)
- [static func buildEither(second: some TipOption) -> some TipOption](tips/optionsbuilder/buildeither(second:).md)
- [static func buildExpression((any TipOption)?) -> some TipOption](tips/optionsbuilder/buildexpression(_:)-132ru.md)
- [static func buildExpression([some TipOption]) -> some TipOption](tips/optionsbuilder/buildexpression(_:)-6xexl.md)
- [static func buildExpression(some TipOption) -> some TipOption](tips/optionsbuilder/buildexpression(_:)-9px05.md)
- [static func buildExpression([(any TipOption)?]) -> some TipOption](tips/optionsbuilder/buildexpression(_:)-r6fx.md)
- [static func buildFinalResult(some TipOption) -> [any TipOption]](tips/optionsbuilder/buildfinalresult(_:).md)
- [static func buildOptional([(any TipOption)?]) -> some TipOption](tips/optionsbuilder/buildoptional(_:)-4056p.md)
- [static func buildOptional((any TipOption)?) -> some TipOption](tips/optionsbuilder/buildoptional(_:)-5sz66.md)
- [static func buildPartialBlock(accumulated: some TipOption, next: some TipOption) -> some TipOption](tips/optionsbuilder/buildpartialblock(accumulated:next:).md)
- [static func buildPartialBlock(first: some TipOption) -> some TipOption](tips/optionsbuilder/buildpartialblock(first:).md)

## See Also

- [struct ActionBuilder](tips/actionbuilder.md)
  The result builder for generating a tip’s actions.
- [struct RuleBuilder](tips/rulebuilder.md)
  The result builder for generating a tip’s rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/optionsbuilder)*