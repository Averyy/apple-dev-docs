# sign(_:using:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Signs an opaque value using a cryptographic signature.

**Availability**:
- iOS 13.4+ - Deprecated in 26.0
- iPadOS 13.4+ - Deprecated in 26.0
- Mac Catalyst 13.4+ - Deprecated in 26.0
- macOS 10.12+
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 6.2+ - Deprecated in 26.0

> **Deprecated**: No longer supported

## Declaration

```swift
func sign(_ signData: Data, using secureElementPass: PKSecureElementPass, completion: @escaping @Sendable (Data?, Data?, (any Error)?) -> Void)
```

```swift
func sign(_ signData: Data, using secureElementPass: PKSecureElementPass) async throws -> (Data, Data)
```

```objc
- (void) signData:(NSData *) signData withSecureElementPass:(PKSecureElementPass *) secureElementPass completion:(void (^)(NSData *signedData, NSData *signature, NSError *error)) completion;
```

## Discussion

> ❗ **Important**:  The method is available only to developers who work with Apple to enable this functionality.

PassKit may execute the completion Swift closure or an Objective-C block on an arbitrary queue.

## Parameters

- `signData`: The opaque value to sign.
- `secureElementPass`: The Secure Element pass that PassKit uses to generate the signature.
- `completion`: A Swift closure or an Objective-C block that PassKit runs when the process finishes.

  - **`signedData`**: The signed value.
  - **`signature`**: The cryptographic signature that PassKit uses to sign the value.
  - **`error`**: If the process fails, an error that describes the failure; otherwise, `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasslibrary/sign(_:using:completion:))*