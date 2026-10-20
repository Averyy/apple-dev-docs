# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a character containing the given Unicode scalar value.

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
init(_ content: Unicode.Scalar)
```

## Parameters

- `content`: The Unicode scalar value to convert into a character.

## See Also

### Working with a Character’s Unicode Values
- [var unicodeScalars: Character.UnicodeScalarView](./unicodescalars.md)
- [Character.UnicodeScalarView](./unicodescalarview.md)
- [var isASCII: Bool](./isascii.md)
  A Boolean value indicating whether this is an ASCII character.
- [var asciiValue: UInt8?](./asciivalue.md)
  The ASCII encoding value of this character, if it is an ASCII character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/init(_:)-8hq6x)*