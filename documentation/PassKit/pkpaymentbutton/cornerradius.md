# cornerRadius

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The radius, in points, for the rounded corners on the button.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var cornerRadius: CGFloat { get set }
```

#### Discussion

To remove the rounded corners, set this value to 0.0.

The default value is `4.0`.

## See Also

- [enum PKPaymentButtonType](pkpaymentbuttontype.md)
  The Apple Pay button types you can display to initiate Apple Pay transactions.
- [enum PKPaymentButtonStyle](pkpaymentbuttonstyle.md)
  A type that indicates the available appearances for an Apple Pay button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentbutton/cornerradius)*