# charactersToBeSkipped

**Framework**: Foundation  
**Kind**: property

Character set containing the characters the scanner ignores when looking for a scannable element.

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
var charactersToBeSkipped: CharacterSet? { get set }
```

#### Discussion

Characters to be skipped are skipped prior to the scanner examining the target. For example, if a scanner ignores spaces and you send it a [`scanInt32(_:)`](scanner/scanint32(_:).md) message, it skips spaces until it finds a decimal digit or other character. While an element is being scanned, no characters are skipped. If you scan for something made of characters in the set to be skipped (for example, using [`scanInt32(_:)`](scanner/scanint32(_:).md) when the set of characters to be skipped is the decimal digits), the result is undefined.

The characters to be skipped are treated as single values. A scanner doesn’t apply its case sensitivity setting to these characters and doesn’t attempt to match composed character sequences with anything in the set of characters to be skipped (though it does match pre-composed characters individually). If you want to skip all vowels while scanning a string, for example, you can set the characters to be skipped to those in the string “AEIOUaeiou” (plus any accented variants with pre-composed characters).

The default set to skip is the whitespace and newline character set.

## See Also

- [class var whitespacesAndNewlines: CharacterSet](nscharacterset/whitespacesandnewlines.md)
  A character set containing characters in Unicode General Category Z*, `U+000A` ~ `U+000D`, and `U+0085`.
- [var scanLocation: Int](scanner/scanlocation.md)
  The character position at which the receiver will begin its next scanning operation.
- [var caseSensitive: Bool](scanner/casesensitive.md)
  Flag that indicates whether the receiver distinguishes case in the characters it scans.
- [var locale: Any?](scanner/locale.md)
  The locale to use when scanning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/characterstobeskipped)*