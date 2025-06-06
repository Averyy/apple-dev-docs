# asciiValue

**Framework**: Swift  
**Kind**: property

The ASCII encoding value of this character, if it is an ASCII character.

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
var asciiValue: UInt8? { get }
```

#### Discussion

```swift
let chars: [Character] = ["a", " ", "™"]
for ch in chars {
    print(ch, "-->", ch.asciiValue)
}
// Prints:
// a --> Optional(97)
//   --> Optional(32)
// ™ --> nil
```

A character with the value “\r\n” (CR-LF) is normalized to “\n” (LF) and has an `asciiValue` property equal to 10.

```swift
let cr = "\r" as Character
// cr.asciiValue == 13
let lf = "\n" as Character
// lf.asciiValue == 10
let crlf = "\r\n" as Character
// crlf.asciiValue == 10
```

## See Also

- [init(Unicode.Scalar)](character/init(_:)-8hq6x.md)
  Creates a character containing the given Unicode scalar value.
- [var unicodeScalars: Character.UnicodeScalarView](character/unicodescalars.md)
- [Character.UnicodeScalarView](character/unicodescalarview.md)
- [var isASCII: Bool](character/isascii.md)
  A Boolean value indicating whether this is an ASCII character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/asciivalue)*