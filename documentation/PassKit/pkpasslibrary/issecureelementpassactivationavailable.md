# isSecureElementPassActivationAvailable

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A Boolean value that indicates whether the device supports creating Secure Element passes.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.12+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var isSecureElementPassActivationAvailable: Bool { get }
```

#### Discussion

Secure Element pass activation requires a special entitlement that Apple provides. If the entitlement isn’t present, this property’s value is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func activate(PKSecureElementPass, activationData: Data, completion: ((Bool, (any Error)?) -> Void)?)](pkpasslibrary/activate(_:activationdata:completion:).md)
  Activates a Secure Element pass using the specified data.
- [func replacePass(with: PKPass) -> Bool](pkpasslibrary/replacepass(with:).md)
  Replaces a pass in the user’s pass library with the specified pass.
- [func removePass(PKPass)](pkpasslibrary/removepass(_:).md)
  Removes the pass from the user’s pass library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/issecureelementpassactivationavailable)*