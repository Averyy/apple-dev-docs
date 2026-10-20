# replacePass(with:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) replacePassWithPass:(PKPass *) pass;
```

#### Return Value

[`true`](../../Swift/true.md) if PassKit replaces the pass successfully; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The new pass replaces the existing pass with the same pass type identifier and serial number. If there isn’t such a pass in the user’s pass library, the replacement fails.

## Parameters

- `pass`: The new pass.

## See Also

### Managing passes
- [var isSecureElementPassActivationAvailable: Bool](./issecureelementpassactivationavailable.md)
  A Boolean value that indicates whether the device supports creating Secure Element passes.
- [func activate(PKSecureElementPass, activationData: Data, completion: ((Bool, (any Error)?) -> Void)?)](./activate%28_,activationdata,completion%29.md)
  Activates a Secure Element pass using the specified data.
- [func removePass(PKPass)](./removepass%28_%29.md)
  Removes the pass from the user’s pass library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/replacepass(with:))*