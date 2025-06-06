# Tips.RuleBuilder

**Framework**: TipKit  
**Kind**: struct

The result builder for generating a tip’s rules.

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
struct RuleBuilder
```

## Topics

### Type Methods
- [static func buildBlock() -> [Tips.Rule]](tips/rulebuilder/buildblock.md)
- [static func buildEither(first: [Tips.Rule]) -> [Tips.Rule]](tips/rulebuilder/buildeither(first:).md)
- [static func buildEither(second: [Tips.Rule]) -> [Tips.Rule]](tips/rulebuilder/buildeither(second:).md)
- [static func buildExpression(Tips.Rule?) -> [Tips.Rule]](tips/rulebuilder/buildexpression(_:)-4fme4.md)
- [static func buildExpression([Tips.Rule]) -> [Tips.Rule]](tips/rulebuilder/buildexpression(_:)-51kbv.md)
- [static func buildExpression(Tips.Rule) -> [Tips.Rule]](tips/rulebuilder/buildexpression(_:)-550io.md)
- [static func buildExpression([Tips.Rule?]) -> [Tips.Rule]](tips/rulebuilder/buildexpression(_:)-8sdof.md)
- [static func buildOptional(Tips.Rule?) -> [Tips.Rule]](tips/rulebuilder/buildoptional(_:)-29ezt.md)
- [static func buildOptional([Tips.Rule?]) -> [Tips.Rule]](tips/rulebuilder/buildoptional(_:)-62rsn.md)
- [static func buildPartialBlock(accumulated: [Tips.Rule], next: [Tips.Rule]) -> [Tips.Rule]](tips/rulebuilder/buildpartialblock(accumulated:next:).md)
- [static func buildPartialBlock(first: [Tips.Rule]) -> [Tips.Rule]](tips/rulebuilder/buildpartialblock(first:).md)

## See Also

- [struct ActionBuilder](tips/actionbuilder.md)
  The result builder for generating a tip’s actions.
- [struct OptionsBuilder](tips/optionsbuilder.md)
  The result builder for generating a tip’s options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/rulebuilder)*