# password

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A one-time password that the vehicle manufacturer provides.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var password: String { get set }
```

#### Discussion

When creating a digital car key, the vehicle manufacturer emails the user a one-time password to verify their identity. Set this property’s value to that password before you use the configuration to initialize [`PKAddSecureElementPassViewController`](pkaddsecureelementpassviewcontroller.md), and PassKit verifies that the passwords match as it creates the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddcarkeypassconfiguration/password)*