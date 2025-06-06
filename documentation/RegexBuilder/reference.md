# Reference

**Framework**: RegexBuilder  
**Kind**: struct

A reference to a captured portion of a regular expression.

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
struct Reference<Capture>
```

#### Overview

You can use a `Reference` to access a regular expression, both during the matching process and after a capture has been successful.

In this example, the `kind` reference captures either `"CREDIT"` or `"DEBIT"` at the beginning of a line. Later in the regular expression, the presence of `kind` matches the same substring that was captured previously at the end of the line.

```swift
let kindRef = Reference(Substring.self)
let kindRegex = ChoiceOf {
    "CREDIT"
    "DEBIT"
}

let transactionRegex = Regex {
    Anchor.startOfLine
    Capture(kindRegex, as: kindRef)
    OneOrMore(.anyNonNewline)
    kindRef
    Anchor.endOfLine
}

let validTransaction = "CREDIT     109912311421    Payroll   $69.73  CREDIT"
let invalidTransaction = "DEBIT     00522142123    Expense   $5.17  CREDIT"

print(validTransaction.contains(transactionRegex))
// Prints "true"
print(invalidTransaction.contains(transactionRegex))
// Prints "false"
```

Any reference that is used for matching must be captured elsewhere in the `Regex` block. You can use a reference for matching before it is captured; in that case, the reference will not match until it has previously been captured.

To access the captured “transaction kind”, you can use the `kind` reference to subscript a `Regex.Match` instance:

```swift
if let match = validTransaction.firstMatch(of: transactionRegex) {
    print(match[kindRef])
}
// Prints "CREDIT"
```

To use a `Reference` to capture a transformed value, include a `transform` closure when capturing.

```swift
struct Transaction {
    var id: UInt64
}
let transactionRef = Reference(Transaction.self)

let transactionIDRegex = Regex {
    Capture(kindRegex, as: kindRef)
    OneOrMore(.whitespace)
    TryCapture(as: transactionRef) {
        OneOrMore(.digit)
    } transform: { str in
        UInt64(str).map(Transaction.init(id:))
    }
    OneOrMore(.anyNonNewline)
    kindRef
    Anchor.endOfLine
}

if let match = validTransaction.firstMatch(of: transactionIDRegex) {
    print(match[transactionRef])
}
// Prints "Transaction(id: 109912311421)"
```

## Topics

### Initializers
- [init(Capture.Type)](reference/init(_:).md)
  Creates a reference with the specified capture type.
### Instance Properties
- [var regex: Regex<Capture>](reference/regex.md)
  The regular expression represented by this component.
### Type Aliases
- [Reference.RegexOutput](reference/regexoutput.md)
  The output type for this regular expression.

## Relationships

### Conforms To
- [RegexComponent](../swift/regexcomponent.md)

## See Also

- [struct Capture](capture.md)
  A regex component that saves the matched substring, or a transformed result, for access in a regex match.
- [struct TryCapture](trycapture.md)
  A regex component that attempts to transform a matched substring, saving the result if successful and backtracking if the transformation fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/reference)*