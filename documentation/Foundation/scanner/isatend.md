# isAtEnd

**Framework**: Foundation  
**Kind**: property

Flag that indicates whether the receiver has exhausted all significant characters.

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
var isAtEnd: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver has exhausted all significant characters in its string, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

If only characters from the set to be skipped remain, returns [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var charactersToBeSkipped: CharacterSet?](scanner/characterstobeskipped.md)
  Character set containing the characters the scanner ignores when looking for a scannable element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/isatend)*