# init(contentsOfFile:encoding:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns an `NSString` object initialized by reading data from the file at a given path using a given encoding.

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
convenience init(contentsOfFile path: String, encoding enc: UInt) throws
```

```objc
- (instancetype) initWithContentsOfFile:(NSString *) path encoding:(NSStringEncoding) enc error:(NSError **) error;
```

#### Return Value

An `NSString` object initialized by reading data from the file named by `path` using the encoding, `enc`. The returned object may be different from the original receiver. If the file can’t be opened or there is an encoding error, returns `nil`.

#### Discussion

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `path`: A path to a file.
- `enc`: The encoding of the file at `path`. For possible values, see [`NSStringEncoding`](../nsstringencoding.md).

## See Also

### Creating and Initializing a String from a File
- [convenience init(contentsOfFile: String, usedEncoding: UnsafeMutablePointer<UInt>?) throws](./init%28contentsoffile,usedencoding%29.md)
  Returns an `NSString` object initialized by reading data from the file at a given path and returns by reference the encoding used to interpret the characters.
- [+ stringWithContentsOfFile:usedEncoding:error:](./stringwithcontentsoffile_usedencoding_error_.md)
  Returns a string created by reading data from the file at a given path and returns by reference the encoding used to interpret the file.
### Related Documentation
- [+ stringWithContentsOfFile:encoding:error:](./stringwithcontentsoffile_encoding_error_.md)
  Returns a string created by reading data from the file at a given path interpreted using a given encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(contentsoffile:encoding:))*