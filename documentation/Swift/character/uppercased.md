# uppercased()

**Framework**: Swift  
**Kind**: method

Returns an uppercased version of this character.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func uppercased() -> String
```

#### Discussion

Because case conversion can result in multiple characters, the result of `uppercased()` is a string.

```swift
let chars: [Character] = ["e", "é", "и", "π", "ß", "1"]
for ch in chars {
    print(ch, "-->", ch.uppercased())
}
// Prints:
// e --> E
// é --> É
// и --> И
// π --> Π
// ß --> SS
// 1 --> 1
```

## See Also

- [var isCased: Bool](character/iscased.md)
  A Boolean value indicating whether this character changes under any form of case conversion.
- [var isUppercase: Bool](character/isuppercase.md)
  A Boolean value indicating whether this character is considered uppercase.
- [var isLowercase: Bool](character/islowercase.md)
  A Boolean value indicating whether this character is considered lowercase.
- [func lowercased() -> String](character/lowercased.md)
  Returns a lowercased version of this character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/uppercased())*