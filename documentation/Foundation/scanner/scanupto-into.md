# scanUpTo(_:into:)

**Framework**: Foundation  
**Kind**: method

Scans the string until a given string is encountered, accumulating characters into a string that’s returned by reference.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func scanUpTo(_ string: String, into result: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver scans any characters, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

If the only scanned characters are in the [`charactersToBeSkipped`](scanner/characterstobeskipped.md) character set (which by default is the whitespace and newline character set), then this method returns [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If `stopString` is present in the receiver, then on return the scan location is set to the beginning of that string.

If `stopString` is the first string in the receiver, then the method returns [`false`](https://developer.apple.com/documentation/Swift/false) and `stringValue` is not changed.

If the search string (`stopString`) isn’t present in the scanner’s source string, the remainder of the source string is put into `stringValue`, the receiver’s `scanLocation` is advanced to the end of the source string, and the method returns [`true`](https://developer.apple.com/documentation/Swift/true).

Invoke this method with `NULL` as `stringValue` to simply scan up to a given string.

## Parameters

- `string`: The string to scan up to.
- `result`: Upon return, contains any characters that were scanned.

## See Also

- [func scanCharacters(from: CharacterSet, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](scanner/scancharacters(from:into:).md)
  Scans the string as long as characters from a given character set are encountered, accumulating characters into a string that’s returned by reference.
- [func scanUpToCharacters(from: CharacterSet, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](scanner/scanuptocharacters(from:into:).md)
  Scans the string until a character from a given character set is encountered, accumulating characters into a string that’s returned by reference.
- [func scanString(String, into: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool](scanner/scanstring(_:into:).md)
  Scans a given string, returning an equivalent string object by reference if a match is found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/scanupto(_:into:))*