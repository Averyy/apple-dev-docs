# PKIdentityButton.Label

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

A type that indicates the available labels for an identity button.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum Label
```

```c
enum PKIdentityButtonLabel : NSInteger;
```

## Topics

### Labels
- [PKIdentityButton.Label.verifyIdentity](./label/verifyidentity.md)
  A label with the text verify identity with Apple Wallet.
- [PKIdentityButton.Label.verify](./label/verify.md)
  A label with the text verify with Apple Wallet.
- [PKIdentityButton.Label.verifyAge](./label/verifyage.md)
  A label with the text verify age with Apple Wallet.
- [PKIdentityButton.Label.continue](./label/continue.md)
  A label with the text continue with Apple Wallet.
### Initializers
- [init?(rawValue: Int)](./label/init%28rawvalue%29.md)

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
- [PKIdentityButton.Style](./style.md)
  A type that indicates the available appearances for an identity button.
- [var cornerRadius: CGFloat](./cornerradius.md)
  The radius for the rounded corners on the button, in points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitybutton/label)*