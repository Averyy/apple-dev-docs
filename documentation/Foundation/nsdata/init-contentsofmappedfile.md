# init(contentsOfMappedFile:)

**Framework**: Foundation  
**Kind**: init

Initializes a data object with the contents of the mapped file specified by a given path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(contentsOfMappedFile path: String)
```

#### Return Value

A data object initialized by reading into it the mapped file specified by `path`.

## Parameters

- `path`: The absolute path of the file from which to read data.

## See Also

- [init?(contentsOfFile: String)](nsdata/init(contentsoffile:).md)
  Initializes a data object with the content of the file at a given path.
- [init(contentsOfFile: String, options: NSData.ReadingOptions) throws](nsdata/init(contentsoffile:options:).md)
  Initializes a data object with the content of the file at a given path.
- [NSData.ReadingOptions](nsdata/readingoptions.md)
  Options for methods used to read data objects.
- [class func dataWithContentsOfMappedFile(String) -> Any?](nsdata/datawithcontentsofmappedfile(_:).md)
  Creates a data object from the mapped file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/init(contentsofmappedfile:))*