# inverted

**Framework**: RegexBuilder  
**Kind**: property

A character class that matches any character that does not match this character class.

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
var inverted: CharacterClass { get }
```

#### Discussion

For example, you can use the `inverted` property to create a character class that excludes a specific group of characters:

```swift
let validCharacters = CharacterClass("a"..."z", .anyOf("-_"))
let invalidCharacters = validCharacters.inverted

let username = "user123"
if username.contains(invalidCharacters) {
    print("Invalid username: '\(username)'")
}
// Prints "Invalid username: 'user123'"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/characterclass/inverted)*