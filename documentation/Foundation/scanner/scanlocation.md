# scanLocation

**Framework**: Foundation  
**Kind**: property

The character position at which the receiver will begin its next scanning operation.

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
var scanLocation: Int { get set }
```

#### Discussion

Raises an `NSRangeException` if `index` is beyond the end of the string being scanned.

This property is useful for backing up to rescan after an error.

Rather than setting the scan location directly to skip known sequences of characters, use [`scanString(_:into:)`](scanner/scanstring(_:into:).md) or [`scanCharacters(from:into:)`](scanner/scancharacters(from:into:).md), which allow you to verify that the expected substring (or set of characters) is in fact present.

## See Also

- [var caseSensitive: Bool](scanner/casesensitive.md)
  Flag that indicates whether the receiver distinguishes case in the characters it scans.
- [var charactersToBeSkipped: CharacterSet?](scanner/characterstobeskipped.md)
  Character set containing the characters the scanner ignores when looking for a scannable element.
- [var locale: Any?](scanner/locale.md)
  The locale to use when scanning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/scanlocation)*