# dataWithContentsOfMappedFile(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a data object from the mapped file at a given path.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.10
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use +dataWithContentsOfURL:options:error: and NSDataReadingMappedIfSafe or NSDataReadingMappedAlways instead.

## Declaration

```swift
class func dataWithContentsOfMappedFile(_ path: String) -> Any?
```

```objc
+ (id) dataWithContentsOfMappedFile:(NSString *) path;
```

## Discussion

This method returns `nil` if the data object could not be created

Because of file mapping restrictions, this method should only be used if the file is guaranteed to exist for the duration of the data object’s existence. It is generally safer to use the [`dataWithContentsOfFile:`](./datawithcontentsoffile_.md) method.

This methods assumes mapped files are available from the underlying operating system. A mapped file uses virtual memory techniques to avoid copying pages of the file into memory until they are actually needed.

## Parameters

- `path`: The absolute path of the file from which to read data.

## See Also

### Reading Data from a File
- [init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes a data object with the content of the file at a given path.
- [init(contentsOfFile: String, options: NSData.ReadingOptions) throws](./init%28contentsoffile,options%29.md)
  Initializes a data object with the content of the file at a given path.
- [NSData.ReadingOptions](./readingoptions.md)
  Options for methods used to read data objects.
- [init?(contentsOfMappedFile: String)](./init%28contentsofmappedfile%29.md)
  Initializes a data object with the contents of the mapped file specified by a given path.
- [+ dataWithContentsOfFile:options:error:](./datawithcontentsoffile_options_error_.md)
  Creates a data object by reading every byte from the file at a given path.
### Related Documentation
- [+ dataWithContentsOfFile:](./datawithcontentsoffile_.md)
  Creates a data object by reading every byte from the file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/datawithcontentsofmappedfile(_:))*