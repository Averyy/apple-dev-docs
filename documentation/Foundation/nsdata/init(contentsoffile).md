# init(contentsOfFile:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a data object with the content of the file at a given path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(contentsOfFile path: String)
```

```objc
- (instancetype) initWithContentsOfFile:(NSString *) path;
```

## Return Value

A data object initialized by reading into it the data from the file specified by `path`.

## Discussion

This method is equivalent to [`init(contentsOfFile:options:)`](./init%28contentsoffile,options%29.md) with no options.

## Parameters

- `path`: The absolute path of the file from which to read data.

## See Also

### Reading Data from a File
- [init(contentsOfFile: String, options: NSData.ReadingOptions) throws](./init%28contentsoffile,options%29.md)
  Initializes a data object with the content of the file at a given path.
- [NSData.ReadingOptions](./readingoptions.md)
  Options for methods used to read data objects.
- [init?(contentsOfMappedFile: String)](./init%28contentsofmappedfile%29.md)
  Initializes a data object with the contents of the mapped file specified by a given path.
- [class func dataWithContentsOfMappedFile(String) -> Any?](./datawithcontentsofmappedfile%28_%29.md)
  Creates a data object from the mapped file at a given path.
- [+ dataWithContentsOfFile:options:error:](./datawithcontentsoffile_options_error_.md)
  Creates a data object by reading every byte from the file at a given path.
### Related Documentation
- [+ dataWithContentsOfFile:](./datawithcontentsoffile_.md)
  Creates a data object by reading every byte from the file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/init(contentsoffile:))*