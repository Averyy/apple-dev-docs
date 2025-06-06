# init(contentsOf:usedEncoding:)

**Framework**: Swift  
**Kind**: init

Produces a string created by reading data from a given URL and returns by reference the encoding used to interpret the data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(contentsOf url: URL, usedEncoding: inout String.Encoding) throws
```

## See Also

- [init(contentsOf: URL) throws](string/init(contentsof:).md)
- [init(contentsOf: URL, encoding: String.Encoding) throws](string/init(contentsof:encoding:).md)
  Produces a string created by reading data from a given URL interpreted using a given encoding.
- [init(contentsOfFile: String) throws](string/init(contentsoffile:).md)
- [init(contentsOfFile: String, encoding: String.Encoding) throws](string/init(contentsoffile:encoding:).md)
  Produces a string created by reading data from the file at a given path interpreted using a given encoding.
- [init(contentsOfFile: String, usedEncoding: inout String.Encoding) throws](string/init(contentsoffile:usedencoding:).md)
  Produces a string created by reading data from the file at a given path and returns by reference the encoding used to interpret the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(contentsof:usedencoding:))*