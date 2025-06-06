# init(_:)

**Framework**: RegexBuilder  
**Kind**: init

Creates a regex component that chooses exactly one of the regex components provided by the builder closure.

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
init(@AlternationBuilder _ builder: () -> ChoiceOf<Output>)
```

#### Discussion

In this example, `regex` successfully matches either a `"CREDIT"` or `"DEBIT"` substring:

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

## Parameters

- `builder`: A builder closure that declares a list of regex   components, each of which can be exclusively matched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/choiceof/init(_:))*