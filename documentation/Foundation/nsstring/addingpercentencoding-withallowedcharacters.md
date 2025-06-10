# addingPercentEncoding(withAllowedCharacters:)

**Framework**: Foundation  
**Kind**: method

Returns a new string made from the receiver by replacing all characters not in the specified set with percent-encoded characters.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addingPercentEncoding(withAllowedCharacters allowedCharacters: CharacterSet) -> String?
```

#### Return Value

Returns the encoded string, or `nil` if the transformation is not possible.

#### Discussion

Entire URL strings cannot be percent-encoded, because each URL component specifies a different set of allowed characters. For example, the query component of a URL allows the “`@`” character, but that character must be percent-encoded in the password component.

UTF-8 encoding is used to determine the correct percent-encoded characters. Any characters in `allowedCharacters` outside of the 7-bit ASCII range are ignored.

> ❗ **Important**:  You must not call this method on strings that are already percent-encoded. Calling this method on strings that are already percent-encoded will cause percent characters in a percent-encoded sequence to be percent-encoded twice.

## Parameters

- `allowedCharacters`: The characters not replaced in the string. Typically, you specify one of the predefined character sets for a particular URL component, such as   or  .

## See Also

- [func replacingPercentEscapes(using: UInt) -> String?](nsstring/replacingpercentescapes(using:).md)
  Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding.
- [func addingPercentEscapes(using: UInt) -> String?](nsstring/addingpercentescapes(using:).md)
  Returns a representation of the receiver using a given encoding to determine the percent escapes necessary to convert the receiver into a legal URL string.
- [var removingPercentEncoding: String?](nsstring/removingpercentencoding.md)
  Returns a new string made from the receiver by replacing all percent encoded sequences with the matching UTF-8 characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/addingpercentencoding(withallowedcharacters:))*