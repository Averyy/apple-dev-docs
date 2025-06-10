# init(contentsOfURL:usedEncoding:)

**Framework**: Foundation  
**Kind**: init

Returns a string created by reading data from a given URL and returns by reference the encoding used to interpret the data.

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
convenience init(contentsOfURL url: URL, usedEncoding enc: UnsafeMutablePointer<UInt>?) throws
```

#### Return Value

A string created by reading data from `url`. If the URL can’t be opened or there is an encoding error, returns `nil`.

#### Discussion

This method attempts to determine the encoding at `url`.

## Parameters

- `url`: The URL from which to read data.
- `enc`: Upon return, if   is read successfully, contains the encoding used to interpret the data. For possible values, see  .

## See Also

- [convenience init(contentsOfURL: URL, encoding: UInt) throws](nsstring/init(contentsofurl:encoding:)-x6cv.md)
  Returns a string created by reading data from a given URL interpreted using a given encoding.
- [convenience init(contentsOfURL: URL, encoding: UInt) throws](nsstring/init(contentsofurl:encoding:)-715fw.md)
  Returns an `NSString` object initialized by reading data from a given URL interpreted using a given encoding.
- [convenience init(contentsOfURL: URL, usedEncoding: UnsafeMutablePointer<UInt>?) throws](nsstring/init(contentsofurl:usedencoding:)-2c72d.md)
  Returns an `NSString` object initialized by reading data from a given URL and returns by reference the encoding used to interpret the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(contentsofurl:usedencoding:)-9jrum)*