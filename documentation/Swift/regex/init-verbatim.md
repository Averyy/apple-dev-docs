# init(verbatim:)

**Framework**: Swift  
**Kind**: init

Creates a regular expression that matches the given string exactly, as though every metacharacter in it was escaped.

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
init(verbatim verbatimString: String)
```

#### Discussion

This example creates a regular expression that matches the string `"(adj)"`, including the parentheses. Although parentheses are regular expression metacharacters, they do not need escaping in the string passed as `verbatimString`.

```swift
let adjectiveDesignator = Regex<Substring>(verbatim: "(adj.)")

print("awesome (adj.)".contains(adjectiveDesignator))
// Prints "true"
print("apple (n.)".contains(adjectiveDesignator))
// Prints "false"
```

## Parameters

- `verbatimString`: A string to convert into a regular expression   exactly, escaping any metacharacters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regex/init(verbatim:))*