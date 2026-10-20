# init(contentsOfFile:encoding:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Produces a string created by reading data from the file at a given path interpreted using a given encoding.

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
init(contentsOfFile path: String, encoding enc: String.Encoding) throws
```

## See Also

### Creating a String from a File or URL
- [init(contentsOf: URL) throws](./init%28contentsof%29.md)
- [init(contentsOf: URL, encoding: String.Encoding) throws](./init%28contentsof,encoding%29.md)
  Produces a string created by reading data from a given URL interpreted using a given encoding.
- [init(contentsOf: URL, usedEncoding: inout String.Encoding) throws](./init%28contentsof,usedencoding%29.md)
  Produces a string created by reading data from a given URL and returns by reference the encoding used to interpret the data.
- [init(contentsOfFile: String) throws](./init%28contentsoffile%29.md)
- [init(contentsOfFile: String, usedEncoding: inout String.Encoding) throws](./init%28contentsoffile,usedencoding%29.md)
  Produces a string created by reading data from the file at a given path and returns by reference the encoding used to interpret the file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(contentsoffile:encoding:))*