# isSupported

**Framework**: Core NFC  
**Kind**: property

A property that indicates whether the current device supports card session functionality.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
class var isSupported: Bool { get }
```

#### Discussion

Query this property before calling [`init()`](cardsession/init().md) to avoid raising [`fatalError(_:file:line:)`](https://developer.apple.com/documentation/Swift/fatalError(_:file:line:)) on ineligible devices.

## See Also

- [static var isEligible: Bool](cardsession/iseligible.md)
  A property that indicates whether the current system supports card session functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/issupported)*