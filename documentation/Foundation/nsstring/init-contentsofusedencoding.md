# init(contentsOf:usedEncoding:)

**Framework**: Foundation  
**Kind**: init

Returns an @c NSString object initialized by reading data from a given URL and returns by reference the encoding used to interpret the data.

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

An @c NSString object initialized by reading data from @c url. Returns @c nil if the URL can’t be opened or there is an encoding error.

## Parameters

- `url`: The URL to read.
- `enc`: Upon return, if the URL is read successfully, contains the encoding used to interpret the file at @c url.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/init(contentsof:usedencoding:))*