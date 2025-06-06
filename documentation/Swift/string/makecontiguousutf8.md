# makeContiguousUTF8()

**Framework**: Swift  
**Kind**: method

If this string is not contiguous, make it so. If this mutates the string, it will invalidate any pre-existing indices.

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
mutating func makeContiguousUTF8()
```

#### Discussion

Complexity: O(n) if non-contiguous, O(1) if already contiguous

## See Also

- [static var availableStringEncodings: [String.Encoding]](string/availablestringencodings.md)
  An array of the encodings that strings support in the application’s environment.
- [static var defaultCStringEncoding: String.Encoding](string/defaultcstringencoding.md)
  The C-string encoding assumed for any method accepting a C string as an argument.
- [static func localizedName(of: String.Encoding) -> String](string/localizedname(of:).md)
  Returns a human-readable string giving the name of the specified encoding.
- [var isContiguousUTF8: Bool](string/iscontiguousutf8.md)
  Returns whether this string is capable of providing access to validly-encoded UTF-8 contents in contiguous memory in O(1) time.
- [func withUTF8<R>((UnsafeBufferPointer<UInt8>) throws -> R) rethrows -> R](string/withutf8(_:).md)
  Runs `body` over the content of this string in contiguous memory. If this string is not contiguous, this will first make it contiguous, which will also speed up subsequent access. If this mutates the string, it will invalidate any pre-existing indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/makecontiguousutf8())*