# activate(_:activationData:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Activates a Secure Element pass using the specified data.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
func activate(_ secureElementPass: PKSecureElementPass, activationData: Data) async throws -> Bool
```

#### Discussion

You must provision the Secure Element pass and make sure it’s in the [`PKSecureElementPass.PassActivationState.requiresActivation`](pksecureelementpass/passactivationstate-swift.enum/requiresactivation.md) state before you call this method.

## Parameters

- `secureElementPass`: The Secure Element pass to activate.
- `activationData`: A cryptographic value that the activation process requires.
- `completion`: A closure that PassKit executes after it attempts activation.

## See Also

- [var isSecureElementPassActivationAvailable: Bool](pkpasslibrary/issecureelementpassactivationavailable.md)
  A Boolean value that indicates whether the device supports creating Secure Element passes.
- [func replacePass(with: PKPass) -> Bool](pkpasslibrary/replacepass(with:).md)
  Replaces a pass in the user’s pass library with the specified pass.
- [func removePass(PKPass)](pkpasslibrary/removepass(_:).md)
  Removes the pass from the user’s pass library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/activate(_:activationdata:completion:))*