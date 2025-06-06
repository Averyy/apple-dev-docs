# Tips.ActionBuilder

**Framework**: TipKit  
**Kind**: struct

The result builder for generating a tip’s actions.

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
struct ActionBuilder
```

## Topics

### Type Methods
- [static func buildArray([[Tips.Action]]) -> [Tips.Action]](tips/actionbuilder/buildarray(_:).md)
  Builds a tip’s actions set from a nested array of actions.
- [static func buildEither(first: [Tips.Action]) -> [Tips.Action]](tips/actionbuilder/buildeither(first:).md)
  Builds a tip’s actions set from an if-else statement that produces an array of actions from the if-then branch.
- [static func buildEither(second: [Tips.Action]) -> [Tips.Action]](tips/actionbuilder/buildeither(second:).md)
  Builds a tip’s actions set from an if-else statement that produces an array of actions from the else branch.
- [static func buildExpression([Tips.Action]) -> [Tips.Action]](tips/actionbuilder/buildexpression(_:)-1x9ev.md)
  Builds a tip’s actions set from an array of actions.
- [static func buildExpression(Tips.Action) -> [Tips.Action]](tips/actionbuilder/buildexpression(_:)-21yaw.md)
  Builds a tip’s actions set from a single action value.
- [static func buildFinalResult([Tips.Action]) -> [Tips.Action]](tips/actionbuilder/buildfinalresult(_:).md)
  Builds a final set of actions that the tip’s view uses.
- [static func buildLimitedAvailability([Tips.Action]) -> [Tips.Action]](tips/actionbuilder/buildlimitedavailability(_:).md)
- [static func buildOptional([Tips.Action]?) -> [Tips.Action]](tips/actionbuilder/buildoptional(_:).md)
  Builds a tip’s actions set from an if statement.
- [static func buildPartialBlock(accumulated: [Tips.Action], next: [Tips.Action]) -> [Tips.Action]](tips/actionbuilder/buildpartialblock(accumulated:next:).md)
  Builds a tip’s actions set by appending an array of actions.
- [static func buildPartialBlock(first: [Tips.Action]) -> [Tips.Action]](tips/actionbuilder/buildpartialblock(first:).md)
  Builds a tip’s actions set from an array of actions.

## See Also

- [struct OptionsBuilder](tips/optionsbuilder.md)
  The result builder for generating a tip’s options.
- [struct RuleBuilder](tips/rulebuilder.md)
  The result builder for generating a tip’s rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/actionbuilder)*