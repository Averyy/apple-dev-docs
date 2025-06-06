# matchingSemantics(_:)

**Framework**: Swift  
**Kind**: method

Returns a regular expression that matches with the specified semantic level.

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
func matchingSemantics(_ semanticLevel: RegexSemanticLevel) -> Regex<Regex<Output>.RegexOutput>
```

#### Return Value

The modified regular expression.

#### Discussion

When matching with grapheme cluster semantics (the default), metacharacters like `.` and `\w`, custom character classes, and character class instances like `.any` match a grapheme cluster when possible, corresponding with the default string representation. In addition, matching with grapheme cluster semantics compares characters using their canonical representation, corresponding with how strings comparison works.

When matching with Unicode scalar semantics, metacharacters and character classes always match a single Unicode scalar value, even if that scalar comprises part of a grapheme cluster.

These semantic levels can lead to different results, especially when working with strings that have decomposed characters. In the following example, `queRegex` matches any 3-character string that begins with `"q"`.

```swift
let composed = "qué"
let decomposed = "que\u{301}"

let queRegex = /^q..$/

print(composed.contains(queRegex))
// Prints "true"
print(decomposed.contains(queRegex))
// Prints "true"
```

When using Unicode scalar semantics, however, the regular expression only matches the composed version of the string, because each `.` matches a single Unicode scalar value.

```swift
let queRegexScalar = queRegex.matchingSemantics(.unicodeScalar)
print(composed.contains(queRegexScalar))
// Prints "true"
print(decomposed.contains(queRegexScalar))
// Prints "false"
```

## Parameters

- `semanticLevel`: The semantics to use during matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regex/matchingsemantics(_:))*