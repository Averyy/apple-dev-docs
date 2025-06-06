# removePass(_:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Removes the pass from the user’s pass library.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func removePass(_ pass: PKPass)
```

#### Discussion

This method does nothing if your app doesn’t have the appropriate entitlement.

A user must confirm adding a pass to Wallet so only remove the pass in response to a user action, such as responding to a prompt to remove the pass or an app setting.

## Parameters

- `pass`: The pass to remove.

## See Also

- [var isSecureElementPassActivationAvailable: Bool](pkpasslibrary/issecureelementpassactivationavailable.md)
  A Boolean value that indicates whether the device supports creating Secure Element passes.
- [func activate(PKSecureElementPass, activationData: Data, completion: ((Bool, (any Error)?) -> Void)?)](pkpasslibrary/activate(_:activationdata:completion:).md)
  Activates a Secure Element pass using the specified data.
- [func replacePass(with: PKPass) -> Bool](pkpasslibrary/replacepass(with:).md)
  Replaces a pass in the user’s pass library with the specified pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/removepass(_:))*