# replacePass(with:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Replaces a pass in the user’s pass library with the specified pass.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func replacePass(with pass: PKPass) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if PassKit replaces the pass successfully; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The new pass replaces the existing pass with the same pass type identifier and serial number. If there isn’t such a pass in the user’s pass library, the replacement fails.

## Parameters

- `pass`: The new pass.

## See Also

- [var isSecureElementPassActivationAvailable: Bool](pkpasslibrary/issecureelementpassactivationavailable.md)
  A Boolean value that indicates whether the device supports creating Secure Element passes.
- [func activate(PKSecureElementPass, activationData: Data, completion: ((Bool, (any Error)?) -> Void)?)](pkpasslibrary/activate(_:activationdata:completion:).md)
  Activates a Secure Element pass using the specified data.
- [func removePass(PKPass)](pkpasslibrary/removepass(_:).md)
  Removes the pass from the user’s pass library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/replacepass(with:))*