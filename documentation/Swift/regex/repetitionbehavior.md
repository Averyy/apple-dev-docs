# repetitionBehavior(_:)

**Framework**: Swift  
**Kind**: method

Returns a regular expression where quantifiers use the specified behavior by default.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func repetitionBehavior(_ behavior: RegexRepetitionBehavior) -> Regex<Regex<Output>.RegexOutput>
```

#### Discussion

This setting does not affect calls to quantifier methods, such as `OneOrMore`, that include an explicit `behavior` parameter.

Passing `.eager` or `.reluctant` to this method corresponds to applying the `(?-U)` or `(?U)` option in regex syntax, respectively.

## Parameters

- `behavior`: The default behavior to use for quantifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regex/repetitionbehavior(_:))*