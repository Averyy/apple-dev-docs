# lowercased()

**Framework**: Swift  
**Kind**: method

Returns a lowercased version of this character.

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
func lowercased() -> String
```

#### Discussion

Because case conversion can result in multiple characters, the result of `lowercased()` is a string.

```swift
let chars: [Character] = ["E", "É", "И", "Π", "1"]
for ch in chars {
    print(ch, "-->", ch.lowercased())
}
// Prints:
// E --> e
// É --> é
// И --> и
// Π --> π
// 1 --> 1
```

## See Also

- [var isCased: Bool](character/iscased.md)
  A Boolean value indicating whether this character changes under any form of case conversion.
- [var isUppercase: Bool](character/isuppercase.md)
  A Boolean value indicating whether this character is considered uppercase.
- [func uppercased() -> String](character/uppercased.md)
  Returns an uppercased version of this character.
- [var isLowercase: Bool](character/islowercase.md)
  A Boolean value indicating whether this character is considered lowercase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/lowercased())*