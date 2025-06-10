# sign(_:using:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Signs an opaque value using a cryptographic signature.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.12+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
func sign(_ signData: Data, using secureElementPass: PKSecureElementPass) async throws -> (Data, Data)
```

#### Discussion

> ❗ **Important**:  The method is available only to developers who work with Apple to enable this functionality.

PassKit may execute the completion Swift closure or an Objective-C block on an arbitrary queue.

## Parameters

- `signData`: The opaque value to sign.
- `secureElementPass`: The Secure Element pass that PassKit uses to generate the signature.
- `completion`: A Swift closure or an Objective-C block that PassKit runs when the process finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/sign(_:using:completion:))*