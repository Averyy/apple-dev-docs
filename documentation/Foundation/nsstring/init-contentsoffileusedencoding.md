# init(contentsOfFile:usedEncoding:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSString` object initialized by reading data from the file at a given path and returns by reference the encoding used to interpret the characters.

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
convenience init(contentsOfFile path: String, usedEncoding enc: UnsafeMutablePointer<UInt>?) throws
```

#### Return Value

An `NSString` object initialized by reading data from the file named by `path`. The returned object may be different from the original receiver. If the file can’t be opened or there is an encoding error, returns `nil`.

#### Discussion

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `path`: A path to a file.
- `enc`: Upon return, if the file is read successfully, contains the encoding used to interpret the file at  . For possible values, see  .

## See Also

- [convenience init(contentsOfFile: String, encoding: UInt) throws](nsstring/init(contentsoffile:encoding:).md)
  Returns an `NSString` object initialized by reading data from the file at a given path using a given encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(contentsoffile:usedencoding:))*