# ChoiceOf

**Framework**: RegexBuilder  
**Kind**: struct

A regex component that chooses exactly one of its constituent regex components when matching.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct ChoiceOf<Output>
```

#### Overview

You can use `ChoiceOf` to provide a group of regex components, each of which can be exclusively matched. In this example, `regex` successfully matches either a `"CREDIT"` or `"DEBIT"` substring:

```swift
let regex = Regex {
    ChoiceOf {
        "CREDIT"
        "DEBIT"
    }
}
let match = try regex.prefixMatch(in: "DEBIT    04032020    Payroll $69.73")
print(match?.0 as Any)
// Prints "DEBIT"
```

## Topics

### Initializers
- [init(() -> ChoiceOf<Output>)](choiceof/init(_:).md)
  Creates a regex component that chooses exactly one of the regex components provided by the builder closure.
### Instance Properties
- [var regex: Regex<Output>](choiceof/regex.md)
  The regular expression represented by this component.
### Type Aliases
- [typealias RegexOutput](choiceof/regexoutput.md)
  The output type for this regular expression.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [RegexComponent](../swift/regexcomponent.md)

## See Also

- [struct CharacterClass](characterclass.md)
  A class of characters that match in a regex.
- [struct Anchor](anchor.md)
  A regex component that matches a specific condition at a particular position in an input string.
- [struct Lookahead](lookahead.md)
  A regex component that allows a match to continue only if its contents match at the given location.
- [struct NegativeLookahead](negativelookahead.md)
  A regex component that allows a match to continue only if its contents do not match at the given location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/choiceof)*