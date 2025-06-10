# init(contentsOfURL:encoding:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSString` object initialized by reading data from a given URL interpreted using a given encoding.

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
convenience init(contentsOf url: URL, encoding enc: UInt) throws
```

#### Return Value

An `NSString` object initialized by reading data from `url`. The returned object may be different from the original receiver. If the URL can’t be opened or there is an encoding error, returns `nil`.

#### Discussion

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The URL to read.
- `enc`: The encoding of the file at  . For possible values, see  .

## See Also

- [convenience init(contentsOfURL: URL, encoding: UInt) throws](nsstring/init(contentsofurl:encoding:)-x6cv.md)
  Returns a string created by reading data from a given URL interpreted using a given encoding.
- [convenience init(contentsOfURL: URL, encoding: UInt) throws](nsstring/init(contentsofurl:encoding:)-x6cv.md)
  Returns a string created by reading data from a given URL interpreted using a given encoding.
- [convenience init(contentsOfURL: URL, usedEncoding: UnsafeMutablePointer<UInt>?) throws](nsstring/init(contentsofurl:usedencoding:)-9jrum.md)
  Returns a string created by reading data from a given URL and returns by reference the encoding used to interpret the data.
- [convenience init(contentsOfURL: URL, usedEncoding: UnsafeMutablePointer<UInt>?) throws](nsstring/init(contentsofurl:usedencoding:)-2c72d.md)
  Returns an `NSString` object initialized by reading data from a given URL and returns by reference the encoding used to interpret the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(contentsofurl:encoding:)-715fw)*