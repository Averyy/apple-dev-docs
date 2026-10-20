# PKIdentityButton.Style

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

A type that indicates the available appearances for an identity button.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum Style
```

```c
enum PKIdentityButtonStyle : NSInteger;
```

## Topics

### Styles
- [PKIdentityButton.Style.black](./style/black.md)
  A style that represents a black button with white lettering.
- [PKIdentityButton.Style.blackOutline](./style/blackoutline.md)
  A style that represents a black button with a light outline.
### Initializers
- [init?(rawValue: Int)](./style/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the appearance
- [PKIdentityButton.Label](./label.md)
  A type that indicates the available labels for an identity button.
- [var cornerRadius: CGFloat](./cornerradius.md)
  The radius for the rounded corners on the button, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitybutton/style)*