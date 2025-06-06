# write(to:)

**Framework**: Swift  
**Kind**: method

Writes the textual representation of the Unicode scalar into the given output stream.

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
func write<Target>(to target: inout Target) where Target : TextOutputStream
```

## Parameters

- `target`: An output stream.

## See Also

- [var description: String](unicode/scalar/description.md)
  A textual representation of the Unicode scalar.
- [func escaped(asASCII: Bool) -> String](unicode/scalar/escaped(asascii:).md)
  Returns a string representation of the Unicode scalar.
- [var utf16: Unicode.Scalar.UTF16View](unicode/scalar/utf16.md)
- [Unicode.Scalar.UTF16View](unicode/scalar/utf16view.md)
- [var debugDescription: String](unicode/scalar/debugdescription.md)
  An escaped textual representation of the Unicode scalar, suitable for debugging.
- [var customMirror: Mirror](unicode/scalar/custommirror.md)
  A mirror that reflects the `Unicode.Scalar` instance.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](unicode/scalar/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Unicode.Scalar` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/write(to:))*