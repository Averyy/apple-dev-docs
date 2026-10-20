# PKPaymentButtonStyle

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

A type that indicates the available appearances for an Apple Pay button.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum PKPaymentButtonStyle
```

```c
enum PKPaymentButtonStyle : NSInteger;
```

## Topics

### Payment button styles
- [PKPaymentButtonStyle.white](./pkpaymentbuttonstyle/white.md)
  A white button with black lettering.
- [PKPaymentButtonStyle.whiteOutline](./pkpaymentbuttonstyle/whiteoutline.md)
  A white button with black lettering and a black outline.
- [PKPaymentButtonStyle.black](./pkpaymentbuttonstyle/black.md)
  A black button with white lettering.
- [PKPaymentButtonStyle.automatic](./pkpaymentbuttonstyle/automatic.md)
  A button that automatically changes its appearance when the user switches between Light Mode and Dark Mode.
### Initializers
- [init?(rawValue: Int)](./pkpaymentbuttonstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring the appearance
- [enum PKPaymentButtonType](./pkpaymentbuttontype.md)
  The Apple Pay button types you can display to initiate Apple Pay transactions.
- [var cornerRadius: CGFloat](./pkpaymentbutton/cornerradius.md)
  The radius, in points, for the rounded corners on the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentbuttonstyle)*