# escaped(asASCII:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns a string representation of the Unicode scalar.

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
func escaped(asASCII forceASCII: Bool) -> String
```

## Return Value

A string representation of the scalar.

## Discussion

Scalar values representing characters that are normally unprintable or that otherwise require escaping are escaped with a backslash.

```swift
let tab = Unicode.Scalar(9)!
print(tab)
// Prints " "
print(tab.escaped(asASCII: false))
// Prints "\t"
```

When the `forceASCII` parameter is `true`, a `Unicode.Scalar` instance with a value greater than 127 is represented using an escaped numeric value; otherwise, non-ASCII characters are represented using their typical string value.

```swift
let bap = Unicode.Scalar(48165)!
print(bap.escaped(asASCII: false))
// Prints "밥"
print(bap.escaped(asASCII: true))
// Prints "\u{BC25}"
```

## Parameters

- `forceASCII`: Pass `true` if you need the result to use only ASCII characters; otherwise, pass `false`.

## See Also

### Printing and Displaying a Scalar
- [var description: String](./description.md)
  A textual representation of the Unicode scalar.
- [func write<Target>(to: inout Target)](./write%28to%29.md)
  Writes the textual representation of the Unicode scalar into the given output stream.
- [var utf16: Unicode.Scalar.UTF16View](./utf16.md)
- [Unicode.Scalar.UTF16View](./utf16view.md)
- [var debugDescription: String](./debugdescription.md)
  An escaped textual representation of the Unicode scalar, suitable for debugging.
- [var customMirror: Mirror](./custommirror.md)
  A mirror that reflects the `Unicode.Scalar` instance.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](./customplaygroundquicklook.md)
  A custom playground Quick Look for the `Unicode.Scalar` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/escaped(asascii:))*