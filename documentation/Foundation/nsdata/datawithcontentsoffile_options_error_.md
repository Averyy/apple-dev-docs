# dataWithContentsOfFile:options:error:

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
+ (instancetype) dataWithContentsOfFile:(NSString *) path options:(NSDataReadingOptions) readOptionsMask error:(NSError **) errorPtr;
```

## Discussion

This method returns `nil` if the data object could not be created. In this case, `errorPtr` will contain an [`NSError`](../nserror.md) indicating the problem.

## Parameters

- `path`: The absolute path of the file from which to read data.
- `readOptionsMask`: A mask that specifies options for reading the data. Constant components are described in [`NSData.ReadingOptions`](./readingoptions.md).
- `errorPtr`: If an error occurs, upon return contains an error object that describes the problem.

## See Also

### Reading Data from a File
- [+ dataWithContentsOfFile:](./datawithcontentsoffile_.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/datawithcontentsoffile:options:error:)*