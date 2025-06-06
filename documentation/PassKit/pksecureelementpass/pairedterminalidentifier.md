# pairedTerminalIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The unique identifier of the paired terminal.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var pairedTerminalIdentifier: String? { get }
```

#### Discussion

PassKit can create a Secure Element pass during an exchange with a terminal. For example, when creating a digital car key. You can use this property’s value to identify the terminal.

## See Also

- [var deviceAccountIdentifier: String](pksecureelementpass/deviceaccountidentifier.md)
  The unique identifier for the device-specific account number.
- [var deviceAccountNumberSuffix: String](pksecureelementpass/deviceaccountnumbersuffix.md)
  A display-ready version of the device-specific account number.
- [var devicePassIdentifier: String?](pksecureelementpass/devicepassidentifier.md)
  An opaque value for the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksecureelementpass/pairedterminalidentifier)*