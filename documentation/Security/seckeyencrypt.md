# SecKeyEncrypt(_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Encrypts a block of plaintext.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 4.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func SecKeyEncrypt(_ key: SecKey, _ padding: SecPadding, _ plainText: UnsafePointer<UInt8>, _ plainTextLen: Int, _ cipherText: UnsafeMutablePointer<UInt8>, _ cipherTextLen: UnsafeMutablePointer<Int>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

The input buffer (`plainText`) can be the same as the output buffer (`cipherText`) to reduce the amount of memory used by the function.

## Parameters

- `key`: Public key with which to encrypt the data.
- `padding`: The type of padding to use. Possible values are listed in  . Typically,   is used, which adds PKCS1 padding before encryption. If you specify  , the data is encrypted as-is.
- `plainText`: The data to encrypt.
- `plainTextLen`: Length in bytes of the data in the   buffer. This must be less than or equal to the value returned by the   function. When PKCS1 padding is performed, the maximum length of data that can be encrypted is 11 bytes less than the value returned by the   function ( ).
- `cipherText`: On return, the encrypted text.
- `cipherTextLen`: On entry, the size of the buffer provided in the   parameter. On return, the amount of data actually placed in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyencrypt(_:_:_:_:_:_:))*