# locale

**Framework**: Foundation  
**Kind**: property

The locale to use when scanning.

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
var locale: Any? { get set }
```

#### Discussion

A scanner’s locale affects the way it interprets numeric values from the string. In particular, a scanner uses the locale’s decimal separator to distinguish the integer and fractional parts of floating-point representations. A scanner with no locale set uses non-localized values. New scanners have no locale by default.

## See Also

- [var scanLocation: Int](scanner/scanlocation.md)
  The character position at which the receiver will begin its next scanning operation.
- [var caseSensitive: Bool](scanner/casesensitive.md)
  Flag that indicates whether the receiver distinguishes case in the characters it scans.
- [var charactersToBeSkipped: CharacterSet?](scanner/characterstobeskipped.md)
  Character set containing the characters the scanner ignores when looking for a scannable element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/locale)*