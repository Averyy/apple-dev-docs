# stringWithContentsOfFile:usedEncoding:error:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a string created by reading data from the file at a given path and returns by reference the encoding used to interpret the file.

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
+ (instancetype) stringWithContentsOfFile:(NSString *) path usedEncoding:(NSStringEncoding *) enc error:(NSError **) error;
```

#### Return Value

A string created by reading data from the file named by `path`. If the file can’t be opened or there is an encoding error, returns `nil`.

#### Discussion

This method attempts to determine the encoding of the file at `path`.

## Parameters

- `path`: A path to a file.
- `enc`: Upon return, if the file is read successfully, contains the encoding used to interpret the file at `path`. For possible values, see [`NSStringEncoding`](../nsstringencoding.md).
- `error`: If an error occurs, upon returns contains an `NSError` object that describes the problem. If you are not interested in possible errors, you may pass in `NULL`.

## See Also

### Creating and Initializing a String from a File
- [+ stringWithContentsOfFile:encoding:error:](./stringwithcontentsoffile_encoding_error_.md)
  Returns a string created by reading data from the file at a given path interpreted using a given encoding.
- [convenience init(contentsOfFile: String, encoding: UInt) throws](./init%28contentsoffile,encoding%29.md)
  Returns an `NSString` object initialized by reading data from the file at a given path using a given encoding.
- [convenience init(contentsOfFile: String, usedEncoding: UnsafeMutablePointer<UInt>?) throws](./init%28contentsoffile,usedencoding%29.md)
  Returns an `NSString` object initialized by reading data from the file at a given path and returns by reference the encoding used to interpret the characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/stringwithcontentsoffile:usedencoding:error:)*