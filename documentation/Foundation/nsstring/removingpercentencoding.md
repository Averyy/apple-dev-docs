# removingPercentEncoding

**Framework**: Foundation  
**Kind**: property

Returns a new string made from the receiver by replacing all percent encoded sequences with the matching UTF-8 characters.

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
var removingPercentEncoding: String? { get }
```

#### Return Value

A new string with the percent-encoded sequences removed, or `nil` if the receiver contains an invalid percent-encoding sequence.

#### Discussion

> ❗ **Important**:  You must call this method only on strings that you know to be percent-encoded. Calling this method on strings that are not percent-encoded can lead to misinterpreting a percent character as the beginning of a percent-encoded sequence.

## See Also

- [func replacingPercentEscapes(using: UInt) -> String?](nsstring/replacingpercentescapes(using:).md)
  Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding.
- [func addingPercentEscapes(using: UInt) -> String?](nsstring/addingpercentescapes(using:).md)
  Returns a representation of the receiver using a given encoding to determine the percent escapes necessary to convert the receiver into a legal URL string.
- [func addingPercentEncoding(withAllowedCharacters: CharacterSet) -> String?](nsstring/addingpercentencoding(withallowedcharacters:).md)
  Returns a new string made from the receiver by replacing all characters not in the specified set with percent-encoded characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/removingpercentencoding)*