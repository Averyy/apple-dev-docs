# title

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A name for the pass that the system displays to the user when they add or select the card.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
var title: String { get }
```

```objc
@property (nonatomic, readonly) NSString * title;
```

## See Also

### Information for displaying an addable card
- [var art: CGImage](./art.md)
  An image to that the system displays to the user when they add or select the card.
- [var identifier: String](./identifier.md)
  A developer-defined value you use to identify the card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionpassentry/title)*