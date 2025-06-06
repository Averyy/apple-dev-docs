# Unicode.Scalar.UTF16View

**Framework**: Swift  
**Kind**: struct

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
@frozen
struct UTF16View
```

## Topics

### Default Implementations
- [BidirectionalCollection Implementations](unicode/scalar/utf16view/bidirectionalcollection-implementations.md)
- [Collection Implementations](unicode/scalar/utf16view/collection-implementations.md)
- [RandomAccessCollection Implementations](unicode/scalar/utf16view/randomaccesscollection-implementations.md)
- [Sequence Implementations](unicode/scalar/utf16view/sequence-implementations.md)

## Relationships

### Conforms To
- [BidirectionalCollection](bidirectionalcollection.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [Collection](collection.md)
- [Copyable](copyable.md)
- [RandomAccessCollection](randomaccesscollection.md)
- [Sendable](sendable.md)
- [Sequence](sequence.md)

## See Also

- [var description: String](unicode/scalar/description.md)
  A textual representation of the Unicode scalar.
- [func write<Target>(to: inout Target)](unicode/scalar/write(to:).md)
  Writes the textual representation of the Unicode scalar into the given output stream.
- [func escaped(asASCII: Bool) -> String](unicode/scalar/escaped(asascii:).md)
  Returns a string representation of the Unicode scalar.
- [var utf16: Unicode.Scalar.UTF16View](unicode/scalar/utf16.md)
- [var debugDescription: String](unicode/scalar/debugdescription.md)
  An escaped textual representation of the Unicode scalar, suitable for debugging.
- [var customMirror: Mirror](unicode/scalar/custommirror.md)
  A mirror that reflects the `Unicode.Scalar` instance.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](unicode/scalar/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Unicode.Scalar` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/utf16view)*