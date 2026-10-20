# description

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

A textual representation of the Unicode scalar.

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
var description: String { get }
```

## See Also

### Printing and Displaying a Scalar
- [func write<Target>(to: inout Target)](./write%28to%29.md)
  Writes the textual representation of the Unicode scalar into the given output stream.
- [func escaped(asASCII: Bool) -> String](./escaped%28asascii%29.md)
  Returns a string representation of the Unicode scalar.
- [var utf16: Unicode.Scalar.UTF16View](./utf16.md)
- [Unicode.Scalar.UTF16View](./utf16view.md)
- [var debugDescription: String](./debugdescription.md)
  An escaped textual representation of the Unicode scalar, suitable for debugging.
- [var customMirror: Mirror](./custommirror.md)
  A mirror that reflects the `Unicode.Scalar` instance.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](./customplaygroundquicklook.md)
  A custom playground Quick Look for the `Unicode.Scalar` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/description)*