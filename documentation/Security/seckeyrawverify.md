# SecKeyRawVerify(_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Verifies a digital signature.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 4.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func SecKeyRawVerify(_ key: SecKey, _ padding: SecPadding, _ signedData: UnsafePointer<UInt8>, _ signedDataLen: Int, _ sig: UnsafePointer<UInt8>, _ sigLen: Int) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `key`: Public key with which to verify the data.
- `padding`: The type of padding used. Possible values are listed in  . Use   if you are verifying a PKCS1-style signature with DER encoding of the digest type and the signed data is a SHA1 digest of the actual data. Specify   if no padding was used.
- `signedData`: The data for which the signature is being verified. Typically, a digest of the actual data is signed.
- `signedDataLen`: Length in bytes of the data in the   buffer.
- `sig`: The digital signature to be verified.
- `sigLen`: Length of the data in the   buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyrawverify(_:_:_:_:_:_:))*