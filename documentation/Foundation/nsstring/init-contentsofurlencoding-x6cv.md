# init(contentsOfURL:encoding:)

**Framework**: Foundation  
**Kind**: init

Returns a string created by reading data from a given URL interpreted using a given encoding.

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
convenience init(contentsOfURL url: URL, encoding enc: UInt) throws
```

#### Return Value

A string created by reading data from `URL` using the encoding, `enc`. If the URL can’t be opened or there is an encoding error, returns `nil`.

## Parameters

- `url`: The URL to read.
- `enc`: The encoding of the data at  . For possible values, see  .

## See Also

- [convenience init(contentsOfURL: URL, encoding: UInt) throws](nsstring/init(contentsofurl:encoding:)-715fw.md)
  Returns an `NSString` object initialized by reading data from a given URL interpreted using a given encoding.
- [convenience init(contentsOfURL: URL, usedEncoding: UnsafeMutablePointer<UInt>?) throws](nsstring/init(contentsofurl:usedencoding:)-9jrum.md)
  Returns a string created by reading data from a given URL and returns by reference the encoding used to interpret the data.
- [convenience init(contentsOfURL: URL, usedEncoding: UnsafeMutablePointer<UInt>?) throws](nsstring/init(contentsofurl:usedencoding:)-2c72d.md)
  Returns an `NSString` object initialized by reading data from a given URL and returns by reference the encoding used to interpret the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(contentsofurl:encoding:)-x6cv)*