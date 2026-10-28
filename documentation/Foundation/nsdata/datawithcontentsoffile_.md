# dataWithContentsOfFile:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a data object by reading every byte from the file at a given path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) dataWithContentsOfFile:(NSString *) path;
```

## Discussion

This method returns `nil` if the data object could not be created. If you need to know the reason for failure, use [`dataWithContentsOfFile:options:error:`](./datawithcontentsoffile_options_error_.md).

This method is equivalent to calling [`dataWithContentsOfFile:options:error:`](./datawithcontentsoffile_options_error_.md) and passing no options.

A sample using this method can be found in [Working With Binary Data](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Tasks/WorkingBinaryData.html#//apple_ref/doc/uid/20000717).

## Parameters

- `path`: The absolute path of the file from which to read data.

## See Also

### Reading Data from a File
- [+ dataWithContentsOfFile:options:error:](./datawithcontentsoffile_options_error_.md)
  Creates a data object by reading every byte from the file at a given path.
- [init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes a data object with the content of the file at a given path.
- [init(contentsOfFile: String, options: NSData.ReadingOptions) throws](./init%28contentsoffile,options%29.md)
  Initializes a data object with the content of the file at a given path.
- [NSData.ReadingOptions](./readingoptions.md)
  Options for methods used to read data objects.
- [init?(contentsOfMappedFile: String)](./init%28contentsofmappedfile%29.md)
  Initializes a data object with the contents of the mapped file specified by a given path.
- [class func dataWithContentsOfMappedFile(String) -> Any?](./datawithcontentsofmappedfile%28_%29.md)
  Creates a data object from the mapped file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/datawithcontentsoffile:)*