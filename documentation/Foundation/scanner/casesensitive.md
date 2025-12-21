# caseSensitive

**Framework**: Foundation  
**Kind**: property

Flag that indicates whether the receiver distinguishes case in the characters it scans.

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
var caseSensitive: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver distinguishes case in the characters it scans, otherwise [`false`](https://developer.apple.com/documentation/Swift/false). The default value is [`false`](https://developer.apple.com/documentation/Swift/false). Note that case sensitivity doesn’t apply to the characters to be skipped.

## See Also

- [var scanLocation: Int](scanner/scanlocation.md)
  The character position at which the receiver will begin its next scanning operation.
- [var charactersToBeSkipped: CharacterSet?](scanner/characterstobeskipped.md)
  Character set containing the characters the scanner ignores when looking for a scannable element.
- [var locale: Any?](scanner/locale.md)
  The locale to use when scanning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/casesensitive)*