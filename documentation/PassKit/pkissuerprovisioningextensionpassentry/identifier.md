# identifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A developer-defined value you use to identify the card.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (nonatomic, readonly) NSString * identifier;
```

## See Also

### Information for displaying an addable card
- [var art: CGImage](./art.md)
  An image to that the system displays to the user when they add or select the card.
- [var title: String](./title.md)
  A name for the pass that the system displays to the user when they add or select the card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionpassentry/identifier)*