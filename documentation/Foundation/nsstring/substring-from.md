# substring(from:)

**Framework**: Foundation  
**Kind**: method

Returns a new string containing the characters of the receiver from the one at a given index to the end.

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
func substring(from: Int) -> String
```

#### Return Value

A new string containing the characters of the receiver from the one at `anIndex` to the end. If `anIndex` is equal to the length of the string, returns an empty string.

## Parameters

- `from`: Raises an   if (  - 1) lies beyond the end of the receiver.

## See Also

- [func components(separatedBy: String) -> [String]](nsstring/components(separatedby:)-238fy.md)
  Returns an array containing substrings from the receiver that have been divided by a given separator.
- [func components(separatedBy: CharacterSet) -> [String]](nsstring/components(separatedby:)-27x9g.md)
  Returns an array containing substrings from the receiver that have been divided by characters in a given set.
- [func trimmingCharacters(in: CharacterSet) -> String](nsstring/trimmingcharacters(in:).md)
  Returns a new string made by removing from both ends of the receiver characters contained in a given character set.
- [func substring(with: NSRange) -> String](nsstring/substring(with:).md)
  Returns a string object containing the characters of the receiver that lie within a given range.
- [func substring(to: Int) -> String](nsstring/substring(to:).md)
  Returns a new string containing the characters of the receiver up to, but not including, the one at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/substring(from:))*