# isAtEnd

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isAtEnd) BOOL atEnd;
```

#### Discussion

[`true`](../../Swift/true.md) if the receiver has exhausted all significant characters in its string, otherwise [`false`](../../Swift/false.md).

If only characters from the set to be skipped remain, returns [`true`](../../Swift/true.md).

## See Also

### Related Documentation
- [var charactersToBeSkipped: CharacterSet?](./characterstobeskipped.md)
  Character set containing the characters the scanner ignores when looking for a scannable element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/scanner/isatend)*