# trimmingCharacters(in:)

**Framework**: Foundation  
**Kind**: method

Returns a new string made by removing from both ends of the receiver characters contained in a given character set.

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
func trimmingCharacters(in set: CharacterSet) -> String
```

#### Return Value

A new string made by removing from both ends of the receiver characters contained in `set`. If the receiver is composed entirely of characters from `set`, the empty string is returned.

#### Discussion

Use [`whitespaces`](nscharacterset/whitespaces.md) or [`whitespacesAndNewlines`](nscharacterset/whitespacesandnewlines.md) to remove whitespace around strings.

## Parameters

- `set`: A character set containing the characters to remove from the receiver.   must not be  .

## See Also

- [func components(separatedBy: String) -> [String]](nsstring/components(separatedby:)-238fy.md)
  Returns an array containing substrings from the receiver that have been divided by a given separator.
- [func components(separatedBy: CharacterSet) -> [String]](nsstring/components(separatedby:)-27x9g.md)
  Returns an array containing substrings from the receiver that have been divided by characters in a given set.
- [func substring(from: Int) -> String](nsstring/substring(from:).md)
  Returns a new string containing the characters of the receiver from the one at a given index to the end.
- [func substring(with: NSRange) -> String](nsstring/substring(with:).md)
  Returns a string object containing the characters of the receiver that lie within a given range.
- [func substring(to: Int) -> String](nsstring/substring(to:).md)
  Returns a new string containing the characters of the receiver up to, but not including, the one at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/trimmingcharacters(in:))*