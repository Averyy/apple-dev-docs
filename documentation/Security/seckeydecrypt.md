# SecKeyDecrypt(_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Decrypts a block of ciphertext.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 4.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func SecKeyDecrypt(_ key: SecKey, _ padding: SecPadding, _ cipherText: UnsafePointer<UInt8>, _ cipherTextLen: Int, _ plainText: UnsafeMutablePointer<UInt8>, _ plainTextLen: UnsafeMutablePointer<Int>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

The input buffer (`cipherText`) can be the same as the output buffer (`plainText`) to reduce the amount of memory used by the function.

## Parameters

- `key`: Private key with which to decrypt the data.
- `padding`: The type of padding used. Possible values are listed in  . Typically,   is used, which removes PKCS1 padding after decryption. If you specify  , the decrypted data is returned as-is.
- `cipherText`: The data to decrypt.
- `cipherTextLen`: Length in bytes of the data in the   buffer. This must be less than or equal to the value returned by the   function.
- `plainText`: On return, the decrypted text.
- `plainTextLen`: On entry, the size of the buffer provided in the   parameter. On return, the amount of data actually placed in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeydecrypt(_:_:_:_:_:_:))*