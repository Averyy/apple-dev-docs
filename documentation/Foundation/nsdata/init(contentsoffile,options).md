# init(contentsOfFile:options:)

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
init(contentsOfFile path: String, options readOptionsMask: NSData.ReadingOptions = []) throws
```

```objc
- (instancetype) initWithContentsOfFile:(NSString *) path options:(NSDataReadingOptions) readOptionsMask error:(NSError **) errorPtr;
```

## Return Value

A data object initialized by reading into it the data from the file specified by `path`.

## Discussion

> **Handling Errors in Swift**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `path`: The absolute path of the file from which to read data.
- `readOptionsMask`: A mask that specifies options for reading the data. Constant components are described in [`NSData.ReadingOptions`](./readingoptions.md).

## See Also

### Reading Data from a File
- [init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Initializes a data object with the content of the file at a given path.
- [NSData.ReadingOptions](./readingoptions.md)
  Options for methods used to read data objects.
- [init?(contentsOfMappedFile: String)](./init%28contentsofmappedfile%29.md)
  Initializes a data object with the contents of the mapped file specified by a given path.
- [class func dataWithContentsOfMappedFile(String) -> Any?](./datawithcontentsofmappedfile%28_%29.md)
  Creates a data object from the mapped file at a given path.
- [+ dataWithContentsOfFile:](./datawithcontentsoffile_.md)
  Creates a data object by reading every byte from the file at a given path.
### Related Documentation
- [+ dataWithContentsOfFile:options:error:](./datawithcontentsoffile_options_error_.md)
  Creates a data object by reading every byte from the file at a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdata/init(contentsoffile:options:))*