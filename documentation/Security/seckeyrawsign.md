# SecKeyRawSign(_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Generates a digital signature for a block of data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 4.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func SecKeyRawSign(_ key: SecKey, _ padding: SecPadding, _ dataToSign: UnsafePointer<UInt8>, _ dataToSignLen: Int, _ sig: UnsafeMutablePointer<UInt8>, _ sigLen: UnsafeMutablePointer<Int>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

The behavior this function with [`kSecPaddingNone`](secpadding/ksecpaddingnone.md) is undefined if the first byte of the data to sign is `0`; there is no way to verify leading zeroes, as they are discarded during the calculation.

## Parameters

- `key`: Private key with which to sign the data.
- `padding`: The type of padding to use. Possible values are listed in  . Use   if the data to be signed is a SHA1 digest of the actual data. If you specify  , the data is signed as-is.
- `dataToSign`: The data to be signed. Typically, a digest of the actual data is signed.
- `dataToSignLen`: Length in bytes of the data in the   buffer. When PKCS1 padding is performed, the maximum length of data that can be signed is 11 bytes less than the value returned by the   function ( ).
- `sig`: On return, the digital signature.
- `sigLen`: On entry, the size of the buffer provided in the   parameter. On return, the amount of data actually placed in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyrawsign(_:_:_:_:_:_:))*