# scanLocation

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The character position at which the receiver will begin its next scanning operation.

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
var scanLocation: Int { get set }
```

```objc
@property NSUInteger scanLocation;
```

## Discussion

Raises an `NSRangeException` if `index` is beyond the end of the string being scanned.

This property is useful for backing up to rescan after an error.

Rather than setting the scan location directly to skip known sequences of characters, use [`scanString(_:into:)`](./scanstring%28_,into%29.md) or [`scanCharacters(from:into:)`](./scancharacters%28from,into%29.md), which allow you to verify that the expected substring (or set of characters) is in fact present.

## See Also

### Configuring a Scanner
- [var caseSensitive: Bool](./casesensitive.md)
  Flag that indicates whether the receiver distinguishes case in the characters it scans.
- [var charactersToBeSkipped: CharacterSet?](./characterstobeskipped.md)
  Character set containing the characters the scanner ignores when looking for a scannable element.
- [var locale: Any?](./locale.md)
  The locale to use when scanning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/scanlocation)*