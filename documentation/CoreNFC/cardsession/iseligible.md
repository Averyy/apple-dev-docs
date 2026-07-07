# isEligible

**Framework**: Core NFC  
**Kind**: property

A property that indicates whether the current system supports card session functionality.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
static var isEligible: Bool { get async }
```

#### Discussion

Query this property before calling [`init()`](cardsession/init().md) to avoid showing a system card session UI on ineligible devices.

## See Also

- [class var isSupported: Bool](cardsession/issupported.md)
  A property that indicates whether the current device supports card session functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/iseligible)*