# write(toFile:atomically:encoding:)

**Framework**: Foundation  
**Kind**: method

Writes the contents of the receiver to a file at a given path using a given encoding.

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
func write(toFile path: String, atomically useAuxiliaryFile: Bool, encoding enc: UInt) throws
```

#### Discussion

This method overwrites any existing file at `path`.

This method stores the specified encoding with the file in an extended attribute under the name `com.apple.TextEncoding`. The value contains the IANA name for the encoding and the [`CFStringEncoding`](https://developer.apple.com/documentation/CoreFoundation/CFStringEncoding) value for the encoding, separated by a semicolon. The `CFStringEncoding` value is written as an ASCII string containing an unsigned 32-bit decimal integer and is not terminated by a null character. One or both of these values may be missing. Examples of the value written include the following:

- `MACINTOSH;0`
- `UTF-8;134217984`
- `UTF-8;`
- `;3071`

The methods [`init(contentsOfFile:usedEncoding:)`](nsstring/init(contentsoffile:usedencoding:).md), [`init(contentsOfURL:usedEncoding:)`](nsstring/init(contentsofurl:usedencoding:)-2c72d.md), [`stringWithContentsOfFile:usedEncoding:error:`](nsstring/stringwithcontentsoffile:usedencoding:error:.md), and [`init(contentsOfURL:usedEncoding:)`](nsstring/init(contentsofurl:usedencoding:)-9jrum.md) use this information to open the file using the right encoding.

> **Note**:  In the future this attribute may be extended compatibly by adding additional information after what’s there now, so any readers should be prepared for an arbitrarily long value for this attribute, with stuff following the `CFStringEncoding` value, separated by a non-digit.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `path`: The file to which to write the receiver. If   contains a tilde ( ) character, you must expand it with   before invoking this method.
- `useAuxiliaryFile`: If  , the receiver is written to an auxiliary file, and then the auxiliary file is renamed to  . If  , the receiver is written directly to  . The   option guarantees that  , if it exists at all, won’t be corrupted even if the system should crash during writing.
- `enc`: The encoding to use for the output. For possible values, see  .

## See Also

- [func write(to: URL, atomically: Bool, encoding: UInt) throws](nsstring/write(to:atomically:encoding:).md)
  Writes the contents of the receiver to the URL specified by `url` using the specified encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/write(tofile:atomically:encoding:))*