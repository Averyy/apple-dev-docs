# init(contentsOfURL:usedEncoding:)

**Framework**: Foundation  
**Kind**: init

Returns an `NSString` object initialized by reading data from a given URL and returns by reference the encoding used to interpret the data.

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
convenience init(contentsOf url: URL, usedEncoding enc: UnsafeMutablePointer<UInt>?) throws
```

#### Return Value

An `NSString` object initialized by reading data from `url`. If `url` can’t be opened or the encoding cannot be determined, returns `nil`. The returned initialized object might be different from the original receiver

#### Discussion

To read data with an unknown encoding, pass `0` as the `enc` parameter as in:

```objc
    NSURL *textFileURL = …;
    NSStringEncoding encoding = 0;
    NSError *error = nil;
    NSString *string = [[NSString alloc] initWithContentsOfURL:textFileURL usedEncoding:&encoding error:&error];
```

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The URL from which to read data.
- `enc`: Upon return, if   is read successfully, contains the encoding used to interpret the data. For possible values, see  .

## See Also

- [convenience init(contentsOfURL: URL, usedEncoding: UnsafeMutablePointer<UInt>?) throws](nsstring/init(contentsofurl:usedencoding:)-9jrum.md)
  Returns a string created by reading data from a given URL and returns by reference the encoding used to interpret the data.
- [convenience init(contentsOfURL: URL, encoding: UInt) throws](nsstring/init(contentsofurl:encoding:)-x6cv.md)
  Returns a string created by reading data from a given URL interpreted using a given encoding.
- [convenience init(contentsOfURL: URL, encoding: UInt) throws](nsstring/init(contentsofurl:encoding:)-715fw.md)
  Returns an `NSString` object initialized by reading data from a given URL interpreted using a given encoding.
- [convenience init(contentsOfURL: URL, usedEncoding: UnsafeMutablePointer<UInt>?) throws](nsstring/init(contentsofurl:usedencoding:)-9jrum.md)
  Returns a string created by reading data from a given URL and returns by reference the encoding used to interpret the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(contentsofurl:usedencoding:)-2c72d)*